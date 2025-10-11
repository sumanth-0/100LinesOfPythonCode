#!/usr/bin/env python3
"""
Morse Code Translator
A CLI tool for translating between Morse code and plain text.
"""

import sys
import argparse

# Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# Reverse dictionary for decoding
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


def text_to_morse(text):
    """
    Convert plain text to Morse code.
    
    Args:
        text: String to convert
    
    Returns:
        Morse code string
    """
    morse = []
    for char in text.upper():
        if char in MORSE_CODE:
            morse.append(MORSE_CODE[char])
        elif char == ' ':
            morse.append('/')
    return ' '.join(morse)


def morse_to_text(morse):
    """
    Convert Morse code to plain text.
    
    Args:
        morse: Morse code string (use / for spaces)
    
    Returns:
        Plain text string
    """
    words = morse.split(' / ')
    decoded = []
    
    for word in words:
        letters = word.split(' ')
        decoded_word = ''
        for letter in letters:
            if letter in REVERSE_MORSE:
                decoded_word += REVERSE_MORSE[letter]
            elif letter:
                decoded_word += '?'
        decoded.append(decoded_word)
    
    return ' '.join(decoded)


def main():
    parser = argparse.ArgumentParser(
        description='Morse Code Translator - Convert between text and Morse code'
    )
    parser.add_argument(
        'mode',
        choices=['encode', 'decode'],
        help='Operation mode: encode (text to Morse) or decode (Morse to text)'
    )
    parser.add_argument(
        'input',
        nargs='+',
        help='Text or Morse code to translate'
    )
    
    args = parser.parse_args()
    input_text = ' '.join(args.input)
    
    if args.mode == 'encode':
        result = text_to_morse(input_text)
        print(f"Text: {input_text}")
        print(f"Morse: {result}")
    elif args.mode == 'decode':
        result = morse_to_text(input_text)
        print(f"Morse: {input_text}")
        print(f"Text: {result}")


if __name__ == '__main__':
    main()
