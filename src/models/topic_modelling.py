import pandas as pd
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
import os
from src.exception import CustomException
import sys
from src.logger import logging


INPUT_PATH = "data/processed/news/news_preprocessed.csv"
OUTPUT_PATH = "data/processed/news/news_with_topics.csv"

try:
    df = pd.read_csv(INPUT_PATH)  # type: ignore
    text = df['clean_text'].astype(str).tolist()  # type: ignore
    logging.info("Data loaded for topic modelling.")
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    topic_model = BERTopic(
        embedding_model=embedding_model,
        min_topic_size=10,
        verbose=True,
        )

    topics, probs = topic_model.fit_transform(text)  # type: ignore


    df['topic_id'] = topics  # type: ignore
    df['topic_confidence'] = probs  # type: ignore
    os.makedirs("data/processed/news", exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    logging.info(f"Data with topics saved to {OUTPUT_PATH}")
except Exception as e:
    raise CustomException(e, sys)

topic_info = topic_model.get_topic_info()  # type: ignore
topic_keywords = topic_model.get_topics()  # type: ignore
