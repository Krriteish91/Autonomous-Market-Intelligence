import pandas as pd
from sentence_transformers import SentenceTransformer
from src.exception import CustomException   
import os 
import sys
import numpy as np
from src.logger import logging

INPUT_PATH = "data/processed/news/news_preprocessed.csv"
OUTPUT_PATH = "data/processed/news/news_embeddings.npy"

df=pd.read_csv(INPUT_PATH)  # type: ignore

model_name = 'all-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

try:
    embeddings = model.encode( # type: ignore
        df['clean_text'].tolist(), # type: ignore
        show_progress_bar=True,
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    np.save(OUTPUT_PATH, embeddings)     # type: ignore
    logging.info(f"Embeddings saved to {OUTPUT_PATH}")
    logging.info(f"Embeddings shape: {embeddings.shape}") # type: ignore
except Exception as e:
    raise CustomException(e, sys)
