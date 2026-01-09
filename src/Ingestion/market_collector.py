import yfinance as yf #type: ignore
import json
import os
import sys


from datetime import datetime
from typing import Any
from src.logger import logging
from src.exception import CustomException


def fetch_market_data(symbol: str = "AAPL", period: str = "3m"):
    logging.info(f"Fetching market data for {symbol}")
    try:
        stock:Any = yf.Ticker(symbol)
        hist:Any = stock.history(period=period)

        data: dict[str,Any]= {
            "symbol": symbol,
            "fetch_time": datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),
            "prices": hist.reset_index().to_dict(orient="records")
        }
        logging.info(f"Market data fetched successfully for {symbol}")
        save_raw_data(data, symbol)
    except Exception as e:
        raise CustomException(e,sys)

def save_raw_data(data: dict[str,Any],symbol:str) -> None:
    try:
        time_stamp = datetime.now().strftime("%Y%m%d %H%M%S")
        path = f"data/raw/market/{symbol}__{time_stamp}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)
    
        with open(path, 'w') as f:
           json.dump(data, f, indent=4)

        logging.info(f"Market data saved successfully for {symbol} at {path}")

        print(f"Market data saved to {path}")
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    fetch_market_data("AAPL")
    fetch_market_data("GOOGL")