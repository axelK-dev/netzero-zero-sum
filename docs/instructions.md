Markdown# Instructions for Running and Using Net Zero – Zero Sum## ✅ Prerequisites- **Python 3.x** installed- Install dependencies:  ```bash  pip install -r requirements.txtShow more lines
(If requirements.txt doesn’t exist yet, add streamlit, pandas, matplotlib.)

✅ Project Structure


```plaintext
netzero-zero-sum/
│
├── src/                     # Source code
│   ├── engine/              # Simulation logic
│   ├── ui/                  # Streamlit dashboard
│   │   ├── dashboard.py     # Main UI file
│   │   └── charts.py        # Chart rendering utilities
│   ├── utils/               # Helper functions
│   └── main.py              # CLI entry point
│
├── data/                    # Static datasets
├── images/                  # Logo and branding assets
├── docs/                    # Documentation
│   └── instructions.md
│
├── requirements.txt         # Python dependencies
└── README.md                # Project overview


✅ Running the Simulation (CLI)
From the project root:
ShellShow more lines

✅ Running the Dashboard (UI)
From the project root:
Shellstreamlit run src/ui/dashboard.pyShow more lines
This will open the dashboard in your browser at:
http://localhost:8501


✅ Features in Dashboard

Sidebar Controls:

Budget allocation slider
Policy selection dropdown


Main View:

Charts for emissions, GDP, and feedback loops
Scenario summary




✅ Adding Logo
Place your logo in:
images/logo.png

Then reference it in dashboard.py:
Pythonst.image("images/logo.png", width=200)Show more lines

✅ Next Steps

Connect simulation engine to UI
Add real datasets in data/
Expand charts in ui/charts.py


✅ Troubleshooting

If you see File does not exist error, check your path and run from the project root.
Use:

Shellstreamlit run src/ui/dashboard.pyShow more lines
not ui/dashboard.py unless you are inside src/ui.

✅ License
MIT License – Open for educational and research use.
