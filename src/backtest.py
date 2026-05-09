import pandas as pd
import numpy as np
import sqlite3
import json
import uuid
import datetime as dt

def run_sma_backtest(db="db/market.db", ticker="AAPL", fee_bps=5, start=None, end=None):
    con = sqlite3.connect(db)
    df = pd.read_sql_query("""
      SELECT c.date, c.close, i.sma20, i.sma50
      FROM candles_daily c JOIN indicators_daily i ON i.ticker=c.ticker AND i.date=c.date
      WHERE c.ticker=? ORDER BY c.date
    """, con, params=[ticker])
    con.close()
    
    if start: df = df[df["date"]>=start]
    if end: df = df[df["date"]<=end]
    df = df.dropna().reset_index(drop=True)
    
    if len(df) == 0:
        return {"error": "Not enough data for backtest"}

    signal = (df["sma20"] > df["sma50"]).astype(int)  # 1=long, 0=flat
    pos = signal.shift(1).fillna(0)  # enter next day open/close simplification
    ret = df["close"].pct_change().fillna(0.0)
    gross = pos * ret
    turns = (pos.diff().abs().fillna(0) > 0).astype(int)
    cost = turns * (fee_bps/10000.0)
    net = gross - cost

    equity = (1 + net).cumprod()
    pnl = float(equity.iloc[-1] - 1)
    roll = equity.pct_change().fillna(0.0)
    sharpe = float(np.sqrt(252) * (roll.mean() / (roll.std()+1e-9))) if roll.std() > 0 else 0.0
    peak = equity.cummax()
    dd = (equity/peak - 1).min()
    trades = int(turns.sum())
    win_rate = float((net[turns==1] > 0).mean() if trades else 0)

    # Format dates and curve for JSON serialization
    dates = df["date"].tolist()
    curve = equity.tolist()

    return {
      "pnl": pnl, 
      "max_dd": float(dd), 
      "sharpe": sharpe, 
      "trades": trades, 
      "win_rate": win_rate,
      "curve": curve, 
      "dates": dates
    }

def save_backtest(db, name, params, ticker, stats):
    if "error" in stats:
        return None
        
    con = sqlite3.connect(db)
    cur = con.cursor()
    bid = str(uuid.uuid4())
    
    # Store curve as stringified json (optional, for later plotting)
    params["curve"] = stats.get("curve", [])
    params["dates"] = stats.get("dates", [])
    
    cur.execute("""INSERT INTO backtests(id,name,params_json,start,end,ticker,pnl,max_dd,sharpe,trades,win_rate,created_at)
                   VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                (bid, name, json.dumps(params), stats["dates"][0], stats["dates"][-1], ticker,
                 stats["pnl"], stats["max_dd"], stats["sharpe"], stats["trades"], stats["win_rate"],
                 dt.datetime.utcnow().isoformat()))
    con.commit()
    con.close()
    return bid
