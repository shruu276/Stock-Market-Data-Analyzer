# 5️⃣ FOLDER STRUCTURE

```text
Stock-Market-Data-Analyzer/
│
├── api/                  # FastAPI backend
│   └── app.py            # API routes and server config
├── apps/
│   └── web/              # Next.js frontend dashboard
├── db/                   # SQLite database and schema
│   └── schema.sql        # Table definitions
├── docs/                 # Project documentation
├── jobs/                 # Background workers and schedulers
│   └── alerts.py         # Alert evaluation logic
├── notebooks/            # Jupyter notebooks for EDA and prototyping
├── src/                  # Core Python modules
│   ├── ingest.py         # yfinance data fetching
│   ├── indicators.py     # Technical indicators computation
│   ├── backtest.py       # Strategy simulation engine
│   ├── portfolio.py      # Portfolio tracking logic
│   └── seed.py           # Initial data population script
├── main.py               # Main entry point to run API
├── requirements.txt      # Python dependencies
├── .gitignore            # Files to ignore in Git
└── README.md             # Project overview
```

## Explanation
- **`api/`**: Contains the FastAPI REST service that connects the Python processing engine to the web frontend.
- **`apps/web/`**: The modern Next.js + Tailwind CSS + Recharts interactive dashboard.
- **`db/`**: Houses the local SQLite database ensuring data is persisted and queryable.
- **`jobs/`**: Standalone scripts that can be run on a schedule (cron) to monitor the market and send alerts.
- **`src/`**: The decoupled heart of the application containing data ingestion, analysis, and backtesting logic. Modular design makes it easy to swap data providers.
- **`docs/`**: Comprehensive theoretical and operational documentation for GitHub visitors and interviewers.
