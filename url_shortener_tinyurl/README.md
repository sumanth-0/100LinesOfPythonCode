# URL Shortener using TinyURL API

A simple Python script that shortens long URLs using the TinyURL web API. This tool provides both an interactive command-line interface and functions that can be imported into other Python scripts.

## Features

- ✨ Shorten URLs using TinyURL's free API
- 🔄 Interactive mode for multiple URL shortening
- 💻 Command-line argument support
- 🚀 No API key required
- 🛡️ Comprehensive error handling
- 📦 Can be imported as a module

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. Install the required dependency:

```bash
pip install requests
```

## Usage

### Interactive Mode

Run the script without arguments to enter interactive mode:

```bash
python url_shortener.py
```

You'll be prompted to enter URLs one at a time. Type 'q' to quit.

### Command-Line Mode

Pass the URL as a command-line argument:

```bash
python url_shortener.py https://www.example.com/very/long/url/that/needs/shortening
```

### As a Module

You can also import the functions into your own Python scripts:

```python
from url_shortener import shorten_url, shorten_multiple_urls

# Shorten a single URL
short_url = shorten_url("https://www.example.com/long/url")
print(short_url)

# Shorten multiple URLs
urls = [
    "https://www.example.com/url1",
    "https://www.example.com/url2",
    "https://www.example.com/url3"
]
results = shorten_multiple_urls(urls)
for original, shortened in results.items():
    print(f"{original} -> {shortened}")
```

## Examples

### Example 1: Basic Usage

```bash
$ python url_shortener.py https://github.com/sumanth-0/100LinesOfPythonCode

==================================================
URL Shortener using TinyURL API
==================================================

Original URL: https://github.com/sumanth-0/100LinesOfPythonCode
Shortened URL: https://tinyurl.com/abc123
```

### Example 2: Interactive Mode

```bash
$ python url_shortener.py

==================================================
URL Shortener using TinyURL API
==================================================

Enter 'q' to quit
--------------------------------------------------

Enter URL to shorten: https://www.example.com/very/long/url
Shortened URL: https://tinyurl.com/xyz789

Enter URL to shorten: q
Thanks for using URL Shortener!
```

## How It Works

1. The script takes a long URL as input
2. Adds "https://" prefix if no scheme is provided
3. Sends a request to TinyURL's API endpoint
4. Returns the shortened URL

## Error Handling

The script handles various error scenarios:

- ⚠️ Network connectivity issues
- ⚠️ Invalid URLs
- ⚠️ API timeouts
- ⚠️ Malformed responses

## Notes

- TinyURL is a free service and doesn't require an API key
- The script automatically adds "https://" if you don't include a protocol
- Shortened URLs are permanent and don't expire
- No rate limiting is mentioned in TinyURL's API documentation, but use responsibly

## Alternative APIs

If you want to use a different URL shortening service:

- **Bitly**: Requires an API key but offers analytics and custom short domains
- **Is.gd**: Another free service similar to TinyURL
- **Shrtco.de**: Free service with no API key required

## License

This script is provided as-is for educational purposes as part of the 100 Lines of Python Code project.

## Contributing

Feel free to fork and improve this script! Some ideas for enhancement:

- Add support for custom TinyURL aliases (requires TinyURL account)
- Implement batch processing from a file
- Add URL validation before shortening
- Create a simple GUI interface
