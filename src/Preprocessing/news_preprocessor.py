import json
import pandas as pd
import glob
import os
import sys

from typing import Any
from src.exception import CustomException
from src.logger import logging

RAW_NEWS_PATH = "data/raw/news/*.json"
PROCESSED_PATH = "data/processed/news/news_clean.csv"

def process_news():
    try:
        records:Any = []
        logging.info("Starting news data processing")
        for file in glob.glob(RAW_NEWS_PATH):
          with open(file, "r") as f:
             data = json.load(f)

          source = "newsapi" if "articles" in data else "gnews"
          articles = data.get("articles", data.get("articles", []))

          for idx, article in enumerate(articles):
            records.append({
                "article_id": f"{source}_{idx}",
                "source": source,
                "title": article.get("title"),
                "description": article.get("description"),
                "content": article.get("content"),
                "published_at": article.get("publishedAt") or article.get("published_at"),
                "url": article.get("url")
            })

        df = pd.DataFrame(records)
        df.drop_duplicates(subset=["title"], inplace=True)
        df.dropna(subset=["title"], inplace=True)  # type: ignore[call-overload]


        os.makedirs(os.path.dirname(PROCESSED_PATH), exist_ok=True)
        df.to_csv(PROCESSED_PATH, index=False)
        logging.info(f"Processed news data saved successfully at {PROCESSED_PATH}")
        print(f" Processed news saved → {PROCESSED_PATH}")
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    process_news()
