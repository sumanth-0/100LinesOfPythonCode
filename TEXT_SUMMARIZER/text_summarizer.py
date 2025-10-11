"""
Text Summarizer using Word Frequency Analysis
Extracts the most important sentences from text based on word frequency scoring.
"""

import re
from collections import Counter
import string

def get_stop_words():
    """Return common English stop words."""
    return {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
            'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'will', 'with',
            'this', 'but', 'they', 'have', 'had', 'what', 'when', 'where', 'who', 'which',
            'why', 'how', 'or', 'so', 'can', 'all', 'if', 'about', 'than', 'been', 'there'}

def tokenize_words(text):
    """Convert text to lowercase words without punctuation."""
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    return text.split()

def calculate_word_frequencies(sentences, stop_words):
    """Calculate normalized frequency of important words."""
    all_words = []
    for sentence in sentences:
        words = [w for w in tokenize_words(sentence) if w not in stop_words and len(w) > 2]
        all_words.extend(words)
    
    word_freq = Counter(all_words)
    if word_freq:
        max_freq = max(word_freq.values())
        word_freq = {word: freq / max_freq for word, freq in word_freq.items()}
    return word_freq

def score_sentences(sentences, word_freq, stop_words):
    """Score each sentence based on average word frequency."""
    scores = {}
    for i, sentence in enumerate(sentences):
        words = [w for w in tokenize_words(sentence) if w not in stop_words and w in word_freq]
        scores[i] = sum(word_freq[w] for w in words) / len(words) if words else 0
    return scores

def summarize_text(text, summary_ratio=0.3):
    """
    Summarize text by selecting top sentences based on word frequency.
    
    Args:
        text: Input text to summarize
        summary_ratio: Proportion of sentences to keep (0.0 to 1.0)
    
    Returns:
        Summarized text as a string
    """
    # Clean and split into sentences
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    
    if len(sentences) <= 1:
        return text
    
    # Calculate number of sentences to keep
    num_sentences = max(1, int(len(sentences) * summary_ratio))
    
    # Get stop words and calculate frequencies
    stop_words = get_stop_words()
    word_freq = calculate_word_frequencies(sentences, stop_words)
    
    # Score and select top sentences
    sentence_scores = score_sentences(sentences, word_freq, stop_words)
    top_indices = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    top_indices.sort()  # Maintain original order
    
    # Build and return summary
    return '. '.join([sentences[i] for i in top_indices]) + '.'

def main():
    """Interactive text summarizer."""
    print("=" * 60 + "\nTEXT SUMMARIZER - Word Frequency Analysis\n" + "=" * 60 +
          "\nType 'quit' to exit | Press Ctrl+C to force quit\n")
    try:
        while True:
            user_text = input("Your text: ").strip()
            if user_text.lower() in ['quit', 'exit', 'q']:
                print("\nThank you for using Text Summarizer!")
                break
            if not user_text:
                print("Please enter some text.")
                continue
            ratio_input = input("Summary ratio (0.1-1.0, default 0.3): ").strip()
            try:
                ratio = float(ratio_input) if ratio_input else 0.3
                ratio = max(0.1, min(1.0, ratio))
            except ValueError:
                ratio = 0.3
            print(f"\nSummary ({int(ratio*100)}%):\n" + "-" * 60)
            print(summarize_text(user_text, ratio) + "\n")
    except KeyboardInterrupt:
        print("\n\nExiting... Goodbye!")
if __name__ == "__main__":
    main()