#!/usr/bin/env python3
"""
AI-Powered Text Mood Highlighter
Highlights text based on mood analysis (positive, negative, neutral)
using TextBlob for sentiment analysis with colored output.
"""

import sys
import re
from typing import List, Tuple

try:
    from textblob import TextBlob
    HAS_TEXTBLOB = True
except ImportError:
    HAS_TEXTBLOB = False
    print("TextBlob not installed. Using rule-based analysis.")
    print("Install with: pip install textblob")

# ANSI color codes for terminal output
COLORS = {
    'positive': '\033[92m',  # Green
    'negative': '\033[91m',  # Red
    'neutral': '\033[93m',   # Yellow
    'reset': '\033[0m'
}

# Rule-based keyword lists for fallback
POSITIVE_KEYWORDS = [
    'happy', 'joy', 'love', 'excellent', 'great', 'wonderful', 'amazing',
    'good', 'best', 'fantastic', 'beautiful', 'perfect', 'awesome', 'brilliant'
]

NEGATIVE_KEYWORDS = [
    'sad', 'angry', 'hate', 'terrible', 'bad', 'awful', 'horrible',
    'worst', 'poor', 'disappointing', 'ugly', 'nasty', 'miserable'
]

def analyze_sentiment_textblob(text: str) -> Tuple[str, float]:
    """Analyze sentiment using TextBlob."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0.1:
        return 'positive', polarity
    elif polarity < -0.1:
        return 'negative', polarity
    else:
        return 'neutral', polarity

def analyze_sentiment_rules(text: str) -> str:
    """Analyze sentiment using rule-based keywords."""
    text_lower = text.lower()
    pos_count = sum(1 for word in POSITIVE_KEYWORDS if word in text_lower)
    neg_count = sum(1 for word in NEGATIVE_KEYWORDS if word in text_lower)
    
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'

def highlight_text(text: str, mood: str, score: float = None) -> str:
    """Apply color highlighting to text based on mood."""
    color = COLORS.get(mood, COLORS['neutral'])
    reset = COLORS['reset']
    score_str = f" [{score:.2f}]" if score is not None else ""
    return f"{color}{text}{reset}{score_str}"

def process_text(text: str) -> None:
    """Process and highlight text based on sentences."""
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    
    print("\n" + "="*60)
    print("TEXT MOOD ANALYSIS")
    print("="*60 + "\n")
    
    for sentence in sentences:
        if not sentence.strip():
            continue
            
        if HAS_TEXTBLOB:
            mood, score = analyze_sentiment_textblob(sentence)
            highlighted = highlight_text(sentence, mood, score)
        else:
            mood = analyze_sentiment_rules(sentence)
            highlighted = highlight_text(sentence, mood)
        
        print(f"[{mood.upper()}] {highlighted}")
    
    print("\n" + "="*60)

def main():
    """Main function to run the mood highlighter."""
    print("AI-Powered Text Mood Highlighter")
    print("-" * 40)
    
    if len(sys.argv) > 1:
        # Read from command line argument
        text = ' '.join(sys.argv[1:])
    else:
        # Interactive mode
        print("Enter text to analyze (or 'quit' to exit):")
        text = input("> ")
        
        if text.lower() == 'quit':
            return
    
    if text.strip():
        process_text(text)
    else:
        print("No text provided.")

if __name__ == "__main__":
    main()
