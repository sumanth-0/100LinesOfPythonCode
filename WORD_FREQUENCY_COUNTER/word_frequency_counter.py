from collections import Counter   # Used for counting word frequencies efficiently
import re                         # Used for regular expressions to clean text

def word_frequency(text):
    """Returns a dictionary of word frequencies in the given text."""
    # Convert the text to lowercase and extract only alphabetic words using regex
    # \b[a-zA-Z]+\b matches sequences of letters (words) while ignoring numbers/punctuation
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    # Count how many times each word appears
    return Counter(words)

def main():
    print("=== Word Frequency Counter ===")
    print("Type or paste your text below (press Enter twice to finish):\n")
    
    # Store user-entered lines of text
    lines = []
    
    # Keep reading lines until the user presses Enter on an empty line
    while True:
        line = input()
        if line.strip() == "":     # Empty line indicates the end of input
            break
        lines.append(line)
    
    # Join all lines into a single text string
    text = " ".join(lines)
    
    # Check if text is empty (user didn’t enter anything)
    if not text.strip():
        print("No text entered. Exiting...")
        return

    # Get word frequency dictionary
    freq = word_frequency(text)
    
    # Display results in descending order of frequency (then alphabetically)
    print("\nWord Frequency Results:\n")
    for word, count in sorted(freq.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word:<15} : {count}")  # Left-align word, then print its count

# Run the program when executed directly
if __name__ == "__main__":
    main()
