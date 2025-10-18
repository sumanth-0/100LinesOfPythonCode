#!/usr/bin/env python3
"""
Mini Spell Checker - A simple CLI tool to check spelling in text files

This tool compares words in a text file against a word list (dictionary)
and identifies potential spelling errors.

Usage:
    python main.py <text_file> [word_list]
    
If no word list is provided, a default English word list will be used.
"""

import sys
import re
from pathlib import Path
from typing import Set, List, Tuple

# Default word list (common English words)
DEFAULT_WORDS = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
    "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
    "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
    "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
    "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us",
    "is", "are", "was", "were", "been", "being", "has", "had", "having", "does"
}

def load_word_list(file_path: str) -> Set[str]:
    """Load words from a file into a set."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        print(f"Error: Word list file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading word list: {e}")
        sys.exit(1)

def load_text_file(file_path: str) -> str:
    """Load text from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Text file '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading text file: {e}")
        sys.exit(1)

def extract_words(text: str) -> List[Tuple[str, int]]:
    """Extract words from text with their line numbers."""
    words_with_lines = []
    for line_num, line in enumerate(text.split('\n'), 1):
        words = re.findall(r"\b[a-zA-Z]+\b", line)
        for word in words:
            words_with_lines.append((word, line_num))
    return words_with_lines

def check_spelling(words_with_lines: List[Tuple[str, int]], word_list: Set[str]) -> List[Tuple[str, int]]:
    """Check spelling and return misspelled words with line numbers."""
    misspelled = []
    for word, line_num in words_with_lines:
        if word.lower() not in word_list:
            misspelled.append((word, line_num))
    return misspelled

def display_results(misspelled: List[Tuple[str, int]], total_words: int) -> None:
    """Display spell check results."""
    if not misspelled:
        print("\n✓ No spelling errors found!")
        print(f"Total words checked: {total_words}")
    else:
        print(f"\n✗ Found {len(misspelled)} potential spelling error(s):\n")
        current_line = None
        for word, line_num in misspelled:
            if line_num != current_line:
                print(f"\nLine {line_num}:")
                current_line = line_num
            print(f"  - {word}")
        print(f"\nTotal words checked: {total_words}")
        print(f"Misspelled words: {len(misspelled)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <text_file> [word_list]")
        print("\nExample:")
        print("  python main.py document.txt")
        print("  python main.py document.txt dictionary.txt")
        sys.exit(1)
    
    text_file = sys.argv[1]
    word_list_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # Load word list
    if word_list_file:
        print(f"Loading word list from: {word_list_file}")
        word_list = load_word_list(word_list_file)
    else:
        print("Using default English word list")
        word_list = DEFAULT_WORDS
    
    print(f"Checking spelling in: {text_file}")
    
    # Load and process text
    text = load_text_file(text_file)
    words_with_lines = extract_words(text)
    
    # Check spelling
    misspelled = check_spelling(words_with_lines, word_list)
    
    # Display results
    display_results(misspelled, len(words_with_lines))

if __name__ == "__main__":
    main()
