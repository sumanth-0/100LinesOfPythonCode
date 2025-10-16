# Text Summarizer

A Python script that extracts the most important sentences from a paragraph using word frequency analysis.

## Description

This script analyzes a given text and identifies the most important sentences based on word frequency. It works by:

1. **Tokenizing** the text into individual sentences
2. **Calculating word frequencies** while filtering out common stop words
3. **Scoring each sentence** based on the cumulative frequency of its words
4. **Ranking and extracting** the top N sentences with the highest scores

The algorithm normalizes sentence scores by length to avoid bias towards longer sentences, ensuring that both long and short sentences are fairly evaluated.

## Features

- Word frequency-based sentence extraction
- Stop words filtering (common words like "the", "a", "is", etc.)
- Sentence score normalization to prevent length bias
- Interactive command-line interface
- Customizable number of sentences to extract
- Clean and well-documented code

## Prerequisites

- Python 3.6 or higher
- No external libraries required (uses only Python standard library)

## Installation

No installation required. Simply download the `text_summarizer.py` file.

## Usage

### Basic Usage

Run the script:

```bash
python text_summarizer.py
```

The program will prompt you to:
1. Enter or paste your paragraph (press Enter twice to finish)
2. Specify how many important sentences you want to extract

### Example

```
==============================================================
Text Summarizer - Extract Important Sentences
==============================================================

Enter or paste your paragraph (press Enter twice to finish):
Artificial intelligence is transforming the world. Machine learning algorithms can now recognize patterns in vast amounts of data. Deep learning, a subset of machine learning, uses neural networks with multiple layers. These technologies are being applied in healthcare, finance, and many other fields. AI systems can diagnose diseases, predict market trends, and even drive cars autonomously.

How many important sentences to extract? (default: 3): 3

==============================================================
Top 3 Most Important Sentences:
==============================================================

1. Machine learning algorithms can now recognize patterns in vast amounts of data
2. Deep learning, a subset of machine learning, uses neural networks with multiple layers
3. AI systems can diagnose diseases, predict market trends, and even drive cars autonomously

==============================================================
```

## How It Works

### Algorithm

1. **Text Preprocessing**: Removes extra whitespace and cleans the input text
2. **Sentence Tokenization**: Splits text into individual sentences using punctuation markers
3. **Word Frequency Calculation**:
   - Converts text to lowercase
   - Removes punctuation
   - Filters out stop words
   - Counts word occurrences
4. **Sentence Scoring**:
   - Each sentence receives a score based on the sum of its words' frequencies
   - Scores are normalized by sentence length
5. **Ranking**: Sentences are sorted by score in descending order
6. **Extraction**: Returns the top N sentences

### Stop Words

The script filters out common English stop words including:
- Articles (a, an, the)
- Conjunctions (and, or, but)
- Prepositions (in, on, at, to, for, etc.)
- Common verbs (is, was, are, were, have, etc.)
- Pronouns (I, you, he, she, it, we, they)

## Code Structure

- `preprocess_text()`: Cleans input text
- `tokenize_sentences()`: Splits text into sentences
- `calculate_word_frequency()`: Computes word frequencies excluding stop words
- `score_sentences()`: Assigns scores to sentences based on word frequencies
- `extract_top_sentences()`: Main function that orchestrates the extraction process
- `main()`: Interactive CLI interface

## Limitations

- Works best with English text (stop words are English-specific)
- Requires well-formed sentences with proper punctuation
- Word frequency may not always correlate with semantic importance
- Does not consider context or sentence relationships

## Future Enhancements

- Support for multiple languages
- Custom stop words list
- TF-IDF (Term Frequency-Inverse Document Frequency) scoring
- Sentence position weighting
- Export results to file

## Contributing

Feel free to fork this project and submit pull requests with improvements!

## License

This project is open source and available under the MIT License.

## Author

Created as part of the 100 Lines of Python Code project.
