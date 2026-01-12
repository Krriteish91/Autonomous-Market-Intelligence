import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from src.exception import CustomException       
import joblib # type: ignore
import sys
import os
from src.logger import logging

INPUT_PATH = "data/processed/news/news_preprocessed.csv"
MODEL_PATH = "models/tfidf_vectorizer.pkl"

try:
    df= pd.read_csv(INPUT_PATH)  # type: ignore
    vectorizer = TfidfVectorizer(max_features=5000,stop_words='english')

    X = vectorizer.fit_transform(df['clean_text'])  # type: ignore

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(vectorizer, MODEL_PATH) # type: ignore

    logging.info(f"TF-IDF Vectorizer model saved to {MODEL_PATH}")
except Exception as e:
    raise CustomException(e, sys)

