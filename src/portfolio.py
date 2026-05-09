import sqlite3
import pandas as pd

def positions(db="db/market.db"):
    con = sqlite3.connect(db)
    tx = pd.read_sql_query("SELECT * FROM portfolio_tx ORDER BY ts", con, parse_dates=["ts"])
    
    if tx.empty: 
        con.close()
        return pd.DataFrame(columns=["ticker","qty","avg_cost"])
        
    pos = (tx.assign(signed_qty=lambda d: d["qty"].where(d["side"]=="BUY", -d["qty"]))
             .groupby("ticker", as_index=False)
             .agg(qty=("signed_qty","sum"),
                  cost=("price","mean")))
                  
    con.close()
    pos.rename(columns={"cost":"avg_cost"}, inplace=True)
    return pos
