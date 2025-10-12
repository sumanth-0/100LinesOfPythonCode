# AI-Powered Text Mood Highlighter

A Python CLI tool that analyzes and highlights text based on mood/sentiment (positive, negative, neutral) with color-coded output.

## Features

- 🎨 **Color-coded output**: Visual highlighting of text based on sentiment
  - Green: Positive sentiment
  - Red: Negative sentiment
  - Yellow: Neutral sentiment
- 🧠 **Dual analysis modes**:
  - TextBlob-based sentiment analysis (when installed)
  - Rule-based keyword analysis (fallback)
- 📊 **Sentiment scores**: Shows polarity scores with TextBlob
- 📝 **Sentence-level analysis**: Analyzes and highlights each sentence individually
- ⚡ **Simple CLI interface**: Easy to use from command line or interactive mode

## Requirements

- Python 3.6+
- TextBlob (optional but recommended)

## Installation

1. Clone this repository or download the script
2. (Optional) Install TextBlob for more accurate sentiment analysis:

```bash
pip install textblob
python -m textblob.download_corpora
```

## Usage

### Command Line Mode

```bash
python ai_powered_text_mood_highlighter.py "Your text here"
```

### Interactive Mode

```bash
python ai_powered_text_mood_highlighter.py
```

Then enter your text when prompted.

## Examples

```bash
# Example 1: Positive text
python ai_powered_text_mood_highlighter.py "I love this amazing product! It's wonderful."

# Example 2: Mixed sentiment
python ai_powered_text_mood_highlighter.py "The movie was great but the ending was disappointing."

# Example 3: Multiple sentences
python ai_powered_text_mood_highlighter.py "What a beautiful day! I'm so happy. Everything is perfect."
```

## How It Works

### TextBlob Mode (Recommended)

When TextBlob is installed, the tool uses sentiment analysis to calculate polarity scores:
- Polarity > 0.1: Positive
- Polarity < -0.1: Negative
- -0.1 ≤ Polarity ≤ 0.1: Neutral

### Rule-Based Mode (Fallback)

When TextBlob is not available, the tool uses keyword matching:
- Counts positive keywords (happy, love, great, etc.)
- Counts negative keywords (sad, hate, terrible, etc.)
- Determines sentiment based on keyword frequency

## Output Format

```
==============================================================
TEXT MOOD ANALYSIS
==============================================================

[POSITIVE] I love this product! [0.50]
[NEGATIVE] The service was terrible. [-0.70]
[NEUTRAL] The building is tall. [0.00]

==============================================================
```

## Code Structure

The script is under 100 lines and includes:
- Sentiment analysis functions (TextBlob and rule-based)
- Text highlighting with ANSI color codes
- Sentence splitting and processing
- CLI interface

## Contributing

Feel free to submit issues and pull requests!

## License

This project is open source and available under the MIT License.

## Related Issue

This tool addresses issue #645 in the 100LinesOfPythonCode repository.
