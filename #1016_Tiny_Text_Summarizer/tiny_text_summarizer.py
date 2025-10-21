# Tiny Text Summarizer
# Issue #1016

from collections import Counter
import re

def summarize_text(text, num_sentences=2):
    sentences = re.split(r'(?<=[.!?]) +', text)
    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)
    sentence_scores = {}
    for sent in sentences:
        for word in re.findall(r'\w+', sent.lower()):
            if word in freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq[word]
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(top_sentences)

if __name__ == "__main__":
    text = input("Enter a paragraph to summarize:\n")
    print("\nSummary:\n", summarize_text(text))
