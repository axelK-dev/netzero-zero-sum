"""
Economy module: Handles GDP, carbon pricing, subsidies, trade.
"""

class Economy:
    def __init__(self, initial_gdp=100_000_000_000_000, carbon_price=50, growth_rate=0.02):
        # You can later pass these from settings.json
        self.gdp = initial_gdp           # Example: $100T global GDP
        self.carbon_price = carbon_price # $/ton CO2
        self.growth_rate = growth_rate   # Annual GDP growth

    def update(self, state, decisions):
        """
        Update economy each turn.
        - decisions: dict of player choices, e.g., {"subsidies": 100e9, "carbon_tax": 60}
        - state: global state dict where we store the economy snapshot
        """
        # Apply simple growth (placeholder). Later, incorporate decisions and feedback loops.
        self.gdp *= (1 + self.growth_rate)

        # Optional: adjust carbon price if decision present
        if "carbon_tax" in decisions:
            self.carbon_price = decisions["carbon_tax"]

        # Write current economy snapshot into global state
        state["economy"] = {
            "gdp": self.gdp,
            "carbon_price": self.carbon_price
        }