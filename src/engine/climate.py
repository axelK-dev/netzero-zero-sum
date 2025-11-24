"""
Climate module: Emissions, temperature, tipping points.
"""

class Climate:
    def __init__(self, emissions_gt=40.0, temperature_c=1.1, tipping_threshold=2.0):
        self.emissions_gt = emissions_gt               # GtCO2e per year
        self.temperature_increase_celsius = temperature_c
        self.tipping_point_threshold = tipping_threshold

    def update(self, state, decisions):
        # Placeholder: if there is clean tech invest, reduce emissions a bit
        if "clean_tech_spend" in decisions:
            self.emissions_gt = max(0.0, self.emissions_gt - 0.2)

        # Very simple temperature drift based on emissions (placeholder)
        self.temperature_increase_celsius += 0.0005 * (self.emissions_gt - 30.0)

        # Tipping risk flag
        tipping_risk = self.temperature_increase_celsius >= self.tipping_point_threshold

        state["climate"] = {
            "emissions_gt": self.emissions_gt,
            "temperature_c": self.temperature_increase_celsius,
            "tipping_risk": tipping_risk
        }