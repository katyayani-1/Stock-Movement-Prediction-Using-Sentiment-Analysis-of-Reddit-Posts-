import praw
import pandas as pd
import time

# Reddit API credentials
client_id = "Vgcrkep8gbdVF2FI325AjA"
client_secret = "g3BBDzQz07KE6yb0uAqJK9Fj88guYg"
user_agent = "script:StockScraper:v1.0 (by /u/Alternative-Line-795)"

# Initialize Reddit API
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Function to scrape Reddit posts from a subreddit
def scrape_reddit(subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.hot(limit=limit):
        posts.append([post.title, post.selftext, post.score, post.url, post.created])

    return pd.DataFrame(posts, columns=["title", "body", "score", "url", "created"])

# Scraping stock-related posts
df = scrape_reddit("stocks", limit=100)

# Saving data to a CSV file
df.to_csv("reddit_posts.csv", index=False)

print("Reddit data scraped successfully!")
