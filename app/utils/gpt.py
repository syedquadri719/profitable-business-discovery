import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(title: str, trend_score: int, sentiment: float) -> str:
    prompt = f"""You're an expert startup analyst.

A Reddit user posted this title: "{title}"

Based on the tone and content, extract and describe a potential business idea this post implies or inspires.

Explain in 1–2 sentences as if you're pitching the concept to an entrepreneur."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
