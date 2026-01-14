import pandas as pd
from src.exception import CustomException   
import sys      
from src.logger import logging

def normalize_time(df: pd.DataFrame):
    try:
        df['published_at'] = pd.to_datetime(df['published_at'], errors='coerce') # type: ignore
        df["date"] = df['published_at'].dt.date # type: ignore
        logging.info("Time normalization completed successfully.")
    except Exception as e:
        raise CustomException(e, sys)

    return df