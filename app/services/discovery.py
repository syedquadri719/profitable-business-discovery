from app.utils.gpt import generate_summary

def get_ideas():
    ideas = [
        {"title": "AI Video Script Generator", "trend_score": 88, "sentiment": 0.72},
        {"title": "Ghost Kitchen for Vegan Desserts", "trend_score": 79, "sentiment": 0.65}
    ]

    for idea in ideas:
        idea["summary"] = generate_summary(
            title=idea["title"],
            trend_score=idea["trend_score"],
            sentiment=idea["sentiment"]
        )

    return ideas
