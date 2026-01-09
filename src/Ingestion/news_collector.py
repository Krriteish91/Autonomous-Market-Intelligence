import os 
import sys
import json
import requests


from typing import Any
from dotenv import load_dotenv
from datetime import datetime
from src.exception import CustomException
from src.logger import logging
load_dotenv()


NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWSAPI_BASE_URL = "https://newsapi.org/v2/everything"

GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
GNEWS_BASE_URL = "https://gnews.io/api/v4/top-headlines"
def fetch_news(query: str="stocks",source: str = "newsapi"):
    logging.info("Fetching news data from NewsAPI")
    try:
        params: dict[str,Any] = {
        "q" : query,
        "apiKey": NEWS_API_KEY

    }
        response = requests.get(NEWSAPI_BASE_URL, params=params)
        response.raise_for_status()
        news_data = response.json()
        save_news(news_data, source)
    except Exception as e:
        raise CustomException(e,sys)


def fetch_gnews(query: str="stocks", source: str = "gnews"):
    logging.info("Fetching news data from GNews")
    try:
        params: dict[str,Any] = {
        "q" : query,
        "lang": "en",
        "country": "in",
        "apikey": GNEWS_API_KEY
    }
        response = requests.get(GNEWS_BASE_URL, params=params)
        response.raise_for_status()
        news_data = response.json()
        save_news(news_data, source)
    except Exception as e:
        raise CustomException(e,sys)



def save_news(news_data: dict[str, Any], source: str) -> None:

    try:
        time_stamp = datetime.now().strftime("%Y%m%d %H%M%S")
        path = f"data/raw/news/{source}__{time_stamp}.json"
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, 'w') as f:
           json.dump(news_data, f, indent=4)

        logging.info(f"News data saved to {path}")

        print(f"News data saved to {path}")
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    fetch_news()
    fetch_gnews()
