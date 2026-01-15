import pandas as pd
from src.exception import CustomException   
from src.logger import logging
from src.agents.reasoning_agent import reasoning_agent #type: ignore
from src.agents.llm_explainer import hf_llm_explainer #type: ignore
import sys  

try:
    sentiment = pd.read_csv("data/analysis/daily_sentiment.csv")  # type: ignore
    topic_trends = pd.read_csv("data/analysis/topic_trends.csv")  # type: ignore
    
    result = reasoning_agent(sentiment, topic_trends)   
    
    explanation = hf_llm_explainer(result)
    logging.info("Agent Explanation Generated Successfully")
    print("Agent Explanation:\n", explanation)
    
except Exception as e:
    raise CustomException(e, sys)