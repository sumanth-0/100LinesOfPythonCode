# Binary to Text Translator

## Description
This Python script converts binary strings into human-readable text and vice versa. It uses ASCII values for each character and supports both directions of conversion.

## Usage
1. To convert binary to text, provide a binary string where each character is represented as 8-bit binary (separated by spaces).
2. To convert text back to binary, provide a string of text, and the script will output the binary representation.

### Example
```python
binary_input = "01001000 01100101 01101100 01101100 01101111 00100000 01010111 01101111 01110010 01101100 01100100"
text = binary_to_text(binary_input)
binary = text_to_binary(text)
