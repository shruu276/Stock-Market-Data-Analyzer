# 8️⃣ VIRTUAL SIMULATION

## Simulating a Real Financial Analysis System

When you demonstrate this project in an interview, you are showing a "Virtual Simulation" of a real-world FinTech pipeline. Here is how the system operates conceptually:

1. **How stock data is fetched or loaded**:
   - The user requests a ticker symbol in the dashboard.
   - The backend reaches out to Yahoo Finance APIs to download historical trading data.
   - To avoid hitting rate limits, the backend saves this data locally in an SQLite database. This mimics how quantitative trading desks build internal data lakes.

2. **How price movement is analyzed**:
   - The raw data is passed into our Python processing engine. The `ta` (Technical Analysis) library processes the time-series data using vectorized Pandas operations (fast and efficient).

3. **How moving averages show trend**:
   - The system calculates the 20-day Simple Moving Average (SMA) and the 50-day SMA.
   - When the short-term trend (SMA20) crosses above the long-term trend (SMA50), it is called a "Golden Cross" indicating a potential buy signal. The dashboard visualizes these lines over the closing price.

4. **How volatility shows risk**:
   - Bollinger Bands and the Relative Strength Index (RSI) are calculated.
   - Wide bands indicate high volatility. An RSI below 30 indicates the stock is "oversold" (potential buy), while above 70 indicates "overbought".

5. **How final insights are generated**:
   - The "Run Backtest" button simulates what would have happened if you traded the SMA crossover strategy in the past.
   - It iterates through the historical data, applying transaction fees, and outputs a Net PnL (Profit and Loss), Win Rate, and Maximum Drawdown.

## Artifacts to Capture
When running the simulation locally, capture screenshots of:
- The terminal showing the FastAPI logs and successful data ingestion.
- The interactive Next.js dashboard displaying the price trends.
- The backtesting results summary card showing profitability.
