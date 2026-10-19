import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
FLAG_WRITE = re.compile(r'set_flag\(\s*"([^"]+)"')
FLAG_READ = re.compile(r'(?:has_flag|get_flag)\(\s*"([^"]+)"')
REQUIRED_FLAGS = re.compile(r'"flags":\s*\[([^\]]*)\]')
# Read only in dialogue/ scenes that chapter_flow does not route. Neither this
# port nor the Godot port sets them, and no earlier choice clearly earns them,
# so their gated lines stay unreachable until the author decides where.
KNOWN_UNSET_FLAGS = {
    "ai_citizens_discovered",
    "elia_bonded",
    "elia_trust_high",
    "elia_trust_low",
    "elisira_conflict_resolved",
    "first_watch_ai_citizens",
    "first_watch_bubbles",
    "first_watch_cinnamon",
    "first_watch_waffle",
    "nyx_trust_high",
    "nyx_trust_low",
    "rho_trust_high",
    "rho_trust_low",
    "shard_whispers_heard",
    "vesper_trust_high",
    "vesper_trust_low",
}


def collect_flags() -> tuple[set[str], set[str]]:
    written: set[str] = set()
    read: set[str] = set()
    for path in sorted(GAME.rglob("*.rpy")):
        text = path.read_text(encoding="utf-8")
        written.update(FLAG_WRITE.findall(text))
        read.update(FLAG_READ.findall(text))
        for group in REQUIRED_FLAGS.findall(text):
            read.update(re.findall(r'"([^"]+)"', group))
    return written, read


def test_every_read_flag_has_a_setter() -> None:
    written, read = collect_flags()

    assert sorted(read - written - KNOWN_UNSET_FLAGS) == []


def test_known_unset_flags_are_still_read_and_unset() -> None:
    written, read = collect_flags()

    assert sorted(KNOWN_UNSET_FLAGS - (read - written)) == []


def test_bond_flags_use_the_same_name_for_setter_and_reader() -> None:
    written, read = collect_flags()

    assert sorted(flag for flag in written | read if flag.startswith("bonded_with_")) == []
    assert sorted(flag for flag in read if flag.endswith("_bonded") and flag not in written) == ["elia_bonded"]
