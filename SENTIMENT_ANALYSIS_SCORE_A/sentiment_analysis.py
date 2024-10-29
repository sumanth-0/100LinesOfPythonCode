

import pandas as pd
from textblob import TextBlob

class SentimentAnalyzer:
    def analyze_sentiment(self, text):
        """Analyze sentiment of the given text and return polarity and subjectivity."""
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        return polarity, subjectivity

def main():
    print("Sentiment Analysis Tool")
    while True:
        user_input = input("Enter a sentence to analyze (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the sentiment analysis tool.")
            break
        polarity, subjectivity = SentimentAnalyzer().analyze_sentiment(user_input)
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        print(f"Sentiment: {sentiment}\nPolarity: {polarity:.2f}, Subjectivity: {subjectivity:.2f}")

if __name__ == "__main__":
    main()
