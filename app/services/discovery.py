from scrapers.reddit_scraper import fetch_reddit_ideas
from app.utils.gpt import generate_summary

def get_ideas():
    titles = fetch_reddit_ideas()  # from r/entrepreneur

    ideas = []
    for title in titles:
        idea = {
            "title": title,
            "trend_score": 80,  # Dummy for now
            "sentiment": 0.7,   # Dummy for now
        }
        idea["summary"] = generate_summary(title, idea["trend_score"], idea["sentiment"])
        ideas.append(idea)

    return ideas
