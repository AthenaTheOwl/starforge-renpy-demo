## relationship_manager.rpy — Character affinity and relationship tier system
##
## Direct port of RelationshipManager from autoload/relationship_manager.gd.
## Affinity 0-100 per character. Tier thresholds gate content.

init python:
    class RelationshipManager(object):
        """Tracks affinity levels for all characters. Tiers gate dialogue access."""

        TIER_THRESHOLDS = {
            "stranger": 0,
            "acquaintance": 10,
            "trusted": 25,
            "close": 45,
            "bonded": 70,
        }

        TIER_ORDER = ["stranger", "acquaintance", "trusted", "close", "bonded"]

        CHARACTERS = {
            # Human crew
            "elia": {"name": "Elia", "type": "crew", "starting_affinity": 15},
            "elisira": {"name": "Elisira", "type": "crew", "starting_affinity": 10},
            "vesper": {"name": "Vesper", "type": "crew", "starting_affinity": 5},
            "jalen": {"name": "Jalen", "type": "crew", "starting_affinity": 5},
            "nyx": {"name": "Nyx", "type": "crew", "starting_affinity": 5},
            "rho": {"name": "Rho", "type": "crew", "starting_affinity": 10},
            # AI citizens
            "waffle": {"name": "Waffle.bat", "type": "ai_citizen", "starting_affinity": 5},
            "bubbles": {"name": "Bubbles", "type": "ai_citizen", "starting_affinity": 5},
            "cinnamon": {"name": "Cinnamon", "type": "ai_citizen", "starting_affinity": 5},
            "souffle": {"name": "Souffle", "type": "ai_citizen", "starting_affinity": 0},
            # Entity
            "bee": {"name": "Bee", "type": "entity", "starting_affinity": 0},
        }

        def __init__(self):
            self.affinity = {}
            self._initialize_affinity()

        def _initialize_affinity(self):
            for char_id, data in self.CHARACTERS.items():
                self.affinity[char_id] = data["starting_affinity"]

        def change_affinity(self, character_id, amount):
            """Change affinity by amount. Clamps to 0-100."""
            char_id = character_id.lower()
            if char_id not in self.affinity:
                return
            old_val = self.affinity[char_id]
            self.affinity[char_id] = max(0, min(100, old_val + amount))
            new_val = self.affinity[char_id]
            # Check for tier change — record milestone in persistent
            old_tier = self._get_tier_for_value(old_val)
            new_tier = self._get_tier_for_value(new_val)
            if new_tier != old_tier:
                self._on_tier_change(char_id, old_tier, new_tier)

        def get_affinity(self, character_id):
            return self.affinity.get(character_id.lower(), 0)

        def get_tier(self, character_id):
            """Return tier name string for character's current affinity."""
            val = self.get_affinity(character_id)
            return self._get_tier_for_value(val)

        def get_tier_name(self, character_id):
            """Alias for get_tier — returns capitalized tier name."""
            return self.get_tier(character_id).capitalize()

        def _get_tier_for_value(self, value):
            if value >= self.TIER_THRESHOLDS["bonded"]:
                return "bonded"
            elif value >= self.TIER_THRESHOLDS["close"]:
                return "close"
            elif value >= self.TIER_THRESHOLDS["trusted"]:
                return "trusted"
            elif value >= self.TIER_THRESHOLDS["acquaintance"]:
                return "acquaintance"
            else:
                return "stranger"

        def is_at_least(self, character_id, min_tier_name):
            """Check if character's tier meets or exceeds the given tier."""
            current = self.TIER_ORDER.index(self.get_tier(character_id))
            required = self.TIER_ORDER.index(min_tier_name.lower())
            return current >= required

        def process_reputation_affinity(self, character_id, amount):
            """Bridge dialogue reputation changes to affinity.
            +1 rep -> +3 affinity (formula: amount * 2 + 1)"""
            affinity_gain = amount * 2 + 1
            self.change_affinity(character_id.lower(), affinity_gain)

        def _on_tier_change(self, character_id, old_tier, new_tier):
            """Handle tier change — set milestone flag, update persistent."""
            milestone = "{}_tier_{}".format(character_id, new_tier)
            if hasattr(store, 'game_state') and store.game_state:
                store.game_state.set_flag(milestone)
            # Track bonded characters in persistent
            if new_tier == "bonded":
                if persistent.characters_bonded is None:
                    persistent.characters_bonded = []
                if character_id not in persistent.characters_bonded:
                    persistent.characters_bonded.append(character_id)

        def __eq__(self, other):
            if not isinstance(other, RelationshipManager):
                return NotImplemented
            return self.affinity == other.affinity

default relationship_manager = RelationshipManager()
