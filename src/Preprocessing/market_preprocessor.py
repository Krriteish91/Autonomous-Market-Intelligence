import json 
import pandas as pd
import glob
import os
import sys

from src.exception import CustomException
from src.logger import logging

RAW_MARKET_PATH = "data/raw/market/*.json"
PROCESSED_PATH = "data/processed/market/market_clean.csv"

def process_market():
    try:
        records = []
        logging.info("Starting market data processing")

        for file in glob.glob(RAW_MARKET_PATH):
          with open(file, "r") as f:
            data = json.load(f)

          symbol = data.get("symbol")
        

          for row in data.get("prices"):
            records.append({ # type: ignore
                "symbol": symbol,
                "date": row.get("Date"),
                "open": row.get("Open"),
                "high": row.get("High"),
                "low": row.get("Low"),
                "close": row.get("Close"),
                "volume": row.get("Volume")
             }) 

        df = pd.DataFrame(records)
        
        df.drop_duplicates(subset=["symbol", "date"], inplace=True)

        os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
        df.to_csv(PROCESSED_PATH, index=False)
        logging.info(f"Processed market data saved successfully at {PROCESSED_PATH}")

    except Exception as e:
        raise CustomException(e, sys)
if __name__ == "__main__":
    process_market()
