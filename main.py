import uvicorn
import os
import sys

# Ensure modules in src/ can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.seed import seed_data

if __name__ == "__main__":
    if not os.path.exists("db/market.db"):
        print("Database not found. Seeding initial data...")
        seed_data()
    
    print("Starting API Server...")
    uvicorn.run("api.app:app", host="127.0.0.1", port=8000, reload=True)
