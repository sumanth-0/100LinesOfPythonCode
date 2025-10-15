"""
Mini Sentiment Analyzer
Author: Diya Satish Kumar
Analyze user input text as Positive, Negative, or Neutral using TextBlob.
"""

from textblob import TextBlob

def analyze_sentiment(text):
    """Return sentiment label based on polarity."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return "Positive 😊"
    elif polarity < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def main():
    print("🧠 MINI SENTIMENT ANALYZER")
    print("Type a sentence or paragraph to analyze sentiment.\n")

    text = input("Enter your text: ").strip()
    if not text:
        print("⚠️ Empty input! Please enter valid text.")
        return

    sentiment = analyze_sentiment(text)
    print(f"\n📊 Sentiment Result: {sentiment}")

    print("\n(Uses TextBlob for polarity-based sentiment detection.)")

if __name__ == "__main__":
    main()
