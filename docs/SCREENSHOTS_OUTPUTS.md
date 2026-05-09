# 1️⃣3️⃣ SCREENSHOTS / OUTPUTS

To build a compelling GitHub README, you must capture visual proof of your project working. Here is exactly what you need to capture and where to place it in the README:

## 1. Project Folder Structure Screenshot
- Open VS Code.
- Expand all the folders in the explorer sidebar (`api`, `apps`, `docs`, `src`).
- Take a clean screenshot. This proves you know how to organize a modern application.

## 2. Terminal Output
- Capture the terminal running `uvicorn` (FastAPI) showing the logs of successful requests (`GET /symbols`, `POST /backtest/sma`).
- Capture the SQLite CLI or a DB Viewer showing rows of data in the `candles_daily` and `indicators_daily` tables.

## 3. The Dashboard (The Most Important Image)
- Open `http://localhost:3000` in your browser.
- Type in a famous ticker like `NVDA` or `AAPL`.
- Capture the entire screen showing the dark-mode premium UI, the KPI cards, and the Recharts graph.
- Name it `dashboard.png` and put it at the very top of your README.

## 4. Backtest Results
- Click "Run Backtest" on the dashboard.
- Capture a close-up screenshot of the Strategy Performance card showing the "Net PnL", "Win Rate", and "Max Drawdown".
- This is critical for proving the analytical value of the application.
