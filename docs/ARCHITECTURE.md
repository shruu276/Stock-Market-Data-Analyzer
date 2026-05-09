# 3️⃣ PROJECT ARCHITECTURE

## Data Flow
The architecture follows a modern decoupled data pipeline pattern:
1. **Input Generation**: User requests data for a ticker via the Next.js frontend.
2. **Data Ingestion**: The FastAPI backend receives the request and utilizes `yfinance` to pull OHLCV data.
3. **Storage**: Raw data is persisted in a local SQLite database (`candles_daily` table).
4. **Processing**: The `ta` library computes indicators (SMA, MACD, RSI, Bollinger Bands) and stores them in `indicators_daily`.
5. **Backtesting Engine**: Analyzes the historical data using a predefined strategy (e.g., SMA Cross) and calculates risk/return metrics (PnL, Sharpe Ratio, Max Drawdown).
6. **Output**: The frontend queries the processed data and renders interactive charts and summary reports using Recharts.

## Architecture Diagram
```text
[ Next.js Dashboard ] (Frontend)
       │      ▲
  HTTP │      │ JSON (Charts, Stats)
  POST │      │
       ▼      │
[ FastAPI Service ] (Backend API)
       │      ▲
       │      │
       ▼      │
[ Python Processing Engine ]
  ├─ ingest.py (yfinance fetcher)
  ├─ indicators.py (ta library)
  ├─ backtest.py (Strategy simulation)
  └─ portfolio.py (P&L tracking)
       │      ▲
       │      │ SQL
       ▼      │
[ SQLite Database ]
  ├─ symbols
  ├─ candles_daily
  ├─ indicators_daily
  ├─ backtests
  └─ alerts
```
