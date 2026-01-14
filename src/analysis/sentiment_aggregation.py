import pandas as pd
from src.Preprocessing.time_preprocessing import normalize_time
from src.exception import CustomException
import sys
import os
from src.logger import logging

INPUT_PATH = "data/processed/news/news_with_sentiment_transformer.csv"
OUTPUT_PATH = "data/analysis/daily_sentiment.csv"

try:
    df = pd.read_csv(INPUT_PATH)  # type: ignore

    df = normalize_time(df)

    daily = df.groupby('date').agg( # type: ignore
        avg_sentiment = ("sentiment_score", "mean"),  # type: ignore
        postive_count = ("sentiment_label", lambda x: (x == 'positive').sum()),  # type: ignore
        negative_count = ("sentiment_label", lambda x: (x == 'negative').sum()),  # type: ignore
        article_count = ("sentiment_label", "count")  # type: ignore
    ).reset_index()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    daily.to_csv(OUTPUT_PATH, index=False)  # type: ignore
    logging.info(f"Daily sentiment aggregation saved to {OUTPUT_PATH}")
except Exception as e:
    raise CustomException(e, sys)