"""
Entry point for Net Zero – Zero Sum simulation.
Initializes configs, loads modules, and runs the simulation loop.
"""

import json
from pathlib import Path

from engine.economy import Economy
from engine.politics import Politics
from engine.culture import Culture
from engine.security import Security
from engine.climate import Climate
from engine.feedback_loops import FeedbackLoops


def load_settings():
    """Load game settings from config/settings.json."""
    settings_path = Path(__file__).resolve().parents[1] / "config" / "settings.json"
    with open(settings_path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    # Load settings
    settings = load_settings()
    years = settings["game"]["time_horizon_years"]
    budget = settings["game"]["starting_budget"]

    # Initialize global state
    state = {}

    # Initialize modules with config values
    economy = Economy(
        initial_gdp=settings["economy"]["initial_gdp"],
        carbon_price=settings["economy"]["carbon_price"],
        growth_rate=settings["economy"]["growth_rate"]
    )
    politics = Politics(
        adoption_rate=settings["politics"]["policy_adoption_rate"],
        cooperation=settings["politics"]["international_cooperation"]
    )
    culture = Culture(
        opinion=settings["culture"]["public_opinion_index"],
        misinformation=settings["culture"]["misinformation_factor"]
    )
    security = Security(
        conflict_risk=settings["security"]["conflict_risk"],
        migration_pressure=settings["security"]["migration_pressure"]
    )
    climate = Climate(
        emissions_gt=settings["climate"]["initial_emissions_gt"],
        temperature_c=settings["climate"]["temperature_increase_celsius"],
        tipping_threshold=settings["climate"]["tipping_point_threshold"]
    )
    feedback = FeedbackLoops()

    # Simulation loop
    for year in range(years):
        print(f"\n--- Year {year + 1} ---")
        print(f"Budget remaining: ${budget:,.0f}")

        # Placeholder for player decisions (empty for now)
        decisions = {}

        # Update modules
        economy.update(state, decisions)
        politics.update(state, decisions)
        culture.update(state, decisions)
        security.update(state, decisions)
        climate.update(state, decisions)
        feedback.apply(state)

        # Print current state snapshot
        for domain, metrics in state.items():
            print(f"{domain.capitalize()}: {metrics}")

    print("\nSimulation complete.")


if __name__ == "__main__":
    main()