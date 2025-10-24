# Auto Text Formatter

A simple Python script that automatically formats text files by:

1. Cleaning extra spaces
2. Capitalizing the first letter of each sentence
3. Ensuring proper spacing around punctuation marks

## Features

- Removes multiple spaces and replaces them with single spaces
- Capitalizes the first letter of each sentence
- Fixes spacing around punctuation marks (.,!?)
- Supports input and output file specification

## Usage

```bash
python auto_text_formatter.py input.txt [-o output.txt]
```

### Arguments

- `input.txt`: Path to the input text file that needs formatting
- `-o output.txt`: (Optional) Path to save the formatted text. If not specified, the input file will be overwritten

## Example

Input text:

```text
this is a    test.   this is another   sentence!what about this one?    yes,this works too.
```

Output text:

```text
This is a test. This is another sentence! What about this one? Yes, this works too.
```

## Notes

- The script preserves the original text encoding (UTF-8)
- It handles multiple types of sentence-ending punctuation (., !, ?)
- The script will create a backup of your original file if you don't specify an output file
