Architecture Overview
Purpose
The architecture of Net Zero – Zero Sum is designed to be modular, scalable, and data-driven, enabling the simulation of complex global systems across multiple domains: economy, politics, culture, security, and climate. Each module operates independently but interacts through a central simulation engine that manages state updates and feedback loops.

High-Level Components


```mermaid
flowchart TD
    A[main.py<br/>Entry Point] --> B[Simulation Engine<br/>(src/engine)]
    A --> C[Data Layer<br/>(config/, data/)]
    B --> D[UI Layer<br/>(src/ui)]
    B <--> C

    subgraph Engine Modules
        E[economy.py]
        F[politics.py]
        G[culture.py]
        H[security.py]
        I[climate.py]
        J[feedback_loops.py]


Module Responsibilities
1. main.py

Loads configuration files (settings.json, data_sources.json).
Initializes simulation engine and UI.
Starts the simulation loop:
while game_active:
    collect_player_decisions()
    update_state()
    render_dashboard()




2. Engine Modules (src/engine/)
Each module represents a domain and exposes functions to:

Initialize state variables (e.g., GDP, emissions, public opinion).
Update state based on player actions and external events.
Return metrics for scoring and visualization.

Modules:

economy.py: Models GDP, carbon pricing, subsidies, trade.
politics.py: Handles policy adoption, treaties, lobbying.
culture.py: Tracks public opinion, activism, misinformation.
security.py: Simulates resource conflicts, migration, cyber threats.
climate.py: Calculates emissions, temperature rise, tipping points.
feedback_loops.py: Applies systemic effects (oscillations, unintended consequences).

Interaction Pattern:
economy.update(state)
politics.update(state)
culture.update(state)
security.update(state)
climate.update(state)
feedback_loops.apply(state)


3. Data Layer

config/: Stores game rules and data source endpoints.
data/:

raw/: Unprocessed datasets (CSV, JSON).
processed/: Cleaned and normalized data for simulation.



Responsibilities:

Abstract data ingestion (local files → APIs → OSINT).
Provide consistent data structures to engine modules.


4. UI Layer (src/ui/)

dashboard.py: Main interface for player interaction.
charts.py: Visualization of metrics (emissions, GDP, stability).
Future: Web-based UI with real-time updates.


5. Utilities (src/utils/)

Logging, error handling.
Data cleaning and transformation.
Helper functions for probability distributions and random events.


Simulation Loop

Initialize state from configs and data.
Player allocates resources (e.g., $1T across interventions).
Engine updates state:

Apply player decisions.
Apply external events (news, random shocks).
Apply feedback loops.


Render UI with updated metrics.
Repeat until end condition (time horizon or stability threshold).


Scalability Considerations

Modular design allows adding new domains easily.
Config-driven rules enable scenario customization.
Data abstraction supports local or cloud-based ingestion.
UI decoupling allows CLI → dashboard → multiplayer web.


Future Extensions

Multiplayer mode with negotiation mechanics.
AI-driven advisors for policy suggestions.
Integration with live OSINT feeds for dynamic realism.