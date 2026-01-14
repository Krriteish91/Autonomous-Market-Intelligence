import pandas as pd
import sys
from src.exception import CustomException
from src.logger import logging

INPUT_PATH = "data/processed/news/news_with_topics.csv"
OUTPUT_PATH = "data/analysis/topic_trends.csv"

def detect_trending_topics(df: pd.DataFrame, window: int = 3) -> pd.DataFrame:
    df["rolling_avg"] = (
        df.groupby("topic_id")["article_count"]  # type: ignore
          .transform(lambda x: x.rolling(window).mean())  # type: ignore
    )

    df["trend_score"] = df["article_count"] - df["rolling_avg"]
    return df


try:
    df = pd.read_csv(INPUT_PATH)  # type: ignore

    df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce')  # type: ignore

    df['date'] = df['published_at'].dt.date  # type: ignore

    # Topic frequency per day
    daily_topics = (
        df.groupby(['date', 'topic_id']).size().reset_index(name='article_count') # type: ignore
    )
    daily_topics = detect_trending_topics(daily_topics)
    daily_topics.to_csv(OUTPUT_PATH, index=False)
    logging.info("Topic trends analysis completed and saved.")
except Exception as e:
    raise CustomException(e,sys)



