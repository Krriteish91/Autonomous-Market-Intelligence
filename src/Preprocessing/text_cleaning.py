import re
import pandas as pd
import sys

from src.exception import CustomException
from src.logger import logging

def clean_text(text: str) -> str:
    try:
        logging.info("Starting text cleaning process")

        if pd.isna(text): # type: ignore
            return ""
        
        text = text.lower()
        text = re.sub(r"http\S+", "", text)  # Remove URLs
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters and numbers
        text = re.sub(r"\s+", " ", text).strip()  # Remove extra
        return text
    
    except Exception as e:
        raise CustomException(e, sys)
    
def preprocess_news(df: pd.DataFrame) -> pd.DataFrame:
    try:
        logging.info("Preprocessing news DataFrame")
        df["clean_text"] = (
        df["title"].fillna("") + " " + # type: ignore
        df["description"].fillna("") + " " +  # type: ignore
        df["content"].fillna("")  # type: ignore
        )

        df["clean_text"] = df["clean_text"].apply(clean_text)  # type: ignore
        return df
    
    except Exception as e:
        raise CustomException(e, sys)