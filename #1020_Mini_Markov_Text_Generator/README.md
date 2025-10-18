# Mini Markov Text Generator

## Description
A Python implementation of a Markov chain text generator that creates random text based on patterns learned from sample text. The generator uses bigrams (2-word sequences) to build a probabilistic model and generate coherent text.

## Features
- **Markov Chain Implementation**: Uses bigrams to build text generation model
- **Multiple Input Options**: 
  - Pre-loaded sample texts
  - User-entered custom text
  - File input capability
- **Text Processing**: Cleans and normalizes input text for better results
- **Configurable Generation**: Adjustable text length and chain order
- **Interactive CLI**: User-friendly command-line interface

## How It Works
1. **Text Analysis**: Breaks input text into word sequences
2. **Chain Building**: Creates a dictionary mapping word pairs to possible next words
3. **Generation**: Randomly walks through the chain to create new text
4. **Output**: Produces coherent text based on learned patterns

## Usage
```bash
python mini_markov_text_generator.py
```

### Options
1. **Use Sample Text**: Choose from pre-loaded examples
2. **Enter Custom Text**: Input your own text for generation
3. **Load from File**: Read text from an external file

## Example
```python
# Sample input:
"Python is a great programming language. Python makes programming fun."

# Possible output:
"Python is a great programming fun and easy. Programming in Python makes programming language."
```

## Technical Details
- **Language**: Python 3
- **Dependencies**: Standard library only (random, re, collections)
- **Chain Order**: 2 (bigrams)
- **Default Output Length**: 30 words

## Code Structure
- `clean_text()`: Preprocesses input text
- `build_markov_chain()`: Creates the Markov chain dictionary
- `generate_text()`: Generates random text from the chain
- `main()`: Handles user interaction and program flow

## Related Issue
Fixes #1020 - Mini Markov Text Generator

## Author
Contribution to 100LinesOfPythonCode repository
