# Grammar Fixer

A simple Python script to enhance basic grammar in text input.

## Features

- Capitalizes sentence starts and the word 'I'
- Adds missing punctuation (periods for statements, question marks for questions)
- Normalizes multiple spaces
- Fixes common contractions (e.g., "dont" → "don't")
- Detects sentence boundaries in unpunctuated text
- Ensures proper spacing after punctuation

## Usage

### Interactive Mode
Navigate to GRAMMAR_FIXER directory
Run the script directly:
```bash
python grammar_fixer.py
```
Enter your text when prompted.

### As a Module
Import the function in your code:
```python
from grammar_fixer import fix_grammar
result = fix_grammar("your text here")
```

## Examples

- Input: `"hello world"`
  - Output: `"Hello world."`

- Input: `"i love coding it makes me happy do you like python"`
  - Output: `"I love coding. It makes me happy. Do you like python?"`

- Input: `"what is your name how are you"`
  - Output: `"What is your name? How are you?"`

## Requirements

- Python 3.x

## Testing

Navigate to GRAMMAR_FIXER directory
Run the test suite:
```bash
python test_grammar.py
```