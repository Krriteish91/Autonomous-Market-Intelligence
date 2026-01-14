import pandas as pd
from src.exception import CustomException
from src.logger import logging  
import sys

SENTIMENT_PATH = "data/analysis/daily_sentiment.csv"
MARKET_PATH = "data/analysis/market_features.csv"
OUTPUT_PATH = "data/analysis/sentiment_market_merged.csv"

try:
    sent = pd.read_csv(SENTIMENT_PATH) # type: ignore
    market = pd.read_csv(MARKET_PATH) # type: ignore

    sent["date"] = pd.to_datetime(sent["date"])     # type: ignore
    market["date"] = pd.to_datetime(market["date"]) # type: ignore

    df = sent.merge(market, on="date", how="inner") # type: ignore

    df.to_csv(OUTPUT_PATH, index=False)
    logging.info("Sentiment-market correlation analysis completed and saved.")
except Exception as e:
    raise CustomException(e, sys)


