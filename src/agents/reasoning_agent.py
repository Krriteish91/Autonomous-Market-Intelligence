
from src.exception import CustomException   
from src.logger import logging
import sys

def reasoning_agent(sentiment_df,topic_df): #type: ignore
    try:
        latest_sentiments = sentiment_df.iloc[-1]   #type: ignore
        trending_topics = topic_df[topic_df['trend_score'] > 1.5]   #type: ignore

        sentiment = latest_sentiments['avg_sentiment'] #type: ignore

        if(sentiment > 0.3):
            sentiment_bias = "positive"
        elif(sentiment < -0.3):
            sentiment_bias = "negative"
        else:
            sentiment_bias = "neutral"

        if(len(trending_topics) >= 2): #type: ignore
            topic_signal = "strong"

        elif(len(trending_topics) == 1): #type: ignore
            topic_signal = "moderate"   
        else:
            topic_signal = "weak"

        if(sentiment_bias == "positive" and topic_signal in ["strong","moderate"]):
            outlook = "Bullish Bias"
            confidence = "High"
        elif(sentiment_bias == "negative" and topic_signal in ["strong","moderate"]):
            outlook = "Bearish Bias"
            confidence = "High"
        else:
            outlook = "Neutral/Uncertain"
            confidence = "Low"
        logging.info("Reasoning Agent Processed Successfully")  
        return {
            "sentiment_bias": sentiment_bias,
            "topic_signal": topic_signal,
            "market_outlook": outlook,
            "confidence_level": confidence,
            "Explanation": f"Lagged sentiment is {sentiment_bias} with {topic_signal} topic momentum."
        }

    except Exception as e:
        raise CustomException(e, sys)