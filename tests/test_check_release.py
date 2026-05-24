from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import check_release


def test_renpy_lint_diagnostic_detection_ignores_clean_output() -> None:
    assert check_release.has_renpy_lint_diagnostics("Lint complete, no problems found.") is False
    assert check_release.has_renpy_lint_diagnostics("game/foo.rpy:10 Text tag 'BEE' is not known.") is True


def test_renpy_lint_summary_counts_diagnostics() -> None:
    output = "\n".join(
        [
            "Ren'Py lint report",
            "game/foo.rpy:10 Text tag 'BEE' is not known.",
            "game/bar.rpy:20 Close text tag '{/i}' does not match an open text tag.",
            "game/python/skill_check.rpy:73 default persistent.x already defined at game/python/replay_system.rpy:11",
        ]
    )

    summary = check_release.summarize_renpy_lint_output(output)

    assert "Ren'Py lint emitted 3 diagnostic line(s)." in summary
    assert "unknown_text_tags: 1" in summary
    assert "tag_mismatches: 1" in summary
    assert "duplicate_defaults: 1" in summary
