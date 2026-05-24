#!/usr/bin/env python3
"""Run deterministic release gates for the Ren'Py demo repo."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED_NAMES = {"errors.txt", "log.txt", "traceback.txt"}
GENERATED_SUFFIXES = {".rpyc", ".rpyb", ".save"}
GENERATED_DIRS = [ROOT / "game" / "cache", ROOT / "game" / "saves"]
GAME_ROOT = ROOT / "game"


def run(label: str, command: list[str], output_transform=None, failure_predicate=None) -> int:
    print(f"\n== {label} ==", flush=True)
    print("+ " + " ".join(command), flush=True)
    result = subprocess.run(
        command,
        cwd=ROOT,
        check=False,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    output = output_transform(result.stdout) if output_transform else result.stdout
    if output:
        emit_output(output, needs_newline=not output.endswith("\n"))
    if failure_predicate and failure_predicate(result.stdout or ""):
        return 1
    return result.returncode


def emit_output(text: str, needs_newline: bool = False) -> None:
    if needs_newline:
        text = f"{text}\n"
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        sys.stdout.buffer.write(text.encode("utf-8", errors="replace"))
    sys.stdout.flush()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_under_generated_dir(path: Path) -> bool:
    return any(path == generated_dir or generated_dir in path.parents for generated_dir in GENERATED_DIRS)


def find_generated_artifacts() -> tuple[list[Path], list[Path]]:
    dirs = [path for path in GENERATED_DIRS if path.exists()]
    files = [ROOT / name for name in GENERATED_NAMES if (ROOT / name).is_file()]

    if GAME_ROOT.exists():
        for path in GAME_ROOT.rglob("*"):
            if is_under_generated_dir(path):
                continue
            if path.is_file() and path.suffix in GENERATED_SUFFIXES:
                files.append(path)

    return sorted(dirs), sorted(files)


def clean_generated_artifacts() -> None:
    dirs, files = find_generated_artifacts()
    for path in files:
        path.unlink()
    for path in dirs:
        if path.exists():
            shutil.rmtree(path)


def verify_no_generated_artifacts() -> int:
    dirs, files = find_generated_artifacts()
    artifacts = [*dirs, *files]
    if not artifacts:
        return 0

    print("\n== Generated artifact check ==")
    print("release gate found generated Ren'Py artifacts:")
    for path in artifacts:
        print(f"- {rel(path)}")
    print("remove them manually or rerun with --clean to remove known Ren'Py churn")
    return 1


def collect_renpy_lint_diagnostics(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return [
        line for line in lines
        if re.search(r"\.rpy:\d+", line) or "already defined at" in line
    ]


def has_renpy_lint_diagnostics(text: str) -> bool:
    return bool(collect_renpy_lint_diagnostics(text))


def summarize_renpy_lint_output(text: str) -> str:
    diagnostics = collect_renpy_lint_diagnostics(text)
    if not diagnostics:
        return text

    category_patterns = {
        "unknown_text_tags": "Text tag",
        "tag_mismatches": "Close text tag",
        "duplicate_defaults": "already defined at",
        "format_percent": "Unknown string format code",
        "missing_images": "is not an image",
        "built_in_name_replacements": "replaces a python built-in name",
    }
    counts = {
        category: sum(1 for line in diagnostics if needle in line)
        for category, needle in category_patterns.items()
    }
    uncategorized = len(diagnostics) - sum(counts.values())

    summary = [f"Ren'Py lint emitted {len(diagnostics)} diagnostic line(s)."]
    summary.extend(f"- {category}: {count}" for category, count in counts.items() if count)
    if uncategorized:
        summary.append(f"- uncategorized: {uncategorized}")
    summary.append("")
    summary.append("First diagnostics:")
    summary.extend(f"- {line}" for line in diagnostics[:20])
    if len(diagnostics) > 20:
        summary.append(f"- ... {len(diagnostics) - 20} more diagnostic line(s) omitted")
    return "\n".join(summary) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean", action="store_true", help="Remove known generated Ren'Py artifacts before and after checks.")
    parser.add_argument("--fail-on-generated", action="store_true", help="Compatibility flag; generated Ren'Py artifacts are always release-blocking.")
    parser.add_argument("--fail-on-renpy-lint-diagnostics", action="store_true", help="Fail Ren'Py lint if it emits diagnostic lines even with exit 0.")
    parser.add_argument("--renpy", help="Path to renpy.exe or renpy.sh.")
    parser.add_argument("--require-renpy", action="store_true", help="Fail if Ren'Py lint cannot run.")
    args = parser.parse_args()
    if args.clean:
        clean_generated_artifacts()

    checks = [
        ("Python tests", [sys.executable, "-m", "pytest"]),
        ("Static Ren'Py source validation", [sys.executable, "tools/validate_renpy.py", "game"]),
        ("Ren'Py playtest path/dead-letter audit", [sys.executable, "tools/playtest_audit.py"]),
    ]

    failures = verify_no_generated_artifacts()
    for label, command in checks:
        failures += 1 if run(label, command) else 0

    renpy = args.renpy or os.environ.get("RENPY_EXECUTABLE")
    if renpy:
        failures += 1 if run(
            "Ren'Py lint",
            [renpy, ".", "lint"],
            output_transform=summarize_renpy_lint_output,
            failure_predicate=has_renpy_lint_diagnostics if args.fail_on_renpy_lint_diagnostics else None,
        ) else 0
        if args.clean:
            clean_generated_artifacts()
        failures += verify_no_generated_artifacts()
    elif args.require_renpy:
        print("\n== Ren'Py lint ==")
        print("missing Ren'Py executable; set RENPY_EXECUTABLE or pass --renpy")
        failures += 1
    else:
        print("\n== Ren'Py lint ==")
        print("skipped; set RENPY_EXECUTABLE or pass --renpy to include engine lint")

    if failures:
        print(f"\nrelease gate failed: {failures} check(s) failed")
        return 1

    print("\nrelease gate passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
