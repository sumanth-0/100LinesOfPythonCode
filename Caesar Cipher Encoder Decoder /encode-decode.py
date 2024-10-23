def caesar_cipher(text, shift, encode=True):
    """Encode or decode a text using a Caesar cipher.

    Args:
        text (str): The input text to be encoded or decoded.
        shift (int): The number of positions to shift the letters.
        encode (bool): True for encoding, False for decoding.

    Returns:
        str: The encoded or decoded text.
    """
    result = ""
    
    # Normalize the shift value
    shift = shift % 26
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Shift the character
            shifted_char = chr((ord(char) - ascii_offset + (shift if encode else -shift)) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char  # Non-alphabetical characters remain unchanged
            
    return result

def main():
    print("Welcome to the Caesar Cipher Encoder/Decoder!")
    choice = input("Would you like to (E)ncode or (D)ecode? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' or 'D'.")
        return
    
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (0-25): "))
    
    if choice == 'E':
        encoded_text = caesar_cipher(text, shift, encode=True)
        print(f"Encoded Text: {encoded_text}")
    else:
        decoded_text = caesar_cipher(text, shift, encode=False)
        print(f"Decoded Text: {decoded_text}")

if __name__ == "__main__":
    main()
