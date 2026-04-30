## party_manager.rpy — Party roster and character stat management
##
## Loads character data from JSON files. Tracks active party, stats, XP.

init python:
    import json as _json
    import os as _os

    class PartyManager(object):
        """Manages the party roster, character stats, and leveling."""

        MAX_ACTIVE_PARTY = 4

        # Stat names that can be used in skill checks
        SKILL_STATS = [
            "attack", "speed", "armor", "shields", "wards",
            "insight", "empathy", "tactics", "wits", "persuasion",
            "lattice", "stealth", "tech", "intimidation",
        ]

        def __init__(self):
            self.characters = {}
            self.active_party = []
            self.xp = {}
            self._load_characters()

        def _load_characters(self):
            """Load character definitions from JSON data files."""
            data_dir = _os.path.join(config.gamedir, "data", "characters")
            if not _os.path.isdir(data_dir):
                return
            for filename in _os.listdir(data_dir):
                if not filename.endswith(".json"):
                    continue
                filepath = _os.path.join(data_dir, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        char_data = _json.load(f)
                    char_id = char_data.get("id", filename.replace(".json", ""))
                    self.characters[char_id] = char_data
                    self.xp[char_id] = 0
                except Exception:
                    pass

            # Default active party — full crew for Act 1
            crew_ids = ["avyanna", "elia", "vesper", "elisira", "nyx", "rho", "jalen"]
            self.active_party = [cid for cid in crew_ids if cid in self.characters]

        def get_character(self, character_id):
            """Return character data dict, or empty dict."""
            return self.characters.get(character_id.lower(), {})

        def get_stat(self, character_id, stat_name):
            """Return a stat value for skill checks. Maps skill names to base stats."""
            char = self.get_character(character_id)
            if not char:
                return 0

            # Direct stat match
            if stat_name in char:
                return char[stat_name]

            # Skill-to-stat mapping for dialogue skill checks
            skill_map = {
                "insight": "speed",
                "empathy": "wards",
                "tactics": "attack",
                "wits": "speed",
                "persuasion": "shields",
                "lattice": "wards",
                "stealth": "speed",
                "tech": "shields",
                "intimidation": "attack",
            }
            mapped_stat = skill_map.get(stat_name.lower())
            if mapped_stat and mapped_stat in char:
                return char[mapped_stat]

            return 0

        def is_in_party(self, character_id):
            return character_id.lower() in self.active_party

        def add_to_party(self, character_id):
            char_id = character_id.lower()
            if char_id not in self.active_party and char_id in self.characters:
                if len(self.active_party) < self.MAX_ACTIVE_PARTY:
                    self.active_party.append(char_id)

        def remove_from_party(self, character_id):
            char_id = character_id.lower()
            if char_id in self.active_party:
                self.active_party.remove(char_id)

        def award_xp(self, amount):
            """Award XP to all active party members."""
            for char_id in self.active_party:
                self.xp[char_id] = self.xp.get(char_id, 0) + amount

        def get_xp(self, character_id):
            return self.xp.get(character_id.lower(), 0)

        def __eq__(self, other):
            if not isinstance(other, PartyManager):
                return NotImplemented
            return (self.characters == other.characters and
                    self.active_party == other.active_party and
                    self.xp == other.xp)

default party_manager = PartyManager()
