# Tiny URL Expander

A Python command-line tool that expands shortened URLs to their full destination. This tool follows URL redirects to reveal the final destination of shortened URLs from services like bit.ly, tinyurl.com, goo.gl, and others.

## Features

- Expands shortened URLs to their final destination
- Supports both `requests` library and `http.client` (stdlib) with automatic fallback
- Follows multiple redirects (up to 10 by default)
- Configurable timeout for network requests
- Simple command-line interface
- Handles both HTTP and HTTPS URLs
- Supports relative and absolute URL redirects

## Requirements

- Python 3.6+
- `requests` library (optional, falls back to stdlib `http.client`)

## Installation

1. Clone this repository or download the script
2. (Optional) Install the requests library for better performance:

```bash
pip install requests
```

## Usage

### Basic Usage

```bash
python tiny_url_expander.py <shortened_url>
```

### Examples

```bash
# Expand a bit.ly URL
python tiny_url_expander.py https://bit.ly/3example

# Expand a tinyurl
python tiny_url_expander.py https://tinyurl.com/example

# With custom timeout (in seconds)
python tiny_url_expander.py https://bit.ly/3example -t 15
```

### Command-Line Arguments

- `url` (required): The shortened URL to expand
- `-t, --timeout` (optional): Request timeout in seconds (default: 10)

### Output Example

```
Expanding: https://bit.ly/3example
Full URL: https://www.example.com/full/destination/path
```

## How It Works

1. The tool sends a HEAD request to the shortened URL
2. It follows HTTP redirects (301, 302, 303, 307, 308 status codes)
3. Continues following redirects until reaching the final destination
4. Returns the full URL after all redirects

## Error Handling

- Network errors are caught and displayed to the user
- Timeout errors show appropriate error messages
- Invalid URLs are handled gracefully

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
