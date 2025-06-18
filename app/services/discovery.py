from scrapers.reddit_scraper import fetch_reddit_ideas
from app.utils.gpt import generate_summary

def get_ideas():
    titles = fetch_reddit_ideas(limit=20)

    # Fallback if Reddit returned too few ideas
    if not titles or len(titles) < 3:
        titles = [
            "Automated bookkeeping for Shopify sellers",
            "Peer-to-peer storage rentals in urban areas",
            "Virtual interior design using AI and AR",
        ]

    ideas = []
    for title in titles:
        idea = {
            "title": title,
            "trend_score": 80,
            "sentiment": 0.7,
            "summary": generate_summary(title, 80, 0.7),
        }
        ideas.append(idea)

    return ideas
