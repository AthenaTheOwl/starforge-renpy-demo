## combat_narrator.rpy — Narrative combat engine
##
## Disco Elysium / Citizen Sleeper style: dice rolls with visible results,
## stat-gated options, "failure is interesting" philosophy.
## Replaces the turn-based grid combat from Godot.

init python:
    import json as _json
    import os as _os
    import random as _random

    class NarrativeCombat(object):
        """Tracks state for a narrative combat encounter."""

        def __init__(self, encounter_id):
            self.encounter_id = encounter_id
            self.encounter = {}
            self.enemies = []
            self.party_hp = {}
            self.party_max_hp = {}
            self.enemy_hp = {}
            self.enemy_max_hp = {}
            self.enemy_names = {}
            self.heat = {}
            self.cli = 0.0
            self.round_number = 0
            self.active_character = "avyanna"
            self.log = []
            self._load_encounter(encounter_id)

        def _load_encounter(self, encounter_id):
            """Load encounter and enemy data from JSON."""
            enc_path = _os.path.join(config.gamedir, "data", "encounters", encounter_id + ".json")
            if not _os.path.isfile(enc_path):
                return
            with open(enc_path, "r", encoding="utf-8") as f:
                self.encounter = _json.load(f)

            # Initialize party HP from party_manager
            if hasattr(store, 'party_manager'):
                for char_id in store.party_manager.active_party:
                    char = store.party_manager.get_character(char_id)
                    hp = char.get("hp_max", 100)
                    self.party_hp[char_id] = hp
                    self.party_max_hp[char_id] = hp
                    self.heat[char_id] = 0

            # Resolve enemies from waves
            enemy_idx = 0
            for wave in self.encounter.get("waves", []):
                for entry in wave.get("enemies", []):
                    enemy_type = entry.get("type", "")
                    count = entry.get("count", 1)
                    enemy_data = self._load_enemy(enemy_type)
                    if not enemy_data:
                        continue
                    for i in range(count):
                        key = "{}_{}".format(enemy_type, enemy_idx)
                        enemy_idx += 1
                        hp = enemy_data.get("hp_max", 40)
                        self.enemy_hp[key] = hp
                        self.enemy_max_hp[key] = hp
                        self.enemy_names[key] = enemy_data.get("name", enemy_type)
                        self.enemies.append({"key": key, "data": enemy_data})

        def _load_enemy(self, enemy_type):
            """Load enemy definition from JSON."""
            path = _os.path.join(config.gamedir, "data", "enemies", enemy_type + ".json")
            if not _os.path.isfile(path):
                return None
            with open(path, "r", encoding="utf-8") as f:
                return _json.load(f)

        def resolve_attack(self, attacker_id, ability_name, target_key):
            """Roll d20 + attack vs target armor. Returns dict with results."""
            attacker_stat = 0
            if hasattr(store, 'party_manager'):
                attacker_stat = store.party_manager.get_stat(attacker_id, "attack")

            target_armor = 0
            for e in self.enemies:
                if e["key"] == target_key:
                    target_armor = e["data"].get("armor", 0)
                    break

            die_roll = _random.randint(1, 20)
            total = die_roll + attacker_stat
            dc = 10 + target_armor

            if die_roll == 20:
                hit = True
                crit = True
            elif die_roll == 1:
                hit = False
                crit = False
            else:
                hit = total >= dc
                crit = False

            # Calculate damage
            base_damage = attacker_stat
            if hit:
                damage = max(1, base_damage - target_armor // 2)
                if crit:
                    damage *= 2
                self.enemy_hp[target_key] = max(0, self.enemy_hp[target_key] - damage)
            else:
                damage = 0

            # Heat management
            self.heat[attacker_id] = self.heat.get(attacker_id, 0) + 1

            result = {
                "hit": hit,
                "crit": crit,
                "die_roll": die_roll,
                "modifier": attacker_stat,
                "total": total,
                "dc": dc,
                "damage": damage,
                "attacker": attacker_id,
                "target": target_key,
                "target_name": self.enemy_names.get(target_key, target_key),
                "target_alive": self.enemy_hp[target_key] > 0,
            }

            # Store for dice screen display
            store.last_skill_check = {
                "stat": "attack",
                "threshold": dc,
                "die_roll": die_roll,
                "stat_value": attacker_stat,
                "total": total,
                "result": "CRITICAL_SUCCESS" if crit else ("SUCCESS" if hit else "FAILURE"),
                "character": attacker_id,
            }

            self.log.append(result)
            return result

        def enemy_threatens(self, enemy_key=None):
            """Pick a random living enemy to attack a random party member."""
            # Pick attacker
            living_enemies = [e for e in self.enemies if self.enemy_hp.get(e["key"], 0) > 0]
            if not living_enemies:
                return {"narrative": "", "damage": 0, "target": None, "target_name": ""}

            if enemy_key:
                attacker = next((e for e in living_enemies if e["key"] == enemy_key), living_enemies[0])
            else:
                attacker = _random.choice(living_enemies)

            # Pick target
            living_party = [cid for cid in self.party_hp if self.party_hp[cid] > 0]
            if not living_party:
                return {"narrative": "", "damage": 0, "target": None, "target_name": ""}

            target = _random.choice(living_party)
            target_armor = 0
            if hasattr(store, 'party_manager'):
                target_armor = store.party_manager.get_stat(target, "armor")

            # Enemy attack
            enemy_attack = attacker["data"].get("attack", 10)
            abilities = attacker["data"].get("abilities", [])
            ability = abilities[0] if abilities else {"name": "Attack", "base_damage": enemy_attack}
            base_damage = ability.get("base_damage", enemy_attack)

            damage = max(1, base_damage - target_armor)
            self.party_hp[target] = max(0, self.party_hp[target] - damage)

            enemy_name = self.enemy_names.get(attacker["key"], "Enemy")
            ability_name = ability.get("name", "Attack")

            return {
                "narrative": "{} uses {} against {}!".format(enemy_name, ability_name, target.title()),
                "damage": damage,
                "target": target,
                "target_name": target.title(),
                "enemy_name": enemy_name,
                "ability_name": ability_name,
            }

        def is_combat_over(self):
            """Check if combat has ended (victory or defeat)."""
            all_enemies_dead = all(hp <= 0 for hp in self.enemy_hp.values())
            all_party_dead = all(hp <= 0 for hp in self.party_hp.values())
            return all_enemies_dead or all_party_dead

        @property
        def victory(self):
            return all(hp <= 0 for hp in self.enemy_hp.values())

        @property
        def defeat(self):
            return all(hp <= 0 for hp in self.party_hp.values())

        def living_enemies_count(self):
            return sum(1 for hp in self.enemy_hp.values() if hp > 0)

        def get_living_enemy_keys(self):
            return [k for k, hp in self.enemy_hp.items() if hp > 0]

        def advance_round(self):
            """Advance to the next round. Decay heat and CLI."""
            self.round_number += 1
            for char_id in self.heat:
                self.heat[char_id] = max(0, self.heat[char_id] - 1)
            self.cli = max(0.0, self.cli - 0.5)

        def __eq__(self, other):
            if not isinstance(other, NarrativeCombat):
                return NotImplemented
            return self.__dict__ == other.__dict__
