# Morse Code Translator

A command-line interface (CLI) tool for translating between Morse code and plain text.

## Features

- **Encode**: Convert plain text to Morse code
- **Decode**: Convert Morse code back to plain text
- **Complete Dictionary**: Supports letters (A-Z), numbers (0-9), and special characters
- **Input Validation**: Handles invalid characters gracefully
- **Lightweight**: Under 100 lines of Python code

## Installation

No installation required! Just make sure you have Python 3.6+ installed on your system.

## Usage

### Encoding Text to Morse Code

```bash
python morse_code_translator.py encode "Hello World"
```

Output:
```
Text: Hello World
Morse: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

### Decoding Morse Code to Text

```bash
python morse_code_translator.py decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
```

Output:
```
Morse: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Text: HELLO WORLD
```

## Morse Code Reference

### Letters
- A: .-    B: -...  C: -.-.  D: -..   E: .
- F: ..-. G: --.   H: ....  I: ..    J: .---
- K: -.-  L: .-..  M: --    N: -.    O: ---
- P: .--. Q: --.-  R: .-.   S: ...   T: -
- U: ..-  V: ...-  W: .--   X: -..-  Y: -.--
- Z: --..

### Numbers
- 0: ----- 1: .---- 2: ..--- 3: ...-- 4: ....-
- 5: ..... 6: -.... 7: --... 8: ---.. 9: ----.

### Special Characters
- Period: .-.-.-    Comma: --..--    Question: ..--..
- Apostrophe: .----. Exclamation: -.-.-- Slash: -..-.
- Parentheses: --.--., -.--.-
- Space: / (forward slash)

## Notes

- In Morse code, letters/characters are separated by spaces
- Words are separated by ` / ` (space-slash-space)
- The decoder is case-insensitive
- Unknown characters are replaced with `?` during decoding

## Examples

```bash
# Encode a simple message
python morse_code_translator.py encode "SOS"

# Decode an emergency signal
python morse_code_translator.py decode "... --- ..."

# Encode with numbers
python morse_code_translator.py encode "Call 911"

# Multi-word encoding
python morse_code_translator.py encode "Good morning"
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the MIT License.
