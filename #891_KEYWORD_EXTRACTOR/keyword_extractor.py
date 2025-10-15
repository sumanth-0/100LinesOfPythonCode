"""
Keyword Extractor
Author: Diya Satish Kumar
Lists the top keywords from a text, ignoring common stopwords.
"""

import re
from collections import Counter

# Basic English stopwords list (you can expand this)
STOPWORDS = {
    "the", "a", "an", "is", "in", "at", "of", "on", "and", "or", "to", "it", 
    "for", "with", "as", "this", "that", "by", "be", "from", "are", "was", "were"
}

def clean_text(text):
    """Normalize text: lowercase and remove punctuation."""
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)  # keep only letters and spaces
    return text

def extract_keywords(text, top_n=10):
    """Extract and display top N keywords."""
    text = clean_text(text)
    words = [word for word in text.split() if word not in STOPWORDS]
    counter = Counter(words)
    return counter.most_common(top_n)

def main():
    print("🔑 KEYWORD EXTRACTOR")
    print("Enter your text below (press Enter twice to analyze):\n")

    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)

    text = " ".join(lines)
    if not text.strip():
        print("⚠️ No input provided. Exiting.")
        return

    top_keywords = extract_keywords(text)
    print("\n📊 Top Keywords:")
    for word, freq in top_keywords:
        print(f"{word:<15} → {freq}")

if __name__ == "__main__":
    main()
