# 🎭 Detailed Sentiment Analyzer

This Python script provides a detailed sentiment analysis of text. It goes beyond a simple mood classification by calculating and displaying two key metrics: **Polarity** (how positive or negative the text is) and **Subjectivity** (how much of an opinion it is vs. a fact).

This tool is built using the `TextBlob` library for its simplicity and power in natural language processing.

## ✨ Features

-   **Mood Classification**: Classifies sentences into **Happy 😊**, **Sad 😢**, or **Neutral 😐**.
-   **Polarity Score**: Provides a numeric score from -1.0 (most negative) to +1.0 (most positive).
-   **Subjectivity Score**: Provides a numeric score from 0.0 (very objective) to 1.0 (very subjective).
-   **Detailed Output**: Displays all analysis results in a clean, readable format.

## ⚙️ Setup

1.  **Prerequisites**: Make sure you have **Python 3.x** installed.

2.  **Install the library**:
    This project requires the `TextBlob` library. Install it using pip:
    ```bash
    pip install textblob
    ```

## 🚀 Usage

To run the analysis on the example sentences, simply execute the script from your terminal:

```bash
python main.py
```

You can customize the sentences to be analyzed by editing the `sentences_to_test` list directly in the `main.py` file.

## 📊 Understanding the Output

The script provides two main scores for each sentence:

-   **Polarity**: This score represents the emotional leaning of the sentence. A positive score means a happy sentiment, a negative score means a sad sentiment, and a score near zero is neutral.
-   **Subjectivity**: This score measures whether the sentence is more of a factual statement or a personal opinion. A score of `0.0` means it's very objective, while a score of `1.0` means it's very subjective.

### Demo Output
```text
--- Detailed Mood Summary ---
Sentence: 'I am incredibly happy and excited about this new project!'
  - Mood: Happy 😊
  - Polarity: 0.92
  - Subjectivity: 0.95

Sentence: 'The Earth is the third planet from the Sun.'
  - Mood: Neutral 😐
  - Polarity: 0.00
  - Subjectivity: 0.00

Sentence: 'I think this is the best movie ever made.'
  - Mood: Happy 😊
  - Polarity: 0.75
  - Subjectivity: 0.45
```