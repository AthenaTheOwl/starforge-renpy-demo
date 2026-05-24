#!/usr/bin/env python3
"""Deterministic playtest audit for the public Ren'Py demo."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
QUEUE_MARKERS = re.compile(r"\b(TODO|FIXME|DEAD[- ]?LETTER|PLAYTEST[- ]?QUEUE|BALANCE[- ]?QUEUE)\b|\bBUG:", re.IGNORECASE)
LABEL_RE = re.compile(r"^\s*label\s+([A-Za-z0-9_.]+)\s*(?:\(.*?\))?:", re.MULTILINE)


def load_json_dir(path: Path) -> dict[str, dict]:
    return {item.stem: json.loads(item.read_text(encoding="utf-8")) for item in sorted(path.glob("*.json"))}


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    rpy_files = sorted(GAME.rglob("*.rpy"))
    labels: set[str] = set()
    marker_hits = []
    menus = 0

    for path in rpy_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        labels.update(LABEL_RE.findall(text))
        menus += len(re.findall(r"^\s*menu\s*:", text, re.MULTILINE))
        for line_no, line in enumerate(text.splitlines(), start=1):
            if QUEUE_MARKERS.search(line):
                marker_hits.append(f"{path.relative_to(ROOT).as_posix()}:{line_no}: {line.strip()}")

    chapter_flow = (GAME / "chapters" / "chapter_flow.rpy").read_text(encoding="utf-8")
    routed_ids = sorted(set(re.findall(r'"(act1_[A-Za-z0-9_]+)"', chapter_flow)))
    routed_story = []
    routed_combat = []
    for route_id in routed_ids:
        if route_id in labels:
            routed_story.append(route_id)
        elif f"combat_{route_id}" in labels:
            routed_combat.append(route_id)
        else:
            errors.append(f"chapter flow route has no story/combat label: {route_id}")

    enemies = load_json_dir(GAME / "data" / "enemies")
    encounters = load_json_dir(GAME / "data" / "encounters")
    threat_scores = []
    for encounter_id, encounter in encounters.items():
        total_hp = 0
        total_attack = 0
        for wave in encounter.get("waves", []):
            for entry in wave.get("enemies", []):
                enemy_id = entry.get("type")
                count = int(entry.get("count", 1))
                if enemy_id not in enemies:
                    errors.append(f"encounter {encounter_id}: missing enemy {enemy_id}")
                    continue
                enemy = enemies[enemy_id]
                total_hp += int(enemy.get("hp_max", 0)) * count
                total_attack += int(enemy.get("attack", 0)) * count
        threat_scores.append((encounter_id, total_hp, total_attack))
        if total_hp <= 0 or total_attack <= 0:
            errors.append(f"encounter {encounter_id}: threat score is zero")

    warnings.extend(marker_hits)

    print("Ren'Py playtest audit")
    print(f"- labels: {len(labels)}")
    print(f"- routed story scenes: {len(routed_story)}")
    print(f"- routed combat scenes: {len(routed_combat)}")
    print(f"- menus: {menus}")
    print(f"- encounters: {len(encounters)}")
    print(f"- dead-letter marker hits: {len(marker_hits)}")
    if threat_scores:
        min_threat = min(threat_scores, key=lambda item: item[1] + item[2])
        max_threat = max(threat_scores, key=lambda item: item[1] + item[2])
        print(f"- lowest encounter threat: {min_threat[0]} hp={min_threat[1]} atk={min_threat[2]}")
        print(f"- highest encounter threat: {max_threat[0]} hp={max_threat[1]} atk={max_threat[2]}")

    if warnings:
        print("\nDead-letter / balance queue:")
        for warning in warnings[:50]:
            print(f"- {warning}")
        if len(warnings) > 50:
            print(f"- ... {len(warnings) - 50} more queue item(s)")

    if errors:
        print("\nplaytest audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("playtest audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

