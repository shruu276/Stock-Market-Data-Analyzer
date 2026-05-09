from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import datetime as dt
from src.ingest import upsert_daily
from src.indicators import compute_indicators
from src.backtest import run_sma_backtest, save_backtest
from typing import Optional

DB = "db/market.db"
app = FastAPI(title="Stock Market Data Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def q(sql, params=()):
    try:
        con = sqlite3.connect(DB)
        con.row_factory = sqlite3.Row
        rows = con.execute(sql, params).fetchall()
        con.close()
        return [dict(r) for r in rows]
    except Exception as e:
        print(f"Database error: {e}")
        return []

@app.get("/symbols")
def get_symbols():
    return q("SELECT ticker, name FROM symbols")

@app.post("/refresh/{ticker}")
def refresh(ticker: str, background_tasks: BackgroundTasks):
    # Process in background so UI doesn't block
    def task():
        upsert_daily(DB, ticker)
        compute_indicators(DB, ticker)
    background_tasks.add_task(task)
    return {"message": f"Refresh started for {ticker} in background."}

@app.get("/chart/{ticker}")
def chart(ticker: str, days: int = 252):
    rows = q("""SELECT c.date, c.close, i.sma20, i.sma50, i.rsi14, i.bb_upper, i.bb_lower, c.volume
              FROM candles_daily c LEFT JOIN indicators_daily i
              ON i.ticker=c.ticker AND i.date=c.date
              WHERE c.ticker=? ORDER BY c.date DESC LIMIT ?""",[ticker, days])
    return list(reversed(rows))

class BacktestReq(BaseModel):
    ticker: str
    fee_bps: int = 5
    start: Optional[str] = None
    end: Optional[str] = None

@app.post("/backtest/sma")
def backtest(req: BacktestReq):
    stats = run_sma_backtest(DB, req.ticker, req.fee_bps, req.start, req.end)
    if "error" in stats:
        raise HTTPException(status_code=400, detail=stats["error"])
        
    bid = save_backtest(DB, "SMA20>50", req.dict(), req.ticker, stats)
    return {"id": bid, "stats": stats}

@app.get("/backtests")
def list_backtests():
    return q("SELECT * FROM backtests ORDER BY created_at DESC LIMIT 10")

@app.get("/alerts")
def list_alerts(): 
    return q("SELECT * FROM alerts WHERE active=1")
