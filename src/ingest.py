# pyrefly: ignore [missing-import]
import yfinance as yf
import pandas as pd
import sqlite3
import datetime as dt
import os

def init_db(db_path="db/market.db", schema_path="db/schema.sql"):
    con = sqlite3.connect(db_path)
    with open(schema_path, "r") as f:
        con.executescript(f.read())
    con.commit()
    con.close()

def fetch_daily(ticker: str, start="2015-01-01", end=None):
    if end is None:
        end = dt.date.today().isoformat()
    df = yf.download(ticker, start=start, end=end, auto_adjust=False)
    if df.empty:
        print(f"Warning: No data fetched for {ticker}")
        return pd.DataFrame(columns=["date","open","high","low","close","adj_close","volume"])
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    
    df = df.reset_index()
    df.columns = [str(c).lower() for c in df.columns]
    
    if 'date' in df.columns:
        df["date"] = pd.to_datetime(df["date"]).dt.date.astype(str)
    elif 'index' in df.columns:
        df["date"] = pd.to_datetime(df["index"]).dt.date.astype(str)
    
    if "adj close" in df.columns:
        df.rename(columns={"adj close":"adj_close"}, inplace=True)
    elif "adj_close" not in df.columns:
        df["adj_close"] = df["close"] # fallback
        
    cols_to_keep = ["date","open","high","low","close","adj_close","volume"]
    # keep only columns that exist, missing ones might happen depending on yfinance response
    existing_cols = [c for c in cols_to_keep if c in df.columns]
    for c in cols_to_keep:
        if c not in existing_cols:
            df[c] = 0.0 # dummy value for missing optional columns
            
    return df[["date","open","high","low","close","adj_close","volume"]]

def upsert_daily(db="db/market.db", ticker="AAPL"):
    df = fetch_daily(ticker)
    if df.empty:
        return
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.executemany("""INSERT OR REPLACE INTO candles_daily
        (ticker,date,open,high,low,close,adj_close,volume)
        VALUES (?,?,?,?,?,?,?,?)""",
        [(ticker, *r) for r in df.itertuples(index=False, name=None)])
    
    # ensure symbol is in symbols table
    cur.execute("INSERT OR IGNORE INTO symbols(ticker, name, exchange, currency) VALUES (?, ?, ?, ?)", 
                (ticker, ticker, "UNKNOWN", "USD"))
    
    con.commit()
    con.close()
    print(f"Successfully upserted data for {ticker}")

if __name__ == "__main__":
    init_db()
    upsert_daily()
