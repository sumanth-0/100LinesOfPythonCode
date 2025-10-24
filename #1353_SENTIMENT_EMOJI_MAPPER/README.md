# Sentiment Emoji Mapper

A simple Python script that analyzes the sentiment of a given text and maps it to an appropriate emoji. The program uses a predefined sentiment dictionary to score words and displays an emoji representing the overall sentiment.

---

## Features

- Assigns sentiment scores to words using a built-in dictionary.
- Calculates the total sentiment score for user input.
- Maps the score to an emoji (positive, neutral, or negative).
- Runs interactively in the terminal.

---

## How It Works

1. The user enters a sentence or phrase.
2. The script splits the text into words and sums their sentiment scores.
3. The total score is mapped to an emoji:
   - Extremely Positive: 😍
   - Positive: 😊
   - Neutral: 🙂
   - Slightly Negative: 😐
   - Negative: 😟
   - Very Negative: 😢
   - Extremely Negative: 😡
4. The emoji is printed to the console.

---

## Example Output

```
Enter text to analyze sentiment: I love this amazing product!
Sentiment Emoji: 😍
```