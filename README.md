This project predicts stock price movements by analyzing sentiment from Reddit discussions in stock-related subreddits. It uses sentiment analysis to classify posts and machine learning to predict stock trends.
Setup
Clone the repo:

git clone https://github.com/yourusername/StockSentimentProject.git

cd StockSentimentProject

Create and activate a virtual environment:

python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Get Reddit API credentials by creating an app on Reddit and update them in scraper.py.

Run the Scripts
1.Scrape Reddit data
python scraper.py

2.Perform Sentiment Analysis:
python analysis.py

3.Train Model & Predict:
python prediction.py

