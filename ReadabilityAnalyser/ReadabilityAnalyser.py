import re
import sys

def count_sentences(text):
    """Count sentences using common terminators."""
    return len(re.findall(r'[.!?]+', text))

def count_words(text):
    """Count words by splitting on whitespace."""
    return len(re.findall(r'\b\w+\b', text))

def count_syllables(word):
    """Simple syllable counter based on vowels."""
    word = word.lower()
    vowels = 'aeiouy'
    count = 0
    prev_char = ''
    for char in word:
        if char in vowels and prev_char not in vowels:
            count += 1
        prev_char = char
    return max(1, count)  # At least 1 syllable

def total_syllables(text):
    """Count total syllables in text."""
    words = re.findall(r'\b\w+\b', text.lower())
    return sum(count_syllables(word) for word in words)

def flesch_reading_ease(text):
    """Calculate Flesch Reading Ease score."""
    sentences = count_sentences(text)
    words = count_words(text)
    syllables = total_syllables(text)
    if sentences == 0 or words == 0:
        return 0
    asl = words / sentences
    asw = syllables / words
    return 206.835 - 1.015 * asl - 84.6 * asw

def flesch_kincaid_grade(text):
    """Calculate Flesch-Kincaid Grade Level."""
    sentences = count_sentences(text)
    words = count_words(text)
    syllables = total_syllables(text)
    if sentences == 0 or words == 0:
        return 0
    asl = words / sentences
    asw = syllables / words
    return 0.39 * asl + 11.8 * asw - 15.59

def gunning_fog_index(text):
    """Calculate Gunning Fog Index."""
    sentences = count_sentences(text)
    words = count_words(text)
    complex_words = sum(1 for word in re.findall(r'\b\w+\b', text.lower())
                        if count_syllables(word) >= 3)
    if sentences == 0 or words == 0:
        return 0
    asl = words / sentences
    pcw = (complex_words / words) * 100
    return 0.4 * (asl + pcw)

def analyze_readability(filename):
    """Analyze readability from file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    text = re.sub(r'\s+', ' ', text.strip())  # Normalize whitespace
    if not text:
        print("File is empty.")
        return
    
    fre = flesch_reading_ease(text)
    fkg = flesch_kincaid_grade(text)
    gfi = gunning_fog_index(text)
    
    print(f"Readability Scores for '{filename}':")
    print(f"Flesch Reading Ease: {fre:.2f} (higher = easier)")
    print(f"Flesch-Kincaid Grade: {fkg:.2f}")
    print(f"Gunning Fog Index: {gfi:.2f}")

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter text file path: ").strip()
    if not filename:
        print("No file provided.")
        return
    analyze_readability(filename)

if __name__ == "__main__":
    main()
