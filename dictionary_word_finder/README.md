# Dictionary Word Finder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A command-line dictionary tool that fetches word definitions, synonyms, and example sentences using the free Dictionary API. Part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) project collection.

## 🎯 Features

- **Word Definitions**: Get comprehensive definitions with parts of speech
- **Synonyms**: Discover alternative words with similar meanings
- **Example Sentences**: See words used in context
- **Free API**: Uses [dictionaryapi.dev](https://dictionaryapi.dev) - no API key required
- **Error Handling**: Graceful handling of invalid inputs and network issues
- **Clean Output**: Well-formatted, readable results

## 📋 Requirements

- Python 3.6 or higher
- `requests` library

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/Agi-Asi/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/dictionary_word_finder
```

2. Install required dependencies:
```bash
pip install requests
```

## 💻 Usage

Run the script from the command line with a word as an argument:

```bash
python dictionary_word_finder.py <word>
```

### Examples

```bash
# Look up a simple word
python dictionary_word_finder.py hello

# Look up a complex word
python dictionary_word_finder.py serendipity

# Look up a technical term
python dictionary_word_finder.py algorithm
```

## 📖 Sample Output

```
Looking up 'serendipity'...

==================================================
WORD: SERENDIPITY
==================================================

DEFINITIONS:
--------------------
1. [noun] The faculty of making fortunate discoveries by accident
2. [noun] Good luck in making unexpected and fortunate discoveries

SYNONYMS:
--------------------
chance, fortune, luck, fate, destiny

EXAMPLE SENTENCES:
--------------------
1. A fortunate stroke of serendipity brought the two old friends together.
2. The discovery was pure serendipity in the laboratory.

==================================================
```

## 🔧 How It Works

1. **Input Validation**: Checks if the input is a valid English word (letters only)
2. **API Request**: Sends a GET request to [dictionaryapi.dev](https://dictionaryapi.dev)
3. **Data Processing**: Extracts definitions, synonyms, and examples from the JSON response
4. **Output Formatting**: Displays the information in a clean, readable format

## 🌐 API Information

This tool uses the free [Dictionary API](https://dictionaryapi.dev) which:
- Requires no API key
- Has no rate limits for reasonable usage
- Provides comprehensive English word data
- Returns JSON responses with definitions, examples, and more

## 🛠️ Technical Details

- **Language**: Python 3.6+
- **External Libraries**: `requests` for HTTP requests
- **API Endpoint**: `https://api.dictionaryapi.dev/api/v2/entries/en/{word}`
- **Error Handling**: Network timeouts, invalid words, API failures
- **Code Length**: Under 100 lines (excluding comments and docstrings)

## 🤝 Contributing

Contributions are welcome! This project is part of the **100 Lines of Python Code** collection. Please ensure your code:

1. Stays under 100 functional lines
2. Follows Python best practices
3. Includes proper error handling
4. Is well-documented

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 🙋‍♀️ Support

If you have questions or need help:

1. Check the [Issues](https://github.com/sumanth-0/100LinesOfPythonCode/issues) page
2. Create a new issue with the `question` label
3. Provide clear details about your problem

## 📚 Related Projects

Explore other projects in the **100 Lines of Python Code** collection:
- [Main Repository](https://github.com/sumanth-0/100LinesOfPythonCode)
- [All Projects](https://github.com/sumanth-0/100LinesOfPythonCode#projects)

---

**Created for Issue #670** | **Part of 100 Lines of Python Code** | **Free & Open Source** ❤️
