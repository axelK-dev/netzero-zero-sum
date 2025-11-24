"""
Culture module: Public opinion, activism, misinformation.
"""

class Culture:
    def __init__(self, opinion=0.6, misinformation=0.2):
        self.public_opinion_index = opinion
        self.misinformation_factor = misinformation

    def update(self, state, decisions):
        # Placeholder dynamics: opinion drifts up slowly if spending on education
        if "education_spend" in decisions:
            self.public_opinion_index = min(1.0, self.public_opinion_index + 0.01)

        # Misinformation reduces opinion very slightly
        self.public_opinion_index = max(0.0, self.public_opinion_index - 0.001 * self.misinformation_factor)

        state["culture"] = {
            "public_opinion_index": self.public_opinion_index,
            "misinformation_factor": self.misinformation_factor
        }