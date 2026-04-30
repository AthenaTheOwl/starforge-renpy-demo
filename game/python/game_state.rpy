## game_state.rpy — Central game state: flags, reputation, chapter tracking
##
## Port of GameManager + StoryManager from Godot autoloads.

init python:
    class GameState(object):
        """Tracks story flags, faction reputation, chapter progress, and dialogue/encounter completion."""

        def __init__(self):
            self.story_flags = {}
            self.current_chapter = 0
            self.played_dialogues = []
            self.cleared_encounters = []
            self.active_objectives = {}
            self.completed_objectives = []

        def set_flag(self, name, value=True):
            self.story_flags[name] = value

        def has_flag(self, name):
            return self.story_flags.get(name, False)

        def get_flag(self, name, default=None):
            return self.story_flags.get(name, default)

        def clear_flag(self, name):
            self.story_flags.pop(name, None)

        def mark_dialogue_played(self, dialogue_id):
            if dialogue_id not in self.played_dialogues:
                self.played_dialogues.append(dialogue_id)

        def has_played_dialogue(self, dialogue_id):
            return dialogue_id in self.played_dialogues

        def mark_encounter_cleared(self, encounter_id):
            if encounter_id not in self.cleared_encounters:
                self.cleared_encounters.append(encounter_id)

        def is_encounter_cleared(self, encounter_id):
            return encounter_id in self.cleared_encounters

        def set_objective(self, objective_id, description):
            self.active_objectives[objective_id] = description

        def complete_objective(self, objective_id):
            self.active_objectives.pop(objective_id, None)
            if objective_id not in self.completed_objectives:
                self.completed_objectives.append(objective_id)

        def __eq__(self, other):
            if not isinstance(other, GameState):
                return NotImplemented
            return self.__dict__ == other.__dict__

default game_state = GameState()
