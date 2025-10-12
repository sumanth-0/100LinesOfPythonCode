# Text Summarizer using Word Frequency Analysis

A Python script in 100 lines that summarizes text by identifying and extracting the most important sentences using simple word frequency analysis. 

## How It Works

1. **Sentence Splitting**: Breaks text into individual sentences
2. **Word Tokenization**: Converts sentences into words, removing punctuation
3. **Stop Word Filtering**: Removes common words (a, the, is, etc.)
4. **Frequency Analysis**: Calculates how often important words appear
5. **Sentence Scoring**: Scores each sentence based on its word frequencies
6. **Summary Generation**: Selects top-scoring sentences in their original order

## Usage

Run the script:
```bash
python text_summarizer.py
```

### As a Module

```python
from text_summarizer import summarize_text

text = "Your long text here..."
summary = summarize_text(text, summary_ratio=0.3)  # Keep 30% of sentences
print(summary)
```

## Parameters

- `summary_ratio`: Float between 0.0 and 1.0 indicating what proportion of sentences to keep
  - `0.3` = Keep 30% of sentences (default)
  - `0.5` = Keep 50% of sentences
  - `0.1` = Keep 10% of sentences (more aggressive summarization)

## Features

- ✅ 100 lines of code
- ✅ No external dependencies (uses only standard library)
- ✅ Simple word frequency algorithm
- ✅ Maintains original sentence order
- ✅ Normalizes scores to avoid length bias
- ✅ Filters common stop words



