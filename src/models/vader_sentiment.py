from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # type: ignore
import pandas as pd
from src.exception import CustomException   
import sys  
from src.logger import logging

INPUT_PATH = "data/processed/news/news_preprocessed.csv"
OUTPUT_PATH = "data/processed/news/news_with_sentiment_vader.csv"

analyser = SentimentIntensityAnalyzer()

def get_sentiment(text):    # type: ignore
    scores = analyser.polarity_scores(text) # type: ignore
    return scores['compound']

df = pd.read_csv(INPUT_PATH)  # type: ignore
try:
    df['sentiment_score'] = df['clean_text'].apply(get_sentiment)  # type: ignore

    logging.info("Sentiment scores computed using VADER.")

    df['sentiment_label'] = df['sentiment_score'].apply( # type: ignore
        lambda score: 'positive' if score >= 0.05 else ('negative' if score <= -0.05 else 'neutral') # type: ignore
    )
    logging.info("Sentiment labels assigned based on VADER scores.")

    df.to_csv(OUTPUT_PATH, index=False)  # type: ignore
    logging.info(f"Data with VADER sentiment scores saved to {OUTPUT_PATH}")
except Exception as e:
    raise CustomException(e, sys)