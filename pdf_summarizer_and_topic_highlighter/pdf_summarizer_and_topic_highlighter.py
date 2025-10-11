#!/usr/bin/env python3
"""
PDF Summarizer & Topic Highlighter
Tool to summarize PDF content and highlight key topics using NLP.
Helpful for students and researchers.
"""

import PyPDF2
from collections import Counter
import re
from typing import List, Tuple
import sys

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text content from a PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

def clean_text(text: str) -> str:
    """Clean and normalize text."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9\s.,!?;:]', '', text)
    return text.strip()

def extract_sentences(text: str) -> List[str]:
    """Split text into sentences."""
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 20]

def get_word_frequencies(text: str) -> Counter:
    """Calculate word frequencies, excluding common stop words."""
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'it', 'its', 'as'}
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    filtered_words = [w for w in words if w not in stop_words]
    return Counter(filtered_words)

def score_sentences(sentences: List[str], word_freq: Counter) -> List[Tuple[str, float]]:
    """Score sentences based on word frequencies."""
    scored_sentences = []
    for sentence in sentences:
        words = re.findall(r'\b[a-z]{3,}\b', sentence.lower())
        score = sum(word_freq[word] for word in words)
        if len(words) > 0:
            score /= len(words)
        scored_sentences.append((sentence, score))
    return sorted(scored_sentences, key=lambda x: x[1], reverse=True)

def generate_summary(text: str, num_sentences: int = 5) -> str:
    """Generate a summary of the text."""
    text = clean_text(text)
    sentences = extract_sentences(text)
    if len(sentences) == 0:
        return "No content to summarize."
    word_freq = get_word_frequencies(text)
    scored = score_sentences(sentences, word_freq)
    summary_sentences = [s[0] for s in scored[:num_sentences]]
    return ' '.join(summary_sentences)

def extract_key_topics(text: str, num_topics: int = 10) -> List[Tuple[str, int]]:
    """Extract key topics (most frequent words) from the text."""
    text = clean_text(text)
    word_freq = get_word_frequencies(text)
    return word_freq.most_common(num_topics)

def main():
    if len(sys.argv) < 2:
        print("Usage: python pdf_summarizer_and_topic_highlighter.py <pdf_file>")
        print("Optional: Add number of summary sentences (default: 5)")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    num_sentences = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    print(f"\n📄 Processing PDF: {pdf_path}\n")
    text = extract_text_from_pdf(pdf_path)
    
    if not text:
        print("Failed to extract text from PDF.")
        sys.exit(1)
    
    print("📝 SUMMARY:")
    print("="*80)
    summary = generate_summary(text, num_sentences)
    print(summary)
    
    print("\n\n🔑 KEY TOPICS:")
    print("="*80)
    topics = extract_key_topics(text, 15)
    for i, (topic, freq) in enumerate(topics, 1):
        print(f"{i:2d}. {topic:20s} (frequency: {freq})")
    
    print("\n" + "="*80)
    print(f"Total words: {len(text.split())}")
    print(f"Total sentences: {len(extract_sentences(text))}")

if __name__ == "__main__":
    main()
