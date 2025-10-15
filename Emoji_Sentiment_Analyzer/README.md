# Emoji Sentiment Analyzer

A Python tool that analyzes the sentiment of text based on emojis present in it.

## Description

This Emoji Sentiment Analyzer extracts emojis from text and determines the overall sentiment (positive, negative, or neutral) based on emoji classifications. The tool uses regex patterns to identify emojis and maintains dictionaries of emoji categories to calculate sentiment scores.

## Features

- **Emoji Extraction**: Automatically extracts all emojis from input text using regex patterns
- **Sentiment Analysis**: Categorizes emojis as positive, negative, or neutral
- **Sentiment Scoring**: Calculates a normalized sentiment score based on emoji distribution
- **Detailed Breakdown**: Provides counts of each emoji category found
- **Multiple Text Support**: Can analyze multiple texts in batch

## Requirements

- Python 3.6+
- No external dependencies required (uses only standard library)

## Usage

```python
from emoji_sentiment_analyzer import EmojiSentimentAnalyzer

# Create analyzer instance
analyzer = EmojiSentimentAnalyzer()

# Analyze text
text = "I love this! 😍🥰❤️"
result = analyzer.analyze_sentiment(text)

print(f"Sentiment: {result['sentiment']}")
print(f"Score: {result['score']}")
print(f"Emojis found: {result['emojis_found']}")
```

## Running the Script

```bash
python emoji_sentiment_analyzer.py
```

## Output Format

The analyzer returns a dictionary containing:
- `sentiment`: Overall sentiment classification ('positive', 'negative', or 'neutral')
- `score`: Normalized sentiment score between -1 and 1
- `emoji_count`: Total number of emojis found
- `positive_emojis`: Count of positive emojis
- `negative_emojis`: Count of negative emojis
- `neutral_emojis`: Count of neutral emojis
- `emojis_found`: List of all emojis extracted

## Example Output

```
Emoji Sentiment Analysis Results:
==================================================

Text: I love this! 😍🥰❤️
Sentiment: POSITIVE
Score: 1.0
Emojis found: 😍 🥰 ❤️
Breakdown - Positive: 3, Negative: 0, Neutral: 0
```

## Author

Created as part of the 100 Lines of Python Code project.

## Issue Reference

Resolves #759 - Emoji Sentiment Analyzer
