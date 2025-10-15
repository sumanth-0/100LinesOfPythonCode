# 🧠 MINI SENTIMENT ANALYZER

Analyze the **sentiment** (positive, negative, or neutral) of any text input using Python's `TextBlob` library.  
This script classifies text based on **polarity** and displays the result in a clean, emoji-coded format.

---

## 💡 Features
- 🧩 Under **100 lines of code**
- ⚙️ Uses the `TextBlob` library for polarity-based sentiment analysis  
- 🧠 Detects **Positive 😊**, **Negative 😞**, or **Neutral 😐** tone
- 🧵 Handles invalid or empty input safely
- 💬 Clean and beginner-friendly terminal interface

---

## 💻 How to Run

### Install dependencies
If you haven’t already, install `textblob` and its corpora:
```bash
pip install textblob
python -m textblob.download_corpora
```
Make sure to run inside your conda environment (e.g. sentiment_env).

### Run the script
```bash
python mini_sentiment_analyzer.py
```

Example Output:
```bash
MINI SENTIMENT ANALYZER
Type a sentence or paragraph to analyze sentiment.

Enter your text: I love Hacktoberfest and open source!

📊 Sentiment Result: Positive 😊

(Uses TextBlob for polarity-based sentiment detection.)
```