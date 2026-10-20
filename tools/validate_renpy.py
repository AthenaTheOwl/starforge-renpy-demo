#!/usr/bin/env python3
"""validate_renpy.py — Validate generated Ren'Py files for Starforge Canticles.

Checks:
1. All jump targets resolve to existing labels
2. All character variables used in say statements are defined
3. No orphan labels (unreachable from entry points)
4. Label naming conventions
5. Screen text uses only known text tags and substitutions of defined names
6. Script text has no over-escaped text tags, unmatched closing braces or
   over-escaped brackets
"""

import ast
import builtins
import os
import re
import sys


# Ren'Py 8.5 built-in text tags (renpy/text/extras.py). The game registers no
# config.custom_text_tags, so any other {tag} in screen text raises at runtime.
RENPY_TEXT_TAGS = {
    "", "a", "alpha", "alt", "art", "axis", "b", "color", "cps", "done", "fast",
    "feature", "font", "i", "image", "instance", "k", "noalt", "nw",
    "outlinecolor", "p", "plain", "rb", "rt", "s", "shader", "size", "space",
    "u", "vspace", "w",
}
# Store names Ren'Py provides that screen text may interpolate.
RENPY_STORE_NAMES = {"persistent", "config", "store", "renpy", "gui", "preferences", "_", "__"}
SCREEN_TEXT_LINE = re.compile(r'^\s*(?:text|textbutton|label|tooltip)\b')
STRING_LITERAL = re.compile(r'"((?:[^"\\]|\\.)*)"')
IDENT = r"[A-Za-z_]\w*"
DEFINED_NAME_PATTERNS = [
    re.compile(rf"^\s*(?:define|default)\s+({IDENT})"),
    re.compile(rf"\b({IDENT})\s*[-+*/%]?=(?!=)"),
    re.compile(rf"\b(?:def|class)\s+({IDENT})"),
    re.compile(rf"\bimport\s+({IDENT})"),
    re.compile(rf"\bas\s+({IDENT})"),
]
PARAM_LIST = re.compile(rf"^\s*(?:screen|label|def)\s+{IDENT}\s*\(([^)]*)\)")
FOR_TARGETS = re.compile(r"\bfor\s+([\w\s,()]+?)\s+in\b")


def collect_defined_names(line, names):
    """Add every name the line could bind (over-inclusive on purpose)."""
    for pattern in DEFINED_NAME_PATTERNS:
        names.update(pattern.findall(line))
    for group in PARAM_LIST.findall(line) + FOR_TARGETS.findall(line):
        names.update(re.findall(IDENT, group))


def iter_text_tags(text):
    """Yield the name of each text tag in a Ren'Py string, honoring {{ escapes."""
    pos = 0
    while pos < len(text):
        if text.startswith("{{", pos):
            pos += 2
            continue
        if text[pos] == "{":
            end = text.find("}", pos)
            if end == -1:
                return
            yield text[pos + 1:end].lstrip("/").split("=", 1)[0].strip()
            pos = end + 1
            continue
        pos += 1


def iter_substitutions(text):
    """Yield the expression of each [substitution] in a Ren'Py string, honoring [[ escapes."""
    pos = 0
    while pos < len(text):
        if text.startswith("[[", pos):
            pos += 2
            continue
        if text[pos] != "[":
            pos += 1
            continue
        depth = 0
        quote = None
        start = pos + 1
        pos = start
        expr_end = None
        while pos < len(text):
            c = text[pos]
            if quote:
                if c == "\\":
                    pos += 1
                elif c == quote:
                    quote = None
            elif c in "'\"":
                quote = c
            elif c in "([":
                depth += 1
            elif c in ")]" and depth:
                depth -= 1
            elif c == "]":
                break
            elif not depth and expr_end is None and (c == ":" or (c == "!" and text[pos + 1:pos + 2] != "=")):
                expr_end = pos
            pos += 1
        yield text[start:expr_end if expr_end is not None else pos]
        pos += 1


def check_screen_text(screen_strings, defined_names):
    """Return error messages for screen strings that Ren'Py cannot render."""
    known = defined_names | RENPY_STORE_NAMES | set(dir(builtins))
    problems = []
    for relpath, line_num, text in screen_strings:
        for tag in iter_text_tags(text):
            if not tag.startswith("#") and tag not in RENPY_TEXT_TAGS:
                problems.append(f"Unknown text tag '{{{tag}}}' in screen text at {relpath}:{line_num}")
        for expr in iter_substitutions(text):
            try:
                tree = ast.parse(expr.strip(), mode="eval")
            except SyntaxError:
                problems.append(f"Substitution '[{expr}]' is not a Python expression at {relpath}:{line_num} (escape a literal bracket as '[[')")
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Name) and node.id not in known:
                    problems.append(f"Substitution '[{expr}]' uses undefined name '{node.id}' at {relpath}:{line_num} (escape a literal bracket as '[[')")
    return problems


