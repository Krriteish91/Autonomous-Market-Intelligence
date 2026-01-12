import pandas as pd 
from src.Preprocessing.text_cleaning import preprocess_news
from src.exception import CustomException   
from src.logger import logging
import sys

INPUT_PATH = "data/processed/news/news_clean.csv"
OUTPUT_PATH = "data/processed/news/news_preprocessed.csv"
try:
    logging.info("Starting preprocessing script")
    df = pd.read_csv(INPUT_PATH) #type: ignore
    logging.info(f"Loaded data from {INPUT_PATH} with shape {df.shape}")
    df = preprocess_news(df)


    df.to_csv(OUTPUT_PATH, index=False)
    logging.info(f"Preprocessed data saved to {OUTPUT_PATH}")
except Exception as e:
    raise CustomException(e, sys)

