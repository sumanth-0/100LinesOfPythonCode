#!/usr/bin/env python3
"""
Emoji Sentiment Analyzer
Analyzes the sentiment of text based on emojis present in it.
"""

import re
from collections import Counter
from typing import Dict, List, Tuple


class EmojiSentimentAnalyzer:
    """Analyzes sentiment based on emojis in text."""
    
    def __init__(self):
        """Initialize the analyzer with emoji sentiment mappings."""
        self.positive_emojis = {
            '😀', '😃', '😄', '😁', '😆', '😊', '☺️', '😇', '🙂', '🙃',
            '😉', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '🤗', '🤩',
            '🥳', '😎', '🤓', '🥸', '👍', '👏', '🙌', '👌', '🤝', '💪',
            '❤️', '🧡', '💛', '💚', '💙', '💜', '🤎', '🖤', '🤍', '💖',
            '💗', '💓', '💞', '💕', '💟', '❣️', '✨', '⭐', '🌟', '💫'
        }
        
        self.negative_emojis = {
            '😠', '😡', '🤬', '😤', '😭', '😢', '😥', '😰', '😨', '😱',
            '😖', '😣', '😞', '😓', '😩', '😫', '🥺', '😿', '😾', '💔',
            '👎', '🙁', '☹️', '😦', '😧', '😮', '😯', '😲', '😳', '🥵',
            '🥶', '😬', '🙄', '😑', '😐', '😒', '🙃', '😔', '😕', '🙁'
        }
        
        self.neutral_emojis = {
            '😐', '😑', '🤔', '🤨', '🧐', '🤫', '🤭', '🙊', '🙉', '🙈',
            '💭', '💬', '🗨️', '🗯️', '💤', '👀', '👁️'
        }
    
    def extract_emojis(self, text: str) -> List[str]:
        """Extract all emojis from the given text."""
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F1E0-\U0001F1FF"  # flags
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE
        )
        return emoji_pattern.findall(text)
    
    def analyze_sentiment(self, text: str) -> Dict[str, any]:
        """Analyze sentiment based on emojis in the text."""
        emojis = self.extract_emojis(text)
        
        if not emojis:
            return {
                'sentiment': 'neutral',
                'score': 0.0,
                'emoji_count': 0,
                'details': 'No emojis found'
            }
        
        positive_count = sum(1 for emoji in emojis if emoji in self.positive_emojis)
        negative_count = sum(1 for emoji in emojis if emoji in self.negative_emojis)
        neutral_count = sum(1 for emoji in emojis if emoji in self.neutral_emojis)
        
        total_emojis = len(emojis)
        sentiment_score = (positive_count - negative_count) / total_emojis
        
        if sentiment_score > 0.2:
            sentiment = 'positive'
        elif sentiment_score < -0.2:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        
        return {
            'sentiment': sentiment,
            'score': round(sentiment_score, 2),
            'emoji_count': total_emojis,
            'positive_emojis': positive_count,
            'negative_emojis': negative_count,
            'neutral_emojis': neutral_count,
            'emojis_found': emojis
        }


def main():
    """Main function to demonstrate emoji sentiment analysis."""
    analyzer = EmojiSentimentAnalyzer()
    
    # Example texts
    test_texts = [
        "I love this! 😍🥰❤️",
        "This is terrible 😡😤😠",
        "Not sure about this 🤔🤨",
        "Great day today! 😊👍✨",
        "Feeling sad 😢😭💔"
    ]
    
    print("Emoji Sentiment Analysis Results:")
    print("=" * 50)
    
    for text in test_texts:
        result = analyzer.analyze_sentiment(text)
        print(f"\nText: {text}")
        print(f"Sentiment: {result['sentiment'].upper()}")
        print(f"Score: {result['score']}")
        print(f"Emojis found: {' '.join(result['emojis_found'])}")
        print(f"Breakdown - Positive: {result['positive_emojis']}, "
              f"Negative: {result['negative_emojis']}, "
              f"Neutral: {result['neutral_emojis']}")


if __name__ == "__main__":
    main()
