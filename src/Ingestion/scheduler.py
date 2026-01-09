
from src.Ingestion.news_collector import fetch_news, fetch_gnews
from src.Ingestion.market_collector import fetch_market_data    
from src.logger import logging
from src.exception import CustomException
import sys

def run_ingestion_cycle():
    try:
        logging.info("Starting ingestion cycle")

        # Fetch market data
        fetch_market_data("AAPL")
        fetch_market_data("GOOGL")

        # Fetch news data
        fetch_news()
        fetch_gnews()

        logging.info("Ingestion cycle completed successfully")
    except Exception as e:
        raise CustomException(e, sys)
    
if __name__ == "__main__":
    run_ingestion_cycle()
        