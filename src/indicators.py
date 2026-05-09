import pandas as pd
import sqlite3
# pyrefly: ignore [missing-import]
from ta.trend import SMAIndicator, MACD
# pyrefly: ignore [missing-import]
from ta.momentum import RSIIndicator
# pyrefly: ignore [missing-import]
from ta.volatility import BollingerBands
import numpy as np

def compute_indicators(db="db/market.db", ticker="AAPL"):
    con = sqlite3.connect(db)
    df = pd.read_sql_query("SELECT date, close FROM candles_daily WHERE ticker=? ORDER BY date", con, params=[ticker])
    if len(df) < 50:
        con.close()
        print(f"Not enough data to compute indicators for {ticker}")
        return
        
    s = df["close"]
    
    # Fill any NaNs
    s = s.ffill().bfill()
    
    sma20 = SMAIndicator(s, window=20).sma_indicator()
    sma50 = SMAIndicator(s, window=50).sma_indicator()
    rsi14 = RSIIndicator(s, window=14).rsi()
    macd_obj = MACD(s)
    macd = macd_obj.macd()
    macd_sig = macd_obj.macd_signal()
    macd_hist = macd_obj.macd_diff()
    
    bb = BollingerBands(s, window=20, window_dev=2)
    
    out = pd.DataFrame({
        "date": df["date"],
        "sma20": sma20, 
        "sma50": sma50, 
        "rsi14": rsi14,
        "macd": macd, 
        "macd_signal": macd_sig, 
        "macd_hist": macd_hist,
        "bb_upper": bb.bollinger_hband(), 
        "bb_mid": bb.bollinger_mavg(), 
        "bb_lower": bb.bollinger_lband()
    }).dropna()
    
    cur = con.cursor()
    cur.executemany("""INSERT OR REPLACE INTO indicators_daily
        (ticker,date,sma20,sma50,rsi14,macd,macd_signal,macd_hist,bb_upper,bb_mid,bb_lower)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        [(ticker, *r) for r in out.itertuples(index=False, name=None)])
    con.commit()
    con.close()
    print(f"Successfully computed indicators for {ticker}")

if __name__ == "__main__":
    compute_indicators()
