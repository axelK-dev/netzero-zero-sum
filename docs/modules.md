# Modules Overview

The simulation engine is divided into modular components, each responsible for a specific domain of the game. This modular design ensures scalability, maintainability, and clarity.

---

## 1. economy.py
**Purpose:**  
Simulates economic dynamics, including GDP growth, carbon pricing, subsidies, and trade.

**Responsibilities:**
- Initialize economic state variables (GDP, inflation, carbon tax).
- Apply player interventions (e.g., subsidies for renewables).
- Model trade-offs between growth and emissions reduction.

**Core Functions:**
- `init_economy_state(config)` – Initialize economic variables from config.
- `update_economy(state, decisions)` – Update GDP, carbon pricing, and trade based on decisions and feedback.
- `calculate_economic_score(state)` – Return economic stability and growth metrics.

---

## 2. politics.py
**Purpose:**  
Handles policy adoption, international treaties, and lobbying effects.

**Responsibilities:**
- Track policy implementation and resistance.
- Model international cooperation and treaty compliance.
- Simulate lobbying and political influence.

**Core Functions:**
- `init_politics_state(config)` – Initialize political variables (policy index, cooperation level).
- `update_politics(state, decisions)` – Update political landscape based on player actions and external events.
- `calculate_political_score(state)` – Return governance and policy effectiveness metrics.

---

## 3. culture.py
**Purpose:**  
Represents public opinion, activism, and misinformation dynamics.

**Responsibilities:**
- Track societal attitudes toward climate action.
- Model activism and grassroots movements.
- Simulate misinformation campaigns and their impact.

**Core Functions:**
- `init_culture_state(config)` – Initialize cultural variables (public opinion index).
- `update_culture(state, decisions)` – Update cultural dynamics based on interventions and random events.
- `calculate_cultural_score(state)` – Return social stability and awareness metrics.

---

## 4. security.py
**Purpose:**  
Simulates resource conflicts, migration pressures, and cyber threats.

**Responsibilities:**
- Model geopolitical tensions over resources.
- Track migration flows due to climate impacts.
- Simulate cyber threats affecting infrastructure.

**Core Functions:**
- `init_security_state(config)` – Initialize security variables (conflict risk, migration index).
- `update_security(state, decisions)` – Update security dynamics based on interventions and shocks.
- `calculate_security_score(state)` – Return global stability and risk metrics.

---

## 5. climate.py
**Purpose:**  
Calculates emissions, temperature rise, and tipping points.

**Responsibilities:**
- Track greenhouse gas emissions.
- Model temperature changes and feedback loops.
- Detect tipping points (ice melt, ecosystem collapse).

**Core Functions:**
- `init_climate_state(config)` – Initialize climate variables (emissions, temperature).
- `update_climate(state, decisions)` – Update climate metrics based on interventions and external factors.
- `calculate_climate_score(state)` – Return climate stability and risk metrics.

---

## 6. feedback_loops.py
**Purpose:**  
Applies systemic effects and oscillations across modules.

**Responsibilities:**
- Introduce unintended consequences (e.g., economic slowdown due to aggressive climate policy).
- Model oscillations and cascading failures.
- Ensure inter-module dependencies are respected.

**Core Functions:**
- `apply_feedback_loops(state)` – Apply systemic feedback effects across all domains.

---

## Shared Utilities
- **helpers.py** – Logging, random event generation, probability distributions.
- **data ingestion** – Functions to load OSINT and real-world data from `data_sources.json`.

