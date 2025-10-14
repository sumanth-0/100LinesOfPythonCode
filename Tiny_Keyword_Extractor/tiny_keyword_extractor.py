"""
Tiny Keyword Extractor
Extracts the top 5-10 keywords from a text file based on frequency, ignoring stopwords.
Uses only Python's built-in libraries - no external dependencies required.
"""

import re
import sys
from collections import Counter

# Common English stopwords to ignore during keyword extraction
STOPWORDS = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'will',
    'with', 'this', 'but', 'they', 'have', 'had', 'what', 'when', 'where',
    'who', 'which', 'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more',
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
    'so', 'than', 'too', 'very', 'can', 'just', 'should', 'now', 'or', 'if', 'i',
    'you', 'we', 'my', 'your', 'our', 'their', 'his', 'her', 'am', 'been', 'being'
}


def extract_keywords(text, top_n=10):
    """
    Extracts top N keywords from text based on frequency.
    
    Args:
        text (str): The input text to analyze
        top_n (int): Number of top keywords to return (default: 10)
        
    Returns:
        list: List of tuples containing (keyword, frequency)
    """
    # Convert to lowercase and extract words (3+ letters, alphabetic only)
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    
    # Filter out stopwords and count frequencies
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Return top N most common words
    return Counter(filtered_words).most_common(top_n)


def read_file(filepath):
    """Reads content from a text file with error handling."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None


def main():
    """Main function to handle file input and display results."""
    print("=" * 60)
    print("Tiny Keyword Extractor")
    print("=" * 60)
    
    # Get filename from command line or user input
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    else:
        filepath = input("\nEnter the path to your text file: ").strip()
        top_n_input = input("How many keywords to extract? (default: 10): ").strip()
        top_n = int(top_n_input) if top_n_input else 10
    
    # Read file and extract keywords
    text = read_file(filepath)
    if text is None:
        return
    
    keywords = extract_keywords(text, top_n)
    
    # Display results
    print(f"\nTop {len(keywords)} Keywords:")
    print("-" * 60)
    for i, (word, count) in enumerate(keywords, 1):
        print(f"{i:2}. {word:<20} (appeared {count} times)")
    print("=" * 60)


if __name__ == "__main__":
    main()