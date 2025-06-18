import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(title: str, trend_score: int, sentiment: float) -> str:
    prompt = f"""Summarize why the following business idea might be trending:

Title: {title}
Trend Score: {trend_score}
Sentiment Score: {sentiment}

Respond in 1–2 sentences.
"""

    if not openai.api_key:
        raise Exception("Missing OpenAI API key")

    response = openai.ChatCompletion.create(
        model="gpt-4o",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message["content"].strip()
