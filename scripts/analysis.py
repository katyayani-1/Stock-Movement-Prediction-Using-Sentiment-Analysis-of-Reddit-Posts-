import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Load the scraped Reddit data
df = pd.read_csv("E:/StockSentimentProject/data/reddit_posts.csv")

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Add sentiment scores to the data
df['sentiment_score'] = df['title'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

# Save sentiment data to a new CSV file
df.to_csv("E:/StockSentimentProject/data/reddit_sentiment.csv", index=False)

print("Sentiment analysis completed successfully!")
