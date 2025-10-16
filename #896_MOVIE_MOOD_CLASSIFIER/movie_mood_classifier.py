"""
Movie Mood Classifier
Author: Diya Satish Kumar
Classifies a movie review as Positive, Negative, or Neutral using TextBlob.
"""

from textblob import TextBlob

def classify_review(review):
    """Analyze the sentiment polarity of a review."""
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        return "Positive 😊"
    elif polarity < -0.1:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def main():
    print("🎬 MOVIE MOOD CLASSIFIER 🎬")
    print("Enter a movie review below:\n")

    review = input("> ").strip()
    if not review:
        print("⚠️ Empty input! Please enter a valid review.")
        return

    result = classify_review(review)
    print(f"\n🧠 Sentiment Analysis Result: {result}")
    print("\n(Uses TextBlob for polarity-based sentiment detection.)")

if __name__ == "__main__":
    main()
