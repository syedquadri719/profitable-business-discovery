# Sample Reddit scraper using PRAW
import praw

def fetch_reddit_posts(subreddit="entrepreneur", limit=5):
    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="business-discovery-script"
    )
    posts = []
    for post in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({"title": post.title, "score": post.score})
    return posts
