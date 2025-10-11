#!/usr/bin/env python3
"""
Movie Review Sentiment Classifier
Classifies movie reviews as positive or negative using TextBlob.
"""

from textblob import TextBlob
import sys


class MovieReviewClassifier:
    """A simple sentiment classifier for movie reviews."""
    
    def __init__(self):
        """Initialize the classifier."""
        self.positive_words = [
            'excellent', 'amazing', 'wonderful', 'fantastic', 'great', 'love',
            'brilliant', 'outstanding', 'perfect', 'best', 'awesome', 'superb'
        ]
        self.negative_words = [
            'terrible', 'awful', 'horrible', 'bad', 'worst', 'hate',
            'disappointing', 'poor', 'boring', 'waste', 'dull'
        ]
    
    def classify_with_textblob(self, review):
        """Classify review using TextBlob sentiment analysis.
        
        Args:
            review (str): The movie review text
            
        Returns:
            tuple: (sentiment, polarity_score)
        """
        blob = TextBlob(review)
        polarity = blob.sentiment.polarity
        
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
            
        return sentiment, polarity
    
    def classify_with_rules(self, review):
        """Classify review using simple rule-based approach.
        
        Args:
            review (str): The movie review text
            
        Returns:
            tuple: (sentiment, score)
        """
        review_lower = review.lower()
        positive_count = sum(1 for word in self.positive_words if word in review_lower)
        negative_count = sum(1 for word in self.negative_words if word in review_lower)
        
        score = positive_count - negative_count
        
        if score > 0:
            sentiment = 'Positive'
        elif score < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
            
        return sentiment, score
    
    def classify(self, review, method='textblob'):
        """Classify a review using the specified method.
        
        Args:
            review (str): The movie review text
            method (str): Classification method ('textblob' or 'rules')
            
        Returns:
            dict: Classification results
        """
        if method == 'textblob':
            sentiment, score = self.classify_with_textblob(review)
        else:
            sentiment, score = self.classify_with_rules(review)
            
        return {
            'review': review,
            'sentiment': sentiment,
            'score': score,
            'method': method
        }


def main():
    """Main function to run the classifier."""
    classifier = MovieReviewClassifier()
    
    print("Movie Review Sentiment Classifier")
    print("=" * 40)
    
    if len(sys.argv) > 1:
        review = ' '.join(sys.argv[1:])
        result = classifier.classify(review)
    else:
        review = input("Enter a movie review: ")
        method = input("Choose method (textblob/rules) [textblob]: ").strip().lower()
        method = method if method in ['textblob', 'rules'] else 'textblob'
        result = classifier.classify(review, method)
    
    print(f"\nReview: {result['review']}")
    print(f"Sentiment: {result['sentiment']}")
    print(f"Score: {result['score']:.2f if isinstance(result['score'], float) else result['score']}")
    print(f"Method: {result['method']}")


if __name__ == "__main__":
    main()
