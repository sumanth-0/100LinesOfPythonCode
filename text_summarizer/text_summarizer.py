#!/usr/bin/env python3
"""
Text Summarizer using Frequency-based Extractive Algorithm
Summarizes text by keeping only the most important sentences.
"""

import re
from collections import Counter
from string import punctuation


def clean_text(text):
    """Remove extra whitespace and normalize text."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def tokenize_sentences(text):
    """Split text into sentences."""
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]


def tokenize_words(text):
    """Extract words and convert to lowercase."""
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return words


def get_word_frequencies(sentences):
    """Calculate word frequency scores."""
    all_words = []
    for sentence in sentences:
        all_words.extend(tokenize_words(sentence))
    
    # Remove common stop words
    stop_words = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'and', 'or',
                  'but', 'in', 'with', 'to', 'for', 'of', 'as', 'by', 'that',
                  'this', 'it', 'from', 'be', 'are', 'was', 'were', 'been',
                  'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                  'could', 'should', 'may', 'might', 'can'}
    
    filtered_words = [w for w in all_words if w not in stop_words]
    
    word_freq = Counter(filtered_words)
    max_freq = max(word_freq.values()) if word_freq else 1
    
    # Normalize frequencies
    for word in word_freq:
        word_freq[word] = word_freq[word] / max_freq
    
    return word_freq


def score_sentences(sentences, word_freq):
    """Score each sentence based on word frequencies."""
    sentence_scores = {}
    
    for sentence in sentences:
        words = tokenize_words(sentence)
        score = sum(word_freq.get(word, 0) for word in words)
        
        if len(words) > 0:
            sentence_scores[sentence] = score / len(words)
        else:
            sentence_scores[sentence] = 0
    
    return sentence_scores


def summarize(text, ratio=0.3):
    """Summarize text by extracting top sentences.
    
    Args:
        text: Input text to summarize
        ratio: Proportion of sentences to keep (0.0 to 1.0)
    
    Returns:
        Summarized text
    """
    text = clean_text(text)
    sentences = tokenize_sentences(text)
    
    if len(sentences) <= 2:
        return text
    
    word_freq = get_word_frequencies(sentences)
    sentence_scores = score_sentences(sentences, word_freq)
    
    # Select top sentences
    num_sentences = max(1, int(len(sentences) * ratio))
    top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]
    
    # Maintain original order
    summary_sentences = sorted(top_sentences, key=lambda x: sentences.index(x[0]))
    summary = '. '.join([s[0] for s in summary_sentences]) + '.'
    
    return summary


if __name__ == "__main__":
    print("Text Summarizer - Frequency-based Extractive Algorithm")
    print("=" * 55)
    text = input("\nEnter text to summarize:\n")
    
    if text.strip():
        summary = summarize(text)
        print("\n" + "=" * 55)
        print("SUMMARY:")
        print("=" * 55)
        print(summary)
    else:
        print("No text provided!")
