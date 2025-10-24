# Palindrome Checker

This Python script (`palindrome_check.py`) reads sentences from a text file and checks if each sentence is a palindrome, ignoring spaces and punctuation.

## Features
- Cleans sentences by removing spaces and punctuation.
- Checks for palindromes case-insensitively.
- Reads sentences from a `.txt` file.

## Usage
1. Ensure you have a text file, for example `input_p.txt`, containing sentences to check.
2. Place `palindrome_check.py` and your text file in the same directory.
3. Run the script using Python:

```bash
python palindrome_check.py
```

The script will output whether each line in the file is a palindrome.

## Example Input File (`input_p.txt`)
```
A man, a plan, a canal, Panama!
Hello World
Madam In Eden, I'm Adam
```

## Example Output
```
Line 1 is a palindrome
Line 2 is NOT a palindrome
Line 3 is a palindrome
```

