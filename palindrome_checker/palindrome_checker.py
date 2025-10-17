def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    user_input = input("Enter a word, phrase, or number: ")
    if is_palindrome(user_input):
        print("Palindrome ✅")
    else:
        print("Not a Palindrome ❌")