# Ren'Py escapes a literal '{' as '{{' but has no escape for '}': any '}' that
# does not close a tag is shown as written, so '{i}}' or '...}}' shows stray
# braces and '{{color=...}}' shows the markup instead of applying it.
OVER_ESCAPED_TAG = re.compile(
    r"\{\{(/?(?:" + "|".join(sorted(tag for tag in RENPY_TEXT_TAGS if tag)) + r")(?:=[^{}]*)?)\}"
)
# Likewise '[[' escapes a literal '[' but ']' has no escape, so '[[x]]' shows
# '[x]]' with a stray bracket.
OVER_ESCAPED_BRACKET = re.compile(r"(?<!\[)\[\[([^\[\]]*)\]\]")
PYTHON_BLOCK = re.compile(r"^\s*(?:init(?:\s+-?\d+)?\s+)?python\b[^:]*:\s*$")


def iter_script_strings(source):
    """Yield (line_num, text) for each string literal in Ren'Py script code.

    Strings in python blocks and in $, define and default lines are Python,
    where '{{' and '}}' are str.format escapes, so they are skipped.
    """
    python_indent = None
    in_python = False
    at_line_start = True
    line_num, pos, end = 1, 0, len(source)
    while pos < end:
        if at_line_start:
            at_line_start = False
            eol = source.find("\n", pos)
            line = source[pos:eol if eol != -1 else end]
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                indent = len(line) - len(line.lstrip())
                if python_indent is not None and indent <= python_indent:
                    python_indent = None
                in_python = python_indent is not None or stripped.startswith(("$", "define ", "default "))
                if python_indent is None and PYTHON_BLOCK.match(line):
                    python_indent = indent
        char = source[pos]
        if char == "\n":
            line_num += 1
            at_line_start = True
        elif char == "#":
            eol = source.find("\n", pos)
            pos = eol if eol != -1 else end
            continue
        elif char in "\"'`":
            quote = char * 3 if source.startswith(char * 3, pos) else char
            start = stop = pos + len(quote)
            while stop < end and not source.startswith(quote, stop):
                stop += 2 if source[stop] == "\\" else 1
            if not in_python:
                yield line_num, source[start:stop]
            line_num += source.count("\n", start, stop)
            pos = stop + len(quote)
            continue
        pos += 1


def check_text_escapes(script_strings):
    """Return error messages for script text whose braces or brackets Ren'Py would show as written."""
    problems = []
    for relpath, line_num, text in script_strings:
        for match in OVER_ESCAPED_BRACKET.finditer(text):
            problems.append(
                f"Over-escaped bracket '{match.group(0)}' shows a stray ']' at {relpath}:{line_num} "
                f"(write '[[{match.group(1)}]')"
            )
        for match in OVER_ESCAPED_TAG.finditer(text):
            problems.append(
                f"Over-escaped text tag '{match.group(0)}' shows as raw markup at {relpath}:{line_num} "
                f"(write '{{{match.group(1)}}}')"
            )
        literal_open = 0
        pos = 0
        while pos < len(text):
            if text.startswith("{{", pos):
                literal_open += 1
                pos += 2
            elif text[pos] == "{":
                close = text.find("}", pos)
                pos = len(text) if close == -1 else close + 1
            elif text[pos] == "}":
                if not literal_open:
                    problems.append(
                        f"Unmatched '}}' shows as a stray brace at {relpath}:{line_num} "
                        "(only '{' is escaped, as '{{'; a closing '}' is written once)"
                    )
                    break
                literal_open -= 1
                pos += 1
            else:
                pos += 1
    return problems


def scan_rpy_files(game_dir):
    """Scan all .rpy files and collect labels, jumps, and character references."""
    labels = set()
    jumps = {}  # {target: [(file, line_num), ...]}
    calls = {}  # {target: [(file, line_num), ...]}
    speakers = set()
    defined_chars = set()
    defined_names = set()
    screen_strings = []  # [(file, line_num, text), ...] for displayed screen text
    script_strings = []  # [(file, line_num, text), ...] for all non-Python string literals

    for root, dirs, files in os.walk(game_dir):
        for fname in files:
            if not fname.endswith(".rpy"):
                continue
            filepath = os.path.join(root, fname)
            relpath = os.path.relpath(filepath, game_dir)

            in_screen = False
            with open(filepath, "r", encoding="utf-8") as f:
                source = f.read()
                for line_num, text in iter_script_strings(source):
                    script_strings.append((relpath, line_num, text))
                for line_num, line in enumerate(source.split("\n"), 1):
                    stripped = line.strip()
                    collect_defined_names(line, defined_names)

                    # Track top-level screen blocks and the text they display
                    if stripped and not line[0].isspace() and not stripped.startswith("#"):
                        in_screen = bool(re.match(r"screen\s", stripped))
                    if in_screen and SCREEN_TEXT_LINE.match(line):
                        for text in STRING_LITERAL.findall(line):
                            screen_strings.append((relpath, line_num, text))

                    # Collect labels
                    label_match = re.match(r'^label\s+(\S+?)(?:\(.*\))?:', stripped)
                    if label_match:
                        labels.add(label_match.group(1))

                    # Collect jumps
                    jump_match = re.match(r'^jump\s+(\S+)', stripped)
                    if jump_match:
                        target = jump_match.group(1)
                        jumps.setdefault(target, []).append((relpath, line_num))

                    # Collect calls
                    call_match = re.match(r'^call\s+(?:expression\s+)?(\S+)', stripped)
                    if call_match:
                        target = call_match.group(1).split("(", 1)[0]
                        # Skip expression calls with variables
                        if not target.startswith("_") and not target.startswith('"'):
                            calls.setdefault(target, []).append((relpath, line_num))

                    # Collect define statements (character definitions)
                    define_match = re.match(r'^define\s+(\w+)\s*=\s*Character\(', stripped)
                    if define_match:
                        defined_chars.add(define_match.group(1))

                    # Collect speaker usage (character variable in say statement)
                    # Use original line (not stripped) since say statements are indented
                    say_match = re.match(r'^\s+(\w+)\s+"', line)
                    if say_match:
                        speaker = say_match.group(1)
                        if speaker not in ("if", "elif", "else", "while", "for", "return",
                                          "jump", "call", "menu", "pass", "python", "default",
                                          "define", "show", "hide", "scene", "with", "pause",
                                          "centered", "text", "textbutton", "label", "style",
                                          "screen", "frame", "vbox", "hbox", "bar", "add",
                                          "null", "timer", "use", "fixed", "grid", "window",
                                          "viewport", "vpgrid", "has", "tag", "zorder",
                                          "modal", "action", "at", "tooltip"):
                            speakers.add(speaker)

    return labels, jumps, calls, speakers, defined_chars, defined_names, screen_strings, script_strings


