import streamlit as st
import pandas as pd
from src.agents.reasoning_agent import reasoning_agent
from src.agents.llm_explainer import hf_llm_explainer

st.set_page_config(page_title="Market Intelligence Dashboard", layout="wide")

st.title("📊 Autonomous Market Intelligence System")

# Load data
sentiment = pd.read_csv("data/analysis/daily_sentiment.csv")
topics = pd.read_csv("data/analysis/topic_trends.csv")

st.sidebar.header("Controls")
run_agent = st.sidebar.button("Run Market Intelligence")

if run_agent:
    agent_output = reasoning_agent(sentiment, topics)
    explanation = hf_llm_explainer(agent_output)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Market Signals")
        st.metric("Sentiment Bias", agent_output["sentiment_bias"])
        st.metric("Topic Momentum", agent_output["topic_signal"])
        st.metric("Market Outlook", agent_output["market_outlook"])
        st.metric("Confidence", agent_output["confidence_level"])

    with col2:
        st.subheader("🧠 LLM Commentary")
        st.write(explanation)

st.subheader("📉 Sentiment Trend")
st.line_chart(sentiment.set_index("date")["avg_sentiment"])

st.subheader("🔥 Trending Topics")
st.dataframe(
    topics.sort_values("trend_score", ascending=False).head(10)
)
