def caesar_cipher(text, shift, mode='encode'):
    """
    Encode or decode text using Caesar cipher.
    
    :param text: The input text to be processed
    :param shift: The number of positions to shift (can be positive or negative)
    :param mode: 'encode' or 'decode'
    :return: The processed text
    """
    result = ""
    
    # Adjust shift for decoding
    if mode == 'decode':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine the ASCII offset based on case
            ascii_offset = 65 if char.isupper() else 97
            
            # Apply the shift and wrap around the alphabet
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            
            result += shifted_char
        else:
            # Preserve non-alphabetic characters
            result += char
    
    return result

def main():
    while True:
        mode = input("Enter mode (encode/decode) or 'q' to quit: ").lower()
        
        if mode == 'q':
            break
        
        if mode not in ['encode', 'decode']:
            print("Invalid mode. Please enter 'encode' or 'decode'.")
            continue
        
        text = input("Enter the text: ")
        
        while True:
            try:
                shift = int(input("Enter the shift value (integer): "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")
        print()

if __name__ == "__main__":
    main()

