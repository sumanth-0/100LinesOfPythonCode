# Movie Review Sentiment Classifier

A Python-based sentiment analysis tool that classifies movie reviews as positive, negative, or neutral using both TextBlob library and simple rule-based approach.

## Features

- **TextBlob-based Classification**: Uses natural language processing to analyze sentiment polarity
- **Rule-based Classification**: Uses keyword matching with predefined positive and negative word lists
- **Interactive Mode**: Prompt-based user input for review classification
- **Command-line Mode**: Direct review classification via command-line arguments
- **Dual Methods**: Choose between TextBlob or rule-based approach

## Requirements

- Python 3.x
- TextBlob library

## Installation

1. Install the required dependency:
```bash
pip install textblob
```

2. Download the necessary TextBlob corpora:
```bash
python -m textblob.download_corpora
```

## Usage

### Interactive Mode

Run the script without arguments:
```bash
python movie_review_sentiment_classifier.py
```

You'll be prompted to:
1. Enter a movie review
2. Choose classification method (textblob or rules)

### Command-line Mode

Provide the review directly as arguments:
```bash
python movie_review_sentiment_classifier.py "This movie was absolutely fantastic! Great acting and storyline."
```

## Example Output

```
Movie Review Sentiment Classifier
========================================

Review: This movie was absolutely fantastic! Great acting and storyline.
Sentiment: Positive
Score: 0.68
Method: textblob
```

## How It Works

### TextBlob Method
- Analyzes the grammatical structure and word meanings
- Returns a polarity score between -1 (negative) and 1 (positive)
- Sentiment is classified based on the polarity score

### Rule-based Method
- Matches words from predefined positive and negative word lists
- Calculates score as: positive_count - negative_count
- Classifies based on the final score

## Project Structure

```
movie_review_sentiment_classifier/
├── movie_review_sentiment_classifier.py  # Main script
└── README.md                              # This file
```

## Contributing

Feel free to contribute by:
- Adding more sophisticated sentiment analysis methods
- Expanding the positive/negative word lists
- Improving the classification accuracy
- Adding support for more nuanced sentiment levels

## License

This project is part of the 100 Lines of Python Code repository.

## Author

Created as part of issue #684 for the 100LinesOfPythonCode project.
