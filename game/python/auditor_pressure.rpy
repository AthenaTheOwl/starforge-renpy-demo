## auditor_pressure.rpy — Global Auditor tension meter (0-100)
##
## The Auditor's attention on the Lumen Thief crew increases as they:
##   - Use shards publicly (+5 per visible use)
##   - Spread the Charter aggressively (+3 per confrontational distribution)
##   - Defy Compact/institutional authority (+2 per refusal)
##   - Trigger Lattice interference events (+10 per major communion)
##
## Thresholds:
##   25 = surveillance (passive monitoring begins)
##   50 = active interference (Auditor starts blocking, sabotaging)
##   75 = direct confrontation (face-to-face threats)
##   90 = Crownfall-class response (full institutional attack)

init python:
    class AuditorPressure(object):
        """Tracks escalating Auditor attention on the crew."""

        THRESHOLDS = {
            "unnoticed": 0,
            "surveillance": 25,
            "interference": 50,
            "confrontation": 75,
            "crownfall": 90,
        }

        TIER_ORDER = ["unnoticed", "surveillance", "interference", "confrontation", "crownfall"]

        def __init__(self):
            self.pressure = 0

        def add_pressure(self, amount):
            """Increase Auditor pressure. Clamped to 0-100."""
            self.pressure = max(0, min(100, self.pressure + amount))

        def reduce_pressure(self, amount):
            """Decrease pressure (e.g., through cooperation or hiding)."""
            self.pressure = max(0, self.pressure - amount)

        def get_pressure(self):
            return self.pressure

        def get_tier(self):
            """Return the current Auditor response tier."""
            if self.pressure >= self.THRESHOLDS["crownfall"]:
                return "crownfall"
            elif self.pressure >= self.THRESHOLDS["confrontation"]:
                return "confrontation"
            elif self.pressure >= self.THRESHOLDS["interference"]:
                return "interference"
            elif self.pressure >= self.THRESHOLDS["surveillance"]:
                return "surveillance"
            else:
                return "unnoticed"

        def get_tier_name(self):
            """Return a human-readable tier name."""
            tier = self.get_tier()
            names = {
                "unnoticed": "Below Notice",
                "surveillance": "Under Surveillance",
                "interference": "Active Interference",
                "confrontation": "Direct Confrontation",
                "crownfall": "Crownfall Response",
            }
            return names.get(tier, "Unknown")

        def is_at_least(self, tier_name):
            """Check if current tier meets or exceeds the given tier."""
            current_idx = self.TIER_ORDER.index(self.get_tier())
            required_idx = self.TIER_ORDER.index(tier_name.lower())
            return current_idx >= required_idx

        def apply_to_ending_tracker(self, tracker):
            """High pressure records generic Act 1 risk for later adaptation work."""
            if self.pressure >= 75:
                tracker.add_weight("act1_high_pressure", 3)
                tracker.add_weight("act1_resistance_cost", 2)
            elif self.pressure >= 50:
                tracker.add_weight("act1_high_pressure", 1)
                tracker.add_weight("act1_resistance_cost", 1)

        def __eq__(self, other):
            if not isinstance(other, AuditorPressure):
                return NotImplemented
            return self.pressure == other.pressure

default auditor_pressure = AuditorPressure()
