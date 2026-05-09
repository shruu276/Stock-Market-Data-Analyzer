# 9️⃣ HOW TO RUN PROJECT

Follow these steps to run the complete system on your local machine.

## 1. Start the Python Backend API
Open a terminal, activate your virtual environment, and run the FastAPI server:

**Windows:**
```bash
venv\Scripts\activate
python main.py
```

**Mac/Linux:**
```bash
source venv/bin/activate
python main.py
```

*Expected Terminal Output:*
```text
INFO:     Uvicorn running on http://127.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## 2. Start the Next.js Frontend Dashboard
Open a **second terminal window**, navigate to the web app, and start the development server:

```bash
cd apps/web
npm run dev
```

*Expected Terminal Output:*
```text
ready - started server on 0.0.0.0:3000, url: http://localhost:3000
```

## 3. View the Application
Open your web browser and go to: **[http://localhost:3000](http://localhost:3000)**

### Testing the Features
1. **Refresh Data**: Enter a stock ticker (e.g., `NVDA`) in the top bar and click the refresh icon. The backend will pull the latest data.
2. **View Charts**: Look at the interactive Recharts graphing the closing price alongside the SMA20 and SMA50.
3. **Run Backtest**: Click the "Run Backtest" button. The backend will compute the historical performance of the SMA Crossover strategy and display the Net PnL, Win Rate, and Max Drawdown on the dashboard.
