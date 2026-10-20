import textwrap
from pathlib import Path
from types import SimpleNamespace


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"


def load_narrative_combat():
    """Run combat_narrator.rpy's init python block outside Ren'Py."""
    source = (GAME / "python" / "combat_narrator.rpy").read_text(encoding="utf-8")
    block = source.split("init python:\n", 1)[1]
    namespace = {
        "config": SimpleNamespace(gamedir=str(GAME)),
        "store": SimpleNamespace(),
    }
    exec(compile(textwrap.dedent(block), "combat_narrator.rpy", "exec"), namespace)
    return namespace["NarrativeCombat"], namespace


def test_attack_on_combat_without_encounter_data_does_not_crash() -> None:
    # act1_glitter_vein is routed (chapter 4) but has no encounter JSON, and
    # its script attacks "claim_jumper_1"; resolve_attack used to raise KeyError on it.
    assert not (GAME / "data" / "encounters" / "act1_glitter_vein.json").exists()
    NarrativeCombat, namespace = load_narrative_combat()

    for roll in (20, 10, 1):  # crit hit, ordinary hit (attack 0 vs DC 10), miss
        namespace["_random"] = SimpleNamespace(randint=lambda low, high, roll=roll: roll)
        combat = NarrativeCombat("act1_glitter_vein")

        result = combat.resolve_attack("avyanna", "strike", "claim_jumper_1")

        assert result["target_alive"] is False
        assert result["target_name"] == "claim_jumper_1"
        assert combat.enemy_hp == {}
