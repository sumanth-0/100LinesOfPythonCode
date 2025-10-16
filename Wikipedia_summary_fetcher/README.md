# Wikipedia Summary Fetcher 📚

Get a one-line summary for any topic using the Wikipedia API.

## 🎯 What This Script Does

This Python script fetches concise summaries from Wikipedia using the official Wikipedia REST API. It's a simple, lightweight tool that requires no external dependencies—just Python's built-in libraries!

## ✨ Features

- **No External Dependencies**: Uses only Python's standard library (`urllib` and `json`)
- **Two Usage Modes**: Command-line arguments or interactive input
- **Error Handling**: Comprehensive error handling for network issues, invalid topics, and API errors
- **Clean Output**: Formatted, easy-to-read console output
- **URL-Safe**: Properly handles topics with spaces and special characters

## 🚀 Usage

### Method 1: Command Line Arguments
```bash
python wikipedia_summary_fetcher.py Python programming
```

### Method 2: Interactive Mode
```bash
python wikipedia_summary_fetcher.py
```
Then enter your topic when prompted.

## 💡 Examples

```bash
# Single word topic
python wikipedia_summary_fetcher.py Python

# Multi-word topic
python wikipedia_summary_fetcher.py Machine Learning

# Complex topic
python wikipedia_summary_fetcher.py Albert Einstein
```

## 📋 Sample Output

```
============================================================
Wikipedia Summary Fetcher
============================================================

Searching for: Python
------------------------------------------------------------

Python is a high-level, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use 
of significant indentation.

============================================================
```

## 🛠️ How It Works

1. Takes a topic as input (either via command line or user prompt)
2. Encodes the topic for URL safety
3. Makes an API request to Wikipedia's REST API
4. Parses the JSON response to extract the summary
5. Displays the result with proper formatting

## ⚠️ Error Handling

The script handles various error scenarios:
- **404 Errors**: Topic not found on Wikipedia
- **Network Errors**: Connection timeouts or failures
- **JSON Parsing Errors**: Invalid API responses
- **Invalid Input**: Empty or malformed topics

## 🤝 Contributing

Issue #776 - Wikipedia Summary Fetcher

Feel free to improve this script by:
- Adding support for other Wikipedia language editions
- Implementing caching for frequently searched topics
- Adding more detailed output options

## 📜 License

This script uses the Wikipedia API, which provides data under Creative Commons licenses. Make sure to comply with Wikipedia's terms of service when using this tool.
