import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".pytest_cache", "__pycache__", ".venv", "venv"}
# Absolute local paths (a drive letter or a home directory) other than the
# documented C:\path\to\... placeholder.
MACHINE_PATH = re.compile(r"\b[A-Za-z]:\\(?!path\\to\\)|(?:^|[\s(`'\"])/(?:home|Users)/\w")


def test_public_docs_have_no_machine_specific_paths() -> None:
    offenders: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if MACHINE_PATH.search(line):
                offenders.append(f"{path.relative_to(ROOT).as_posix()}:{line_no}: {line.strip()}")

    assert offenders == [], "use a placeholder such as C:\\path\\to\\renpy-8.5.2-sdk instead:\n" + "\n".join(offenders)
