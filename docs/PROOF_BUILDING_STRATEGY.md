# 1️⃣2️⃣ PROOF BUILDING STRATEGY

To simulate real-world development and show a healthy Git commit history, follow this day-wise proof plan. Do not just commit everything at once.

## Day 1: Setup & Architecture
- Initialize Python environment.
- Create folder structure.
- Commit: `chore: initial project setup and folder structure`

## Day 2: Data Ingestion
- Write `src/ingest.py`.
- Configure SQLite schema.
- Run tests to ensure `yfinance` fetches data.
- Commit: `feat: implement yfinance data ingestion and sqlite storage`

## Day 3: Technical Indicators
- Write `src/indicators.py`.
- Compute SMA, MACD, RSI, and Bollinger Bands using Pandas.
- Commit: `feat: add vectorized computation for technical indicators`

## Day 4: Backtesting Engine
- Write `src/backtest.py`.
- Implement SMA Crossover strategy and performance metrics (Sharpe, Drawdown).
- Commit: `feat: implement vectorized backtesting engine with strategy metrics`

## Day 5: API & Alert Scheduler
- Write `api/app.py` and `jobs/alerts.py`.
- Connect the FastAPI endpoints to the local SQLite database.
- Commit: `feat: expose backend processing via FastAPI endpoints`

## Day 6: Frontend Dashboard
- Setup Next.js.
- Create Tailwind CSS dashboard and integrate Recharts.
- Commit: `feat: build interactive Next.js dashboard for data visualization`

## Day 7: Documentation
- Add README, Architecture notes, and screenshots.
- Commit: `docs: add comprehensive project documentation and setup instructions`
