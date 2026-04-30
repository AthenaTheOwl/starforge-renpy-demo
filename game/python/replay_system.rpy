## replay_system.rpy — Cross-playthrough persistent data and NG+ unlocks
##
## Uses Ren'Py's persistent.* for data that survives across saves and new games.

## Persistent variables — survive across all saves and playthroughs
default persistent.playthrough_count = 0
default persistent.endings_seen = []
default persistent.memories = {}
default persistent.characters_bonded = []
default persistent.highest_chapter_reached = 0
default persistent.skill_checks_attempted = 0
default persistent.skill_checks_succeeded = 0
default persistent.combat_victories = 0
default persistent.combat_defeats = 0

init python:

    ## Memory catalog — defines all recordable story moments
    MEMORY_CATALOG = {
        "elia_rescue": {"title": "Cinder Hours", "text": "You pulled Elia from the burning mine. She's never forgotten."},
        "souffle_becoming": {"title": "The Becoming", "text": "Souffle opened their eyes for the first time. A new consciousness, fragile and wondering."},
        "the_heist": {"title": "The Heist", "text": "The crew moved as one. Whatever came next, you faced it together."},
        "bee_awakens": {"title": "Bee Awakens", "text": "The shard spoke. Not in words — in warmth, in recognition. You were not alone."},
        "act1_complete": {"title": "Act 1 Complete", "text": "The first act ends. But the story is far from over."},
    }

    def is_ng_plus():
        """Check if current game is a New Game+ run."""
        return persistent.playthrough_count is not None and persistent.playthrough_count > 0

    def get_ng_plus_level():
        """Return how many times the game has been completed."""
        return persistent.playthrough_count or 0

    def record_ending(ending_id):
        """Record that an ending has been seen."""
        if persistent.endings_seen is None:
            persistent.endings_seen = []
        if ending_id not in persistent.endings_seen:
            persistent.endings_seen.append(ending_id)

    def has_seen_ending(ending_id):
        """Check if a specific ending has been seen."""
        return persistent.endings_seen is not None and ending_id in persistent.endings_seen

    def record_memory(memory_id, text=None):
        """Record a key moment for the memories gallery.

        If text is None, looks up the memory in MEMORY_CATALOG.
        Stores {"title": ..., "text": ...} in persistent.memories.
        """
        if persistent.memories is None:
            persistent.memories = {}
        if text is not None:
            # Legacy/direct call — store as dict with text only
            persistent.memories[memory_id] = {"title": memory_id.replace("_", " ").title(), "text": text}
        elif memory_id in MEMORY_CATALOG:
            persistent.memories[memory_id] = dict(MEMORY_CATALOG[memory_id])

    def get_memories():
        """Return all recorded memories."""
        return persistent.memories or {}

    def complete_playthrough(ending_id="act1_complete"):
        """Finalize a playthrough: increment count, record ending, snapshot bonds.

        Called at the end of an act/game to persist cross-playthrough data.
        Returns None.
        """
        # Increment playthrough count
        persistent.playthrough_count = (persistent.playthrough_count or 0) + 1

        # Record the ending
        record_ending(ending_id)

        # Record completion memory
        record_memory(ending_id)

        # Snapshot bonded characters from relationship_manager
        if hasattr(store, 'relationship_manager') and store.relationship_manager:
            bonded = []
            for char_id in store.relationship_manager.affinity:
                if store.relationship_manager.is_at_least(char_id, "trusted"):
                    bonded.append(char_id)
            if bonded:
                if persistent.characters_bonded is None:
                    persistent.characters_bonded = []
                for char_id in bonded:
                    if char_id not in persistent.characters_bonded:
                        persistent.characters_bonded.append(char_id)

        return None

    def update_highest_chapter(chapter_num):
        """Track the highest chapter reached across all playthroughs."""
        if persistent.highest_chapter_reached is None or chapter_num > persistent.highest_chapter_reached:
            persistent.highest_chapter_reached = chapter_num

    def apply_ng_plus_unlocks():
        """Apply NG+ bonuses at game start. Called from script.rpy."""
        if not is_ng_plus():
            return

        # Starting affinity bonuses for previously bonded characters
        if persistent.characters_bonded and hasattr(store, 'relationship_manager'):
            for char_id in persistent.characters_bonded:
                store.relationship_manager.change_affinity(char_id, 5)

        # Set NG+ flag for dialogue gating
        if hasattr(store, 'game_state') and store.game_state:
            store.game_state.set_flag("ng_plus")
            store.game_state.set_flag("ng_plus_level", get_ng_plus_level())

            # Unlock extra content based on endings seen
            if has_seen_ending("act1_complete"):
                store.game_state.set_flag("ng_plus_act1_aware")
