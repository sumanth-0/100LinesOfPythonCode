# Text Summarizer

A Python script that summarizes text by keeping only the most important sentences using simple word frequency analysis.

## Features

- **Frequency-based Extractive Algorithm**: Analyzes word frequencies to identify important sentences
- **Stop Words Filtering**: Removes common words to focus on meaningful content
- **Normalized Scoring**: Scores sentences based on normalized word frequencies
- **Maintains Original Order**: Preserves the original sequence of selected sentences
- **Configurable Summary Ratio**: Adjust the proportion of sentences to include in the summary

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Installation

No installation required. Simply download the script:

```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/text_summarizer
```

## Usage

### Interactive Mode

Run the script and enter text when prompted:

```bash
python text_summarizer.py
```

### Programmatic Usage

```python
from text_summarizer import summarize

text = """
Your long text goes here. The text summarizer will analyze word frequencies
and select the most important sentences. It uses an extractive approach,
meaning it pulls sentences directly from the original text rather than
generating new ones.
"""

# Summarize with default 30% ratio
summary = summarize(text)
print(summary)

# Summarize with custom ratio (e.g., 50% of sentences)
summary = summarize(text, ratio=0.5)
print(summary)
```

## How It Works

1. **Text Cleaning**: Removes extra whitespace and normalizes the input text
2. **Sentence Tokenization**: Splits text into individual sentences
3. **Word Tokenization**: Extracts words and converts them to lowercase
4. **Frequency Analysis**: Calculates word frequencies while filtering stop words
5. **Sentence Scoring**: Scores each sentence based on the frequency of words it contains
6. **Sentence Selection**: Selects top-scoring sentences based on the specified ratio
7. **Order Preservation**: Returns selected sentences in their original order

## Algorithm Details

### Stop Words Filtering

The script filters out common English stop words like "the", "is", "at", "which", etc. This helps focus on content-bearing words.

### Scoring Formula

Each sentence is scored using:
```
sentence_score = sum(normalized_word_frequencies) / number_of_words
```

This approach favors sentences with high-frequency important words while normalizing for sentence length.

## Example

### Input
```
Artificial intelligence is transforming technology. Machine learning algorithms can process vast amounts of data. Neural networks are inspired by the human brain. Deep learning has revolutionized computer vision. Natural language processing enables computers to understand text. AI applications are everywhere in modern life.
```

### Output (30% ratio - 2 sentences)
```
Deep learning has revolutionized computer vision. Neural networks are inspired by the human brain.
```

## Limitations

- Works best with structured, well-written text
- May not capture context or semantic relationships
- Limited stop word list (can be expanded)
- No handling of complex linguistic structures
- Best suited for informative/factual text rather than narrative content

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is part of the 100LinesOfPythonCode repository. See the main repository for license information.

## References

- Issue: #682
- Repository: [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode)
