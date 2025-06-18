import praw
import os

def fetch_reddit_ideas(subreddit="entrepreneur", limit=20):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    ideas = []
    for post in reddit.subreddit(subreddit).hot(limit=limit):
        if not post.stickied and len(post.title) > 10 and post.score > 20:
            ideas.append(post.title.strip())
    return ideas
