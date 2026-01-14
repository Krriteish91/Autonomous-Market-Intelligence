import pandas as pd
from src.exception import CustomException
from src.logger import logging
import sys

INPUT_PATH = "data/processed/market/market_clean.csv"
OUTPUT_PATH = "data/analysis/market_features.csv"

try:
    df = pd.read_csv(INPUT_PATH)  # type: ignore

    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d_%H:%M:%S', errors='coerce')# type: ignore
    df = df.sort_values(by=['symbol', 'date'])  # type: ignore

    df['daily_return'] = (df.groupby('symbol')['close'].pct_change())  # type: ignore
    
    df.to_csv(OUTPUT_PATH, index=False) # type: ignore
    logging.info("Market features analysis completed and saved.")

except Exception as e:
    raise CustomException(e,sys)