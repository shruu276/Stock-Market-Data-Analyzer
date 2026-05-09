# 4️⃣ IMPLEMENTATION PLAN

## Phase 1: Setup
- **What to do**: Install Python, Node.js, and create the virtual environment.
- **Why**: Isolates project dependencies.
- **Expected Output**: A clean working environment.
- **Common Beginner Mistakes**: Forgetting to activate the virtual environment before pip install.

## Phase 2: Project folder creation
- **What to do**: Setup the Git repository and directory structure (src, api, docs, apps).
- **Why**: Ensures code is organized and scalable.
- **Expected Output**: Standardized folder tree.
- **Common Beginner Mistakes**: Placing everything in a single `main.py` file.

## Phase 3: Stock data collection
- **What to do**: Write `ingest.py` to pull data from `yfinance` and save to SQLite.
- **Why**: Reliable data is the foundation of the project.
- **Expected Output**: A populated database with AAPL, MSFT, etc.
- **Common Beginner Mistakes**: Not handling missing dates or network timeouts.

## Phase 4: Data cleaning
- **What to do**: Handle missing values, forward-fill NaNs, adjust column names.
- **Why**: Incomplete data crashes mathematical models.
- **Expected Output**: Clean, continuous time-series data.
- **Common Beginner Mistakes**: Dropping all rows with NaNs instead of forward-filling.

## Phase 5: Exploratory data analysis
- **What to do**: Query the database to understand price ranges and volumes.
- **Why**: Understand the data distribution before building models.
- **Expected Output**: SQL queries and basic insights.

## Phase 6: Moving average calculation
- **What to do**: Write `indicators.py` to compute SMA20, SMA50, RSI, MACD.
- **Why**: To generate trading signals.
- **Expected Output**: Populated `indicators_daily` table.

## Phase 7: Return and volatility analysis
- **What to do**: Write `backtest.py` to calculate daily returns, PnL, Max Drawdown, and Sharpe ratio.
- **Why**: Quantifies the risk and reward of the strategy.
- **Expected Output**: JSON object with strategy metrics.

## Phase 8: Visualization
- **What to do**: Build the Next.js frontend with Tailwind and Recharts.
- **Why**: Visuals make the data understandable to non-technical users.
- **Expected Output**: Interactive web dashboard.
- **Common Beginner Mistakes**: Overcomplicating React state management.

## Phase 9: Report generation
- **What to do**: Display strategy results in a neat summary card on the dashboard.
- **Why**: Summarizes the findings for quick decision-making.
- **Expected Output**: PnL and Sharpe ratio displayed clearly.

## Phase 10: GitHub upload
- **What to do**: Write `README.md`, `.gitignore`, and push to GitHub.
- **Why**: To act as a public proof-of-work for recruiters.
- **Expected Output**: A professional GitHub repository.
