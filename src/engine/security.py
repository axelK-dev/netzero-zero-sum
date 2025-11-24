"""
Security module: Resource conflicts, migration, cyber threats.
"""

class Security:
    def __init__(self, conflict_risk=0.1, migration_pressure=0.05):
        self.conflict_risk = conflict_risk
        self.migration_pressure = migration_pressure

    def update(self, state, decisions):
        # Placeholder: spending on resilience reduces risk
        if "resilience_spend" in decisions:
            self.conflict_risk = max(0.0, self.conflict_risk - 0.002)

        # Climate-linked migration might rise if emissions are high (hook to climate later)
        # For now, mild drift
        self.migration_pressure = min(1.0, self.migration_pressure + 0.0005)

        state["security"] = {
            "conflict_risk": self.conflict_risk,
            "migration_pressure": self.migration_pressure
        }