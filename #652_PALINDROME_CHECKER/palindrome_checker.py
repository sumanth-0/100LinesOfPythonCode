import string

def is_palindrome(sentence: str) -> bool:
    """
    Check if a given sentence is a palindrome.
    Ignores spaces, punctuation, and case sensitivity.
    """
    # Remove spaces and punctuation, and convert to lowercase
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    return cleaned == cleaned[::-1]


def main():
    print("=== Palindrome Checker ===")
    sentence = input("Enter a sentence: ").strip()
    if is_palindrome(sentence):
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")


if __name__ == "__main__":
    main()
