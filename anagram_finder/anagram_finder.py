# Anagram Finder
# Description: Checks if two words or phrases are anagrams of each other.
# Usage: Run and input two strings when prompted.

def is_anagram(str1, str2):
    # Remove spaces and make lowercase
    cleaned1 = ''.join(ch.lower() for ch in str1 if ch.isalpha())
    cleaned2 = ''.join(ch.lower() for ch in str2 if ch.isalpha())

    # Compare sorted characters
    return sorted(cleaned1) == sorted(cleaned2)

if __name__ == "__main__":
    print("🔠 ANAGRAM FINDER 🔠")
    first = input("Enter the first word or phrase: ")
    second = input("Enter the second word or phrase: ")

    if is_anagram(first, second):
        print("✅ They are Anagrams!")
    else:
        print("❌ Not Anagrams.")
