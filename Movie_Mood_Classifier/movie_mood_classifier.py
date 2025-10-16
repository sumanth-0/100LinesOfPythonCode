"""
Movie Review Sentiment Classifier 🎬
-----------------------------------
Classify a movie review as Positive, Negative, or Neutral using TextBlob.

Usage:
    python movie_review_sentiment.py
"""

from textblob import TextBlob


def classify_review(review: str) -> str:
    """
    Analyze sentiment of a given movie review.

    Parameters:
        review (str): The text of the review.

    Returns:
        str: Sentiment classification ("Positive", "Negative", "Neutral")
    """
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity  # Range: [-1.0, 1.0]

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    return "Neutral"


def main() -> None:
    """Main CLI interface for classifying a movie review."""
    print("🎬 Movie Review Sentiment Classifier")
    print("------------------------------------")

    review = input("Enter your movie review: ").strip()

    if not review:
        print("Please enter a valid review.")
        return

    sentiment = classify_review(review)
    print(f"\n🧠 Sentiment: {sentiment}")


if __name__ == "__main__":
    main()
