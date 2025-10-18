# Mini Spell Checker

## Description
A simple command-line tool to check spelling in text files against a word list (dictionary). It identifies potential spelling errors and reports them with line numbers.

## Features
- ✅ Check text files against custom or default word list
- ✅ Report misspelled words with their line numbers
- ✅ Simple and intuitive CLI interface
- ✅ Supports custom dictionary files
- ✅ Default English word list included

## Installation
No additional dependencies required! Uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/1015_mini_spell_checker
```

## Usage

### Basic usage with default word list:
```bash
python main.py document.txt
```

### Using a custom dictionary file:
```bash
python main.py document.txt custom_dictionary.txt
```

### Example:
```bash
# Create a test file
echo "This is a test documnt with som misspeled words." > test.txt

# Run the spell checker
python main.py test.txt
```

## Output Example
```
Using default English word list
Checking spelling in: test.txt

✗ Found 3 potential spelling error(s):

Line 1:
  - documnt
  - som
  - misspeled

Total words checked: 8
Misspelled words: 3
```

## How It Works
1. Loads a word list (custom or default) into memory
2. Reads the text file and extracts all words
3. Compares each word against the dictionary (case-insensitive)
4. Reports any words not found in the dictionary with their line numbers

## File Format
- **Text files**: Plain text files (.txt) with any content
- **Dictionary files**: One word per line, case-insensitive

## Contributing
Contributions are welcome! Please follow the repository's CONTRIBUTING.md guidelines.

## License
This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

## Author
Created for Issue #1015 - Mini Spell Checker
