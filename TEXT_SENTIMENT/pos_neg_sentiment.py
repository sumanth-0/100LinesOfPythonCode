"""
Visualize positive vs negative sentiment across user-entered paragraphs.
Requirements:
    pip install nltk matplotlib
"""
from typing import List
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Ensure VADER lexicon is availableP
nltk.download("vader_lexicon", quiet=True)

def analyze_paragraphs(paragraphs: List[str]):
    sia = SentimentIntensityAnalyzer()
    results = []
    for p in paragraphs:
        scores = sia.polarity_scores(p)
        results.append({
            "text": p,
            "pos": scores["pos"],
            "neg": scores["neg"],
            "neu": scores["neu"],
            "compound": scores["compound"],
        })
    return results

def plot_pos_vs_neg(results, title="Positive vs Negative Sentiment by Paragraph"):
    labels = [f"P{i+1}" for i in range(len(results))]
    pos = [r["pos"] for r in results]
    neg = [-r["neg"] for r in results]
    compounds = [r["compound"] for r in results]
    y = range(len(results))

    fig, ax = plt.subplots(figsize=(8, max(4, len(results) * 0.6)))
    ax.barh(y, pos, align="center", label="Positive", color="seagreen")
    ax.barh(y, neg, align="center", label="Negative", color="salmon")
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Sentiment score (fraction)")
    ax.set_title(title)
    ax.axvline(0, color="black", linewidth=0.8)

    for i, c in enumerate(compounds):
        ax.text(max(pos[i], 0.02) + 0.02, i, f"compound={c:.2f}", va="center", fontsize=8)

    ax.legend(loc="lower right")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Enter paragraphs (press ENTER twice to finish):")
    paragraphs = []
    while True:
        p = input()
        if not p.strip():
            break
        paragraphs.append(p.strip())

    if not paragraphs:
        print("No input provided.")
    else:
        results = analyze_paragraphs(paragraphs)
        plot_pos_vs_neg(results, title="User Input: Positive vs Negative Sentiment")
