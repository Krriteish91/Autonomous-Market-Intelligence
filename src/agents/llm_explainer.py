import requests
import os
import sys
from src.exception import CustomException
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def hf_llm_explainer(agent_output: dict) -> str: #type: ignore
    try:
        prompt = f"""
You are a market intelligence assistant.

You must NOT predict prices or give trading advice.

Structured Signals:
- Sentiment Bias: {agent_output['sentiment_bias']}
- Topic Momentum: {agent_output['topic_signal']}
- Market Outlook: {agent_output['market_outlook']}
- Confidence Level: {agent_output['confidence_level']}

Instructions:
- Explain reasoning clearly
- Be concise (4-6 sentences)
- Mention uncertainty if confidence is low

Generate:
1. Market summary
2. Key drivers
3. Risk note
"""

        payload = { #type: ignore
            "model": "meta-llama/Meta-Llama-3-8B-Instruct",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a professional market intelligence analyst."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 300,
            "temperature": 0.3
        }

        response = requests.post(
            HF_API_URL,
            headers=HEADERS,
            json=payload, #type: ignore
            timeout=60
        )

        response.raise_for_status()
        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        raise CustomException(e, sys)
