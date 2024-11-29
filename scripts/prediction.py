import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv("E:/StockSentimentProject/data/reddit_sentiment.csv")

# Debug: Check the data
print("Dataset Shape:", data.shape)
print(data.head())

if data.empty:
    print("Error: The dataset is empty.")
    exit()

# Define features and target
X = data["title"]  # Feature
y = data["sentiment_score"]  # Target

# Vectorize the text feature
vectorizer = TfidfVectorizer(max_features=500)
X_vectorized = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Training Score: {train_score}")
print(f"Testing Score: {test_score}")

# Make predictions
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
