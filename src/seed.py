import os
from src.ingest import init_db, upsert_daily
from src.indicators import compute_indicators
import sqlite3

def seed_data():
    db_path = "db/market.db"
    
    if not os.path.exists("db"):
        os.makedirs("db")
        
    print("Initializing Database...")
    init_db(db_path, "db/schema.sql")
    
    # Add a sample alert
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO alerts(id, ticker, rule, threshold) VALUES ('a1', 'AAPL', 'RSI_LT', 30)")
    con.commit()
    con.close()
    
    symbols = ["AAPL", "MSFT", "GOOGL", "NVDA", "TSLA"]
    
    print("Fetching historical data and computing indicators...")
    for sym in symbols:
        print(f"Processing {sym}...")
        upsert_daily(db_path, sym)
        compute_indicators(db_path, sym)
        
    print("Seeding complete!")

if __name__ == "__main__":
    seed_data()
