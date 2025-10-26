MORSE_CODE_CHARACHTERS = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.'
}

REVERSE_MORSE_CODE_CHARACHTERS = {v: k for k, v in MORSE_CODE_CHARACHTERS.items()}

def text_to_morse_code(text):
    morse_code = []
    for char in text.upper():
        if char in MORSE_CODE_CHARACHTERS:
            morse_code.append(MORSE_CODE_CHARACHTERS[char])
        elif char == ' ':
            morse_code.append('/')  # Use '/' to denote space between words
        else
            morse_code.append('#')  # Ignore unsupported characters
    return ' '.join(morse_code)

def morse_code_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_words = []
    for word in words:
        characters = word.split()
        decoded_characters = []
        for char in characters:
            if char in reverse_morse_code:
                decoded_characters.append(reverse_morse_code[char])
            else:
                decoded_characters.append('#')  # Ignore unsupported characters
        decoded_words.append(''.join(decoded_characters))
    return ' '.join(decoded_words)

def main():
    print("Morse Code Converter Test")
    sample_text = "Hello this is me testing my morse code converter function"
    print(f'Text: "{sample_text}"')
    morse = text_to_morse_code(sample_text)
    print(f"Text to Morse: {morse}")
    print("-----")
    print("Now I will convert morse code into text")
    morse_sample_text = "- .... .. ... / .. ... / .- / ... . -. - . -. -.-. . --..-- / .-- .-. .. - - . -. / .. -. / -- --- .-. ... . / -.-. --- -.. . .-.-.-"
    print(f'Morse Code: "{morse_sample_text}"')
    decoded_text = morse_code_to_text(morse_sample_text)
    print(f"Morse converted to Text: {decoded_text}")

if __name__ == "__main__":
    main()