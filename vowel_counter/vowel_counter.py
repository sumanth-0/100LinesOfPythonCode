# Vowel Counter
# Description: Counts total vowels and occurrences of each vowel in a given text.
# Usage: Run the script and enter any sentence or word.

def count_vowels(text):
    vowels = "aeiou"
    text = text.lower()
    counts = {v: text.count(v) for v in vowels}
    total = sum(counts.values())
    return total, counts

if __name__ == "__main__":
    print("🔤 VOWEL COUNTER 🔤")
    user_input = input("Enter a word, phrase, or sentence: ")
    total_vowels, vowel_counts = count_vowels(user_input)

    print(f"\nTotal vowels: {total_vowels}")
    for v, c in vowel_counts.items():
        print(f"{v.upper()}: {c}")
