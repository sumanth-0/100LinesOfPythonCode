# URL Shortener CLI

A powerful command-line interface tool for shortening URLs using both API-based and hash-based methods. This tool provides a flexible way to shorten long URLs and manage your shortened URL history.

## Features

- **Dual Shortening Methods**:
  - **API-based**: Uses is.gd API for creating publicly accessible short URLs
  - **Hash-based**: Generates local hash codes for URL mapping

- **URL History**: Automatically tracks all shortened URLs with timestamps

- **Custom Short Codes**: Create personalized short codes for your URLs (API method)

- **URL Expansion**: Retrieve original URLs from hash-based short codes

- **Configurable Hash Length**: Customize the length of hash-based short codes

- **Persistent Storage**: All URL mappings are saved locally for future reference

- **URL Validation**: Ensures only valid URLs are processed

- **User-friendly CLI**: Simple and intuitive command-line interface with comprehensive help

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. Clone the repository or download the script:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/url_shortener_cli
```

2. Install required dependencies:
```bash
pip install requests
```

3. Make the script executable (optional, for Unix-based systems):
```bash
chmod +x url_shortener_cli.py
```

## Usage

### Basic Syntax

```bash
python url_shortener_cli.py [OPTIONS]
```

### Command-Line Options

| Option | Description |
|--------|-------------|
| `-u, --url URL` | URL to shorten |
| `-m, --method {api,hash}` | Shortening method (default: api) |
| `-c, --custom CODE` | Custom short code (API method only) |
| `-e, --expand CODE` | Expand hash-based short code to original URL |
| `-l, --length N` | Length of hash-based short code (default: 8) |
| `--history` | Show URL shortening history |
| `-n, --number N` | Number of history entries to show (default: 10) |
| `-h, --help` | Show help message and exit |

## Examples

### 1. Shorten a URL using API (default method)

```bash
python url_shortener_cli.py -u https://example.com/very/long/url/path
```

**Output:**
```
Original URL: https://example.com/very/long/url/path
Short URL: https://is.gd/abc123
```

### 2. Shorten a URL with a custom short code

```bash
python url_shortener_cli.py -u https://example.com -c mylink
```

**Output:**
```
Original URL: https://example.com
Short URL: https://is.gd/mylink
```

### 3. Shorten a URL using hash-based method

```bash
python url_shortener_cli.py -u https://example.com/long/url -m hash
```

**Output:**
```
Original URL: https://example.com/long/url
Short Code: 8f3b4a9c

Note: This is a hash-based code. Use --expand to retrieve the original URL.
```

### 4. Shorten a URL with custom hash length

```bash
python url_shortener_cli.py -u https://example.com -m hash -l 6
```

**Output:**
```
Original URL: https://example.com
Short Code: 8f3b4a

Note: This is a hash-based code. Use --expand to retrieve the original URL.
```

### 5. Expand a hash-based short code

```bash
python url_shortener_cli.py -e 8f3b4a9c
```

**Output:**
```
Original URL: https://example.com/long/url
```

### 6. View URL shortening history

```bash
python url_shortener_cli.py --history
```

**Output:**
```
Showing last 10 entries:

Method               Original URL                                       Short URL/Code                
----------------------------------------------------------------------------------------------------
api                  https://example.com/very/long/url/path...          https://is.gd/abc123          
hash                 https://example.com/long/url...                    8f3b4a9c                      
```

### 7. View more history entries

```bash
python url_shortener_cli.py --history -n 20
```

### 8. Get help

```bash
python url_shortener_cli.py -h
```

## Configuration

The tool automatically creates a configuration directory in your home folder:
- **Location**: `~/.url_shortener/`
- **History File**: `~/.url_shortener/history.json`

All URL shortening operations are saved to the history file for future reference.

## How It Works

### API-Based Method
1. Sends the URL to the is.gd API
2. Receives a publicly accessible short URL
3. Stores the mapping in local history
4. Returns the short URL that can be shared with anyone

### Hash-Based Method
1. Generates a SHA-256 hash of the URL
2. Takes the first N characters as the short code
3. Stores the mapping locally
4. Returns the short code (requires the tool to expand)

## Error Handling

The tool includes comprehensive error handling for:
- Invalid URLs
- Network failures
- API errors
- File I/O errors
- Invalid short codes

## Dependencies

- **requests**: For making HTTP requests to the is.gd API
- **hashlib**: For generating hash-based short codes (built-in)
- **json**: For storing and loading history (built-in)
- **argparse**: For command-line argument parsing (built-in)

## Limitations

- **API Method**: Requires internet connection and is subject to is.gd API rate limits
- **Hash Method**: Short codes only work locally and require the tool to expand
- **Custom Codes**: Must be unique and available on is.gd

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is part of the 100LinesOfPythonCode repository.

## Author

Created for issue #991 in the 100LinesOfPythonCode project.

## Troubleshooting

### "Invalid URL" Error
Make sure your URL includes the protocol (http:// or https://)

```bash
# Wrong
python url_shortener_cli.py -u example.com

# Correct
python url_shortener_cli.py -u https://example.com
```

### Network Error
Check your internet connection if using the API method. For offline use, try the hash-based method.

### Permission Denied
Ensure the script has write permissions to create the `~/.url_shortener/` directory.

## Future Enhancements

- Support for additional URL shortening APIs
- QR code generation for shortened URLs
- Batch URL shortening
- URL analytics and statistics
- Export/import history functionality
