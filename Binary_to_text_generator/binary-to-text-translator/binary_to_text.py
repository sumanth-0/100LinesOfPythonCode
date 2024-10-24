def binary_to_text(binary_str):
    """
    Converts a binary string into human-readable text.
    
    :param binary_str: A string of binary values separated by spaces.
    :return: The corresponding human-readable text.
    """
    binary_values = binary_str.split()  # Split the binary string by space into individual binary numbers
    ascii_characters = [chr(int(b, 2)) for b in binary_values]  # Convert each binary number to an ASCII character
    return ''.join(ascii_characters)  # Join the ASCII characters into a single string


def text_to_binary(text):
    """
    Converts human-readable text into binary representation.
    
    :param text: A string of human-readable text.
    :return: The corresponding binary string where each character is represented in 8-bit binary.
    """
    binary_representation = ' '.join(format(ord(char), '08b') for char in text)  # Convert each char to its 8-bit binary
    return binary_representation


# Example usage
binary_input = "01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100"
print(f"Input: {binary_input}")

# Convert binary to text
text = binary_to_text(binary_str=binary_input)
print(f"Binary to Text: {text}")

# Convert text back to binary
binary = text_to_binary(text=text)
print(f"Back to Binary: {binary}")

# Check if the converted binary is equal to the original input
print(f"Equal to original input: {binary == binary_input}")
