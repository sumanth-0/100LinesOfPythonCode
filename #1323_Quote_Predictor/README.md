# 🧠 Celebrity Quote Predictor (Rule-Based)

A simple **Python rule-based text classification script** that predicts which celebrity is most likely to have said a given quote — based on **keyword and phrase matching** using regular expressions.

---

## 📋 Overview

This script uses a dictionary of predefined **signature phrases**, **catchphrases**, or **stylistic patterns** associated with famous personalities.  
When a quote is input, it searches for these patterns and assigns a **"hit count"** to each celebrity.  
The celebrity with the highest number of hits is predicted as the **speaker**.

---

## ⚙️ Features

- 🧩 **Rule-based NLP** using regex patterns.  
- 🔍 **Case-insensitive matching** for robust detection.  
- 🧠 **Multiple celebrity profiles** supported (easy to extend).  
- 📈 **Hit count scoring system** for confidence-based predictions.  
- 🧪 **Includes demo quotes** for quick testing.

---

---

## 🚀 How It Works

1. Each celebrity has a set of **rules** — unique keywords or phrases.
2. The script scans an input quote and counts how many of those rules match.
3. The celebrity with the most matches is returned as the predicted speaker.
4. If no matches are found, the result is **"Unknown Speaker"**.

---

## 🧩 Example Rules

```python
PREDICTION_RULES = {
    "Yoda": [
        r"hmmm", "always in motion", r"\bdo or do not\b", "much to learn", 
        "powerful you have become", "judge me by my size"
    ],
    "Oprah Winfrey": [
        "best life", "aha moment", "live your truth", "what I know for sure",
        "stand in your power"
    ],
    "Dwayne 'The Rock' Johnson": [
        "Jabroni", "candy", "smell what The Rock is cooking", "layeth the smack down",
        "finally"
    ],
    "Taylor Swift": [
        "long list of ex-lovers", "shake it off", "dear John", "karma is", 
        "lover", "haters gonna hate"
    ]
}

