"""
Text Summarizer - Extract Important Sentences Using Word Frequency
This script extracts the most important sentences from a paragraph based on word frequency analysis.
"""

import re
from collections import Counter
import string


def preprocess_text(text):
    """
    Clean and preprocess the input text.

    Args:
        text (str): Input text to preprocess

    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def tokenize_sentences(text):
    """
    Split text into sentences.

    Args:
        text (str): Input text

    Returns:
        list: List of sentences
    """
    # Split by sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    # Remove empty sentences and strip whitespace
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences


def calculate_word_frequency(sentences, stop_words=None):
    """
    Calculate word frequency from sentences, excluding stop words.

    Args:
        sentences (list): List of sentences
        stop_words (set): Set of words to exclude from frequency calculation

    Returns:
        Counter: Word frequency counter
    """
    if stop_words is None:
        # Common English stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
            'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
            'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that',
            'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
        }

    words = []
    for sentence in sentences:
        # Convert to lowercase and remove punctuation
        cleaned = sentence.lower().translate(str.maketrans('', '', string.punctuation))
        # Split into words
        sentence_words = cleaned.split()
        # Filter out stop words
        words.extend([word for word in sentence_words if word not in stop_words])

    return Counter(words)


def score_sentences(sentences, word_freq):
    """
    Score each sentence based on the frequency of words it contains.

    Args:
        sentences (list): List of sentences
        word_freq (Counter): Word frequency counter

    Returns:
        list: List of tuples (sentence, score)
    """
    sentence_scores = []

    for sentence in sentences:
        # Convert to lowercase and remove punctuation for scoring
        cleaned = sentence.lower().translate(str.maketrans('', '', string.punctuation))
        words = cleaned.split()

        # Calculate sentence score as sum of word frequencies
        score = sum(word_freq.get(word, 0) for word in words)

        # Normalize by sentence length to avoid bias towards longer sentences
        if len(words) > 0:
            score = score / len(words)

        sentence_scores.append((sentence, score))

    return sentence_scores


def extract_top_sentences(text, num_sentences=3):
    """
    Extract the most important sentences from text based on word frequency.

    Args:
        text (str): Input text
        num_sentences (int): Number of top sentences to extract

    Returns:
        list: List of top sentences in order of importance
    """
    # Preprocess text
    text = preprocess_text(text)

    # Tokenize into sentences
    sentences = tokenize_sentences(text)

    if len(sentences) == 0:
        return []

    # Calculate word frequency
    word_freq = calculate_word_frequency(sentences)

    # Score sentences
    sentence_scores = score_sentences(sentences, word_freq)

    # Sort by score in descending order
    sorted_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)

    # Extract top N sentences
    top_sentences = [sentence for sentence, score in sorted_sentences[:num_sentences]]

    return top_sentences


def main():
    """Main function to demonstrate text summarization."""
    print("=" * 60)
    print("Text Summarizer - Extract Important Sentences")
    print("=" * 60)

    # Get input from user
    print("\nEnter or paste your paragraph (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = " ".join(lines)

    if not text.strip():
        print("\nNo text provided. Exiting.")
        return

    # Get number of sentences to extract
    while True:
        try:
            num_sentences = int(input("\nHow many important sentences to extract? (default: 3): ") or "3")
            if num_sentences > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")

    # Extract top sentences
    top_sentences = extract_top_sentences(text, num_sentences)

    # Display results
    print("\n" + "=" * 60)
    print(f"Top {len(top_sentences)} Most Important Sentences:")
    print("=" * 60)

    for i, sentence in enumerate(top_sentences, 1):
        print(f"\n{i}. {sentence}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
