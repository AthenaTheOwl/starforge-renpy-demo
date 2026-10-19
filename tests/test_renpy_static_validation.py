import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_static_renpy_validation_has_no_errors() -> None:
    result = subprocess.run(
        [sys.executable, "tools/validate_renpy.py", "game"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )

    assert result.returncode == 0, result.stdout


def test_screen_text_check_flags_strings_renpy_cannot_render() -> None:
    sys.path.insert(0, str(ROOT / "tools"))
    import validate_renpy

    strings = [
        ("screens/x.rpy", 1, "{color=#d4a843}[NEW]{/color} [_d_name]"),
        ("screens/x.rpy", 2, "{color=#555555}{icon=lock} [_d_name]{/color}"),
        ("screens/x.rpy", 3, "{color=#d4a843}[[NEW]{/color} [_d_name] [persistent.count + 1] [message!tq]"),
    ]

    problems = validate_renpy.check_screen_text(strings, {"_d_name", "message"})

    assert len(problems) == 2, problems
    assert "undefined name 'NEW'" in problems[0] and "x.rpy:1" in problems[0]
    assert "Unknown text tag '{icon}'" in problems[1] and "x.rpy:2" in problems[1]


def test_text_escape_check_flags_braces_renpy_shows_as_written() -> None:
    sys.path.insert(0, str(ROOT / "tools"))
    import validate_renpy

    strings = [
        ("x.rpy", 1, "{{color=#808090}}{b}NOTE:{/b}{{/color}}"),
        ("x.rpy", 2, "{i}}{{WAFFLE.BAT// status}}{/i}}"),
        ("x.rpy", 3, "{color=cyan}}{{BEE:: signal}}{/color}}"),
        ("x.rpy", 4, "{color=#808090}{b}NOTE:{/b}{/color}"),
        ("x.rpy", 5, "{i}{{WAFFLE.BAT// a | {{BEE:: b} | c}{/i}"),
        ("x.rpy", 6, "{{OUTER {{INNER}}"),
    ]

    problems = validate_renpy.check_text_escapes(strings)

    assert len(problems) == 5, problems
    assert "Over-escaped text tag '{{color=#808090}'" in problems[0] and "write '{color=#808090}'" in problems[0]
    assert "Over-escaped text tag '{{/color}'" in problems[1] and "x.rpy:1" in problems[1]
    assert [problem.split(" at ")[1].split(" ")[0] for problem in problems[2:]] == ["x.rpy:1", "x.rpy:2", "x.rpy:3"]
    assert all("Unmatched '}'" in problem for problem in problems[2:])


def test_script_string_scan_skips_python_and_tracks_multiline_strings() -> None:
    sys.path.insert(0, str(ROOT / "tools"))
    import validate_renpy

    source = (
        "label start:\n"
        "    # a comment's apostrophe\n"
        '    e "one}}"\n'
        '    "two\n'
        "\n"
        'three"\n'
        '    $ x = "{{}}".format()\n'
        "init python:\n"
        '    y = "{0}}}".format(1)\n'
        "\n"
        "label after:\n"
        "    'four'\n"
    )

    assert list(validate_renpy.iter_script_strings(source)) == [(3, "one}}"), (4, "two\n\nthree"), (12, "four")]
