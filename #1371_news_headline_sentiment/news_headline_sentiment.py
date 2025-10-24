# -----------------------------
# 1. Import required libraries
# -----------------------------
import requests
from textblob import TextBlob

# -----------------------------
# 2. News API setup
# -----------------------------
API_KEY = "YOUR_NEWSAPI_KEY"  # Replace with your API key
NEWS_URL = "https://newsapi.org/v2/top-headlines"
PARAMS = {
    "country": "us",   # Change country if needed
    "pageSize": 10,    # Number of headlines to fetch
    "apiKey": API_KEY
}

# -----------------------------
# 3. Fetch news headlines
# -----------------------------
def fetch_headlines():
    """Fetch top news headlines from NewsAPI."""
    response = requests.get(NEWS_URL, params=PARAMS)
    data = response.json()
    if data.get("status") != "ok":
        print("Error fetching news:", data.get("message"))
        return []
    headlines = [article["title"] for article in data.get("articles", [])]
    return headlines

# -----------------------------
# 4. Analyze sentiment
# -----------------------------
def analyze_sentiment(text):
    """Return 'Positive', 'Negative', or 'Neutral' based on sentiment polarity."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# -----------------------------
# 5. Main program
# -----------------------------
if __name__ == "__main__":
    print("Fetching latest news headlines...\n")
    headlines = fetch_headlines()

    if not headlines:
        print("No headlines found.")
    else:
        for idx, headline in enumerate(headlines, start=1):
            sentiment = analyze_sentiment(headline)
            print(f"{idx}. {headline} -> {sentiment}")
