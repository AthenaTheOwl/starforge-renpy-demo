## ending_tracker.rpy - Act 1 demo-safe choice tracking
##
## The private workshop has broader ending design. This public copy keeps only
## generic choice-weight plumbing so the Act 1 demo can run without exposing
## unreleased routes.

init python:
    class EndingTracker(object):
        """Minimal Act 1-safe tracker for future branching work."""

        def __init__(self):
            self.weights = {}

        def add_weight(self, choice_id, amount):
            self.weights[choice_id] = self.weights.get(choice_id, 0) + amount

        def add_weights(self, weight_dict):
            for choice_id, amount in weight_dict.items():
                self.add_weight(choice_id, amount)

        def get_dominant_ending(self):
            return "act1_complete"

        def __eq__(self, other):
            if not isinstance(other, EndingTracker):
                return NotImplemented
            return self.weights == other.weights

    class FactionReputation(object):
        """Act 1-safe reputation ledger."""

        FACTIONS = ["guild", "rim", "compact"]

        def __init__(self):
            self.reputation = {faction: 0 for faction in self.FACTIONS}

        def change_reputation(self, faction, amount):
            if faction in self.reputation:
                self.reputation[faction] = max(-100, min(100, self.reputation[faction] + amount))

        def get_reputation(self, faction):
            return self.reputation.get(faction, 0)

        def get_faction_tier(self, faction):
            rep = self.get_reputation(faction)
            if rep >= 50:
                return "allied"
            if rep >= 20:
                return "friendly"
            if rep >= -10:
                return "neutral"
            if rep >= -40:
                return "distrusted"
            return "hostile"

        def apply_to_ending_tracker(self, tracker):
            return None

        def __eq__(self, other):
            if not isinstance(other, FactionReputation):
                return NotImplemented
            return self.reputation == other.reputation

default ending_tracker = EndingTracker()
default faction_reputation = FactionReputation()
