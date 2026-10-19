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
