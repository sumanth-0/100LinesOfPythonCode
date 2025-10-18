import random
import re
from collections import defaultdict

def clean_text(text):
    """
    Clean and prepare text for processing.
    Remove extra whitespace and normalize text.
    """
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def build_markov_chain(text, order=2):
    """
    Build a Markov chain from the input text.
    order: the number of words used as the key (default: 2 for bigrams)
    """
    words = text.split()
    if len(words) < order + 1:
        return None, None
    
    chain = defaultdict(list)
    
    for i in range(len(words) - order):
        key = tuple(words[i:i + order])
        next_word = words[i + order]
        chain[key].append(next_word)
    
    return chain, words

def generate_text(chain, words, length=50, order=2):
    """
    Generate text using the Markov chain.
    length: number of words to generate
    """
    if not chain or not words:
        return "Not enough text to generate from."
    
    # Start with a random key from the chain
    current_key = random.choice(list(chain.keys()))
    result = list(current_key)
    
    for _ in range(length - order):
        if current_key not in chain:
            break
        
        next_word = random.choice(chain[current_key])
        result.append(next_word)
        
        current_key = tuple(result[-order:])
    
    return ' '.join(result)

def main():
    print("=" * 50)
    print("Mini Markov Text Generator")
    print("=" * 50)
    print()
    
    # Sample text for demonstration
    sample_texts = [
        "The quick brown fox jumps over the lazy dog. The dog was not amused by the fox.",
        "Python is a great programming language. Python makes programming fun and easy. Programming in Python is productive.",
        "Machine learning is the future. The future of technology is machine learning and artificial intelligence."
    ]
    
    print("Choose an option:")
    print("1. Use sample text")
    print("2. Enter your own text")
    print("3. Load text from file")
    
    choice = input("\nEnter your choice (1-3): ").strip()
    
    if choice == '1':
        print("\nSelect a sample text:")
        for i, text in enumerate(sample_texts, 1):
            print(f"{i}. {text[:50]}...")
        
        sample_choice = int(input("\nEnter sample number: ")) - 1
        if 0 <= sample_choice < len(sample_texts):
            input_text = sample_texts[sample_choice]
        else:
            print("Invalid choice. Using first sample.")
            input_text = sample_texts[0]
    
    elif choice == '2':
        print("\nEnter your text (press Enter twice when done):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        input_text = ' '.join(lines)
    
    else:
        print("Invalid choice. Using first sample text.")
        input_text = sample_texts[0]
    
    # Clean the input text
    cleaned_text = clean_text(input_text)
    
    # Get Markov chain order
    order = 2  # Default to bigrams
    
    # Build the Markov chain
    chain, words = build_markov_chain(cleaned_text, order)
    
    if chain is None:
        print("\nError: Text is too short to generate from.")
        return
    
    # Generate text
    length = 30  # Default length
    generated = generate_text(chain, words, length, order)
    
    print("\n" + "=" * 50)
    print("Generated Text:")
    print("=" * 50)
    print(generated)
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()
