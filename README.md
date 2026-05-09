# Stock Market Data Analyzer

![Dashboard Preview](images/dashboard.png) *(Note: Please add screenshot to images folder)*

## Project Overview
A complete, decoupled Python pipeline and Next.js dashboard for ingesting, analyzing, and backtesting stock market data. This project fetches historical OHLCV data, calculates technical indicators (SMA, RSI, MACD), simulates quantitative trading strategies, and presents the insights via a modern, interactive web interface.

## Problem Statement
Analyzing stock market trends manually through spreadsheets is inefficient and prone to error. This project automates the data collection, mathematical modeling, and visualization, allowing analysts to instantly view historical trends and validate the mathematical edge of simple trading strategies (like Moving Average Crossovers).

## Industry Relevance
Fintech companies, brokers, and quantitative trading desks rely on robust data pipelines. This project mirrors a modern FinTech architecture:
- **Data Engineering**: Reliable ingestion and SQLite storage of time-series data.
- **Quantitative Analysis**: Vectorized computation of technical indicators using Pandas.
- **Backend APIs**: Exposing insights via FastAPI.
- **Frontend**: Premium data visualization using Next.js and Recharts.

## Features
- **Live Data Ingestion**: Automated fetching of historical stock prices via `yfinance`.
- **Technical Indicators**: Calculates SMA20, SMA50, RSI(14), MACD, and Bollinger Bands.
- **Vectorized Backtesting**: Simulates a "Golden Cross" (SMA20 > SMA50) trading strategy, calculating Net PnL, Win Rate, and Max Drawdown.
- **Premium Dashboard**: A glassmorphism dark-mode UI built with Tailwind CSS and Recharts for interactive exploration.
- **RESTful API**: Fast and scalable endpoints served by FastAPI.

## Tech Stack
- **Backend**: Python 3.10+, FastAPI, Pandas, NumPy, SQLite, `yfinance`, `ta` (Technical Analysis library).
- **Frontend**: Next.js (React), Tailwind CSS, Recharts, Lucide React.

## Folder Structure
```text
Stock-Market-Data-Analyzer/
├── api/             # FastAPI REST endpoints
├── apps/web/        # Next.js Dashboard
├── db/              # SQLite database and schema
├── src/             # Core Python modules (Ingest, Indicators, Backtest)
├── jobs/            # Background alert scripts
└── docs/            # Comprehensive documentation
```

## How to Run

### 1. Python Backend
```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # Or source venv/bin/activate on Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Seed the database
python src/seed.py

# Start the API
python main.py
```

### 2. Next.js Frontend
```bash
cd apps/web
npm install
npm run dev
```

Visit `http://localhost:3000` to view the dashboard!

## Sample Output
The backtesting engine outputs actionable metrics like:
`PnL: 154.2% • MaxDD: -22.4% • Sharpe: 1.15 • Trades: 42 • Win%: 45.2%`

## Learning Outcomes
By building this project, I demonstrated proficiency in:
- Building robust, decoupled architectures.
- Time-series data manipulation with Pandas.
- Developing and testing API endpoints with FastAPI.
- Managing database state with SQLite.
- Creating highly interactive and visually appealing frontend dashboards.

---
**Disclaimer**: This project is for educational purposes only and does not constitute financial advice. The trading strategies simulated here are rudimentary and should not be used with real money.