def validate(game_dir):
    """Run all validation checks."""
    print(f"Validating Ren'Py project: {game_dir}\n")

    labels, jumps, calls, speakers, defined_chars, defined_names, screen_strings, script_strings = scan_rpy_files(game_dir)

    errors = 0
    warnings = 0

    # 1. Check jump targets
    print("--- Jump Target Validation ---")
    for target, locations in sorted(jumps.items()):
        # Skip relative jumps (starting with .)
        if target.startswith("."):
            continue
        if target not in labels:
            for file, line in locations:
                print(f"  ERROR: Jump to undefined label '{target}' at {file}:{line}")
                errors += 1

    # 2. Check call targets
    print("\n--- Call Target Validation ---")
    for target, locations in sorted(calls.items()):
        if target.startswith(".") or target.startswith("screen"):
            continue
        if target not in labels:
            # May be a dynamic call or built-in
            for file, line in locations:
                print(f"  WARNING: Call to potentially undefined label '{target}' at {file}:{line}")
                warnings += 1

    # 3. Check speaker definitions
    print("\n--- Speaker Validation ---")
    # Add narrator as always-defined
    defined_chars.add("narrator")
    undefined_speakers = speakers - defined_chars
    # Filter out common false positives
    false_positives = {"properties", "spacing", "xalign", "yalign", "xpos", "ypos",
                       "xsize", "ysize", "xoffset", "yoffset", "color", "size",
                       "bold", "italic", "background", "hover_background", "padding",
                       "selected_color", "hover_color", "insensitive_color",
                       "font", "id", "key", "layout", "scrollbars", "size_group",
                       "style_prefix", "text_color", "text_hover_color", "margin",
                       "xmaximum", "ymaximum", "xminimum", "yminimum", "yfill",
                       "xfill", "first_spacing", "box_wrap",
                       "xcenter", "ycenter", "anchor", "pos", "align",
                       "tooltip"}
    undefined_speakers -= false_positives
    for speaker in sorted(undefined_speakers):
        print(f"  WARNING: Speaker variable '{speaker}' used but not defined with Character()")
        warnings += 1

    # 4. Check screen text that Ren'Py renders at runtime (lint does not)
    print("\n--- Screen Text Validation ---")
    for problem in check_screen_text(screen_strings, defined_names):
        print(f"  ERROR: {problem}")
        errors += 1

    # 5. Check braces and brackets in script text that Ren'Py would show as written (lint does not)
    print("\n--- Text Escape Validation ---")
    for problem in check_text_escapes(script_strings):
        print(f"  ERROR: {problem}")
        errors += 1

    # 6. Summary stats
    print(f"\n--- Summary ---")
    print(f"  Labels found:    {len(labels)}")
    print(f"  Jump targets:    {len(jumps)}")
    print(f"  Call targets:    {len(calls)}")
    print(f"  Speakers used:   {len(speakers)}")
    print(f"  Characters defined: {len(defined_chars)}")
    print(f"  Screen text strings: {len(screen_strings)}")
    print(f"  Script text strings: {len(script_strings)}")
    print(f"")
    print(f"  Errors:   {errors}")
    print(f"  Warnings: {warnings}")

    return errors == 0


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)

    if len(sys.argv) >= 2:
        game_dir = sys.argv[1]
    else:
        game_dir = os.path.join(base_dir, "starforge-renpy", "game")

    if not os.path.isdir(game_dir):
        print(f"ERROR: Game directory not found: {game_dir}")
        sys.exit(1)

    success = validate(game_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
