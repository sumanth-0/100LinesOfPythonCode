import re

def is_palindrome(text):
    """
    Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    input_string = input("Enter a string to check if it's a palindrome: ")
    if is_palindrome(input_string):
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')