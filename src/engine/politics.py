"""
Politics module: Policy adoption, treaties, lobbying.
"""

class Politics:
    def __init__(self, adoption_rate=0.1, cooperation=0.5):
        self.policy_adoption_rate = adoption_rate
        self.international_cooperation = cooperation
        self.policy_index = 0.0

    def update(self, state, decisions):
        # Placeholder: increase policy index a bit each year
        self.policy_index += self.policy_adoption_rate * self.international_cooperation

        # Example decision hook
        if "diplomacy_spend" in decisions:
            self.international_cooperation = min(1.0, self.international_cooperation + 0.01)

        state["politics"] = {
            "policy_index": self.policy_index,
            "international_cooperation": self.international_cooperation
        }