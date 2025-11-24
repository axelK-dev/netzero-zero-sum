
# API Documentation – Net Zero Zero Sum

## Overview
This API allows interaction with the Net Zero Zero Sum simulation engine, enabling data retrieval, scenario execution, and visualization integration.

---

## Base URL

http://localhost:8000/api/v1
*(Update if deployed to cloud)*

---

## Authentication
- **Method:** API Key or OAuth (future)
- **Header Example:**

Authorization: Bearer <API_KEY>

---

## Endpoints

### 1. **Run Simulation**

POST /simulation/run
**Description:** Executes a simulation with given parameters.

**Request Body:**
```json
{
  "budget": 1000000000000,
  "policy": "carbon_tax",
  "duration_years": 10
}

Response:
JSON{  "status": "success",  "results": {    "emissions": [100, 95, 90],    "gdp": [50, 52, 54]  }}Show more lines

2. Get Scenarios
GET /scenarios

Description: Lists available policy scenarios.
Response:
JSON{  "scenarios": ["carbon_tax", "renewable_subsidies", "tech_rnd"]}Show more lines

3. Fetch Data
GET /data/climate

Description: Retrieves climate data for visualization.
Response:
JSON{  "temperature": [1.2, 1.3, 1.4],  "co2": [400, 405, 410]}Show more lines

Error Codes

400 – Bad Request
401 – Unauthorized
500 – Internal Server Error


Future Extensions

WebSocket for real-time updates
AI-driven policy recommendations