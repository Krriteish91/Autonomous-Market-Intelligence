import pandas as pd
from transformers import pipeline # type: ignore
from src.exception import CustomException
import sys  
from src.logger import logging

INPUT_PATH = "data/processed/news/news_preprocessed.csv"
OUTPUT_PATH = "data/processed/news/news_with_sentiment_transformer.csv"

sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert", tokenizer="ProsusAI/finbert")

df = pd.read_csv(INPUT_PATH)  # type: ignore
try:
    def predict_sentiment(text):  # type: ignore
        if not text or len(text)<10 : # type: ignore
            return "neutral",0.0
        
        result = sentiment_pipeline(text,truncation=True)[0]  # type: ignore
        return result['label'].lower(), result['score']  # type: ignore
    df[['sentiment_label', 'sentiment_score']] = df['clean_text'].apply(  # type: ignore
        lambda x: pd.Series(predict_sentiment(x))  # type: ignore
    )
    df.to_csv(OUTPUT_PATH, index=False)  # type: ignore
    logging.info(f"Data with transformer sentiment scores saved to {OUTPUT_PATH}")
except Exception as e:  
    raise CustomException(e, sys)