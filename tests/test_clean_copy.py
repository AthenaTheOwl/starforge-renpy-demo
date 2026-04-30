from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_public_act1_renpy_source_present() -> None:
    rpy_files = sorted((ROOT / "game").rglob("*.rpy"))

    assert (ROOT / "game" / "script.rpy").exists()
    assert (ROOT / "game" / "screens.rpy").exists()
    assert (ROOT / "game" / "prose_scenes" / "act1").exists()
    assert len(rpy_files) >= 80


def test_unreleased_act_source_is_not_present() -> None:
    offenders = [
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "game").rglob("*")
        if path.is_file() and path.name.lower().startswith(("act2_", "act3_"))
    ]
    offenders.extend(
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "game" / "prose_scenes").glob("act*")
        if path.is_dir() and path.name != "act1"
    )

    assert offenders == []


def test_unreleased_act_tokens_are_not_present_in_game_source() -> None:
    forbidden_tokens = [
        "act2_",
        "act3_",
        "acts 1-3",
        "61 chapters",
        "full cleaned",
        "full source",
        "full corpus",
        "burn_the_ledger",
        "rim_liberation",
        "cult_awakening",
        "corporate_monetization",
        "compact_containment",
        "guild_coup",
    ]
    offenders: list[str] = []
    for path in (ROOT / "game").rglob("*"):
        if not path.is_file() or path.suffix not in {".rpy", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        if any(token in text for token in forbidden_tokens):
            offenders.append(path.relative_to(ROOT).as_posix())

    assert offenders == []


def test_no_runtime_junk() -> None:
    forbidden_suffixes = {".rpyc", ".rpyb", ".save", ".pyc"}
    forbidden_names = {
        "cache",
        "saves",
        "errors.txt",
        "traceback.txt",
        "log.txt",
        "renpy-8.5.2-sdk",
    }

    offenders: list[str] = []
    for path in ROOT.rglob("*"):
        if "__pycache__" in path.parts or ".pytest_cache" in path.parts:
            continue
        if any(part in forbidden_names for part in path.parts):
            offenders.append(str(path.relative_to(ROOT)))
        if path.is_file() and (path.suffix in forbidden_suffixes or path.name in forbidden_names):
            offenders.append(str(path.relative_to(ROOT)))

    assert offenders == []
