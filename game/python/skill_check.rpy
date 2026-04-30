## skill_check.rpy — D20 skill check system
##
## Port of DialogueManager._resolve_skill_check from Godot.
## D&D-style: roll d20 + stat modifier vs DC threshold.
## Nat 20 = critical success, Nat 1 = critical failure.

init python:
    import random as _random

    class SkillCheckSystem(object):
        """Resolves D20 skill checks with stat modifiers."""

        RESULT_CRITICAL_SUCCESS = "CRITICAL_SUCCESS"
        RESULT_SUCCESS = "SUCCESS"
        RESULT_FAILURE = "FAILURE"
        RESULT_CRITICAL_FAILURE = "CRITICAL_FAILURE"

        def roll(self, stat_name, threshold, character_id="avyanna"):
            """Roll d20 + stat_value vs threshold. Returns result string."""
            stat_value = 0
            if hasattr(store, 'party_manager') and store.party_manager:
                stat_value = store.party_manager.get_stat(character_id, stat_name)

            die_roll = _random.randint(1, 20)
            total = die_roll + stat_value

            if die_roll == 20:
                result = self.RESULT_CRITICAL_SUCCESS
            elif die_roll == 1:
                result = self.RESULT_CRITICAL_FAILURE
            elif total >= threshold:
                result = self.RESULT_SUCCESS
            else:
                result = self.RESULT_FAILURE

            # Store for UI display (dice_roll_screen reads this)
            store.last_skill_check = {
                "stat": stat_name,
                "threshold": threshold,
                "die_roll": die_roll,
                "stat_value": stat_value,
                "total": total,
                "result": result,
                "character": character_id,
            }

            # Track in persistent stats
            if persistent.skill_checks_attempted is None:
                persistent.skill_checks_attempted = 0
            persistent.skill_checks_attempted += 1
            if result in (self.RESULT_SUCCESS, self.RESULT_CRITICAL_SUCCESS):
                if persistent.skill_checks_succeeded is None:
                    persistent.skill_checks_succeeded = 0
                persistent.skill_checks_succeeded += 1

            return result

    def skill_check(stat, threshold, character="avyanna"):
        """Convenience function for use in Ren'Py script.
        Rolls dice, shows the dice screen briefly, returns result string."""
        result = store.skill_system.roll(stat, threshold, character)
        renpy.show_screen("dice_roll_screen", _transient=True)
        renpy.pause(2.0)
        renpy.hide_screen("dice_roll_screen")
        return result

    def skill_check_silent(stat, threshold, character="avyanna"):
        """Roll without showing the dice screen (for passive checks)."""
        return store.skill_system.roll(stat, threshold, character)

default skill_system = SkillCheckSystem()
default last_skill_check = {}
default persistent.skill_checks_attempted = 0
default persistent.skill_checks_succeeded = 0
