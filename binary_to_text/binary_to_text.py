binary_to_text = lambda binary_str: ''.join([chr(int(b, 2)) for b in binary_str.split()])

# Example usage
binary_string = '01001000 01100101 01101100 01101100 01101111'  # "Hello" in binary
text = binary_to_text(binary_string)
print(text)
