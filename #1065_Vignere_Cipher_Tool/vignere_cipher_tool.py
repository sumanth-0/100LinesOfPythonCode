import string

def vigenere_cipher(text, key, mode='encrypt'):
    """
    Encrypts or decrypts a message using the Vigenère cipher.

    Args:
        text (str): The message to encrypt or decrypt.
        key (str): The keyword for the cipher.
        mode (str): 'encrypt' to encrypt, 'decrypt' to decrypt.

    Returns:
        str: The resulting encrypted or decrypted message.
    """
    result = []
    key_index = 0
    # Ensure key is uppercase for consistent calculations
    key = key.upper()
    # Create a mapping for A-Z to 0-25
    alphabet = string.ascii_uppercase
    alpha_map = {char: i for i, char in enumerate(alphabet)}
    num_map = {i: char for i, char in enumerate(alphabet)}

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_upper = char.upper()

            # Get numeric value of current character and key character
            char_num = alpha_map[char_upper]
            key_char = key[key_index % len(key)]
            key_num = alpha_map[key_char]

            if mode == 'encrypt':
                # (P + K) mod 26
                new_char_num = (char_num + key_num) % 26
            elif mode == 'decrypt':
                # (C - K) mod 26
                new_char_num = (char_num - key_num + 26) % 26
            else:
                raise ValueError("Mode must be 'encrypt' or 'decrypt'")

            # Convert back to character, preserving original case
            new_char = num_map[new_char_num]
            result.append(new_char if is_upper else new_char.lower())

            # Move to the next key character only if an alphabet character was processed
            key_index += 1
        else:
            # Non-alphabetic characters are added directly
            result.append(char)

    return "".join(result)

# --- Example Usage ---
if __name__ == "__main__":
    message = "Hello, World! This is a secret message."
    keyword = "PYTHON"

    print(f"Original Message: {message}")
    print(f"Keyword: {keyword}")

    # Encrypt the message
    encrypted_message = vigenere_cipher(message, keyword, mode='encrypt')
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the message
    decrypted_message = vigenere_cipher(encrypted_message, keyword, mode='decrypt')
    print(f"Decrypted Message: {decrypted_message}")

    # Test with a different message and keyword
    test_msg = "Cryptography is fun."
    test_key = "CIPHER"
    enc_test = vigenere_cipher(test_msg, test_key, 'encrypt')
    dec_test = vigenere_cipher(enc_test, test_key, 'decrypt')
    print(f"\nTest Message: {test_msg}")
    print(f"Test Keyword: {test_key}")
    print(f"Encrypted Test: {enc_test}")
    print(f"Decrypted Test: {dec_test}")