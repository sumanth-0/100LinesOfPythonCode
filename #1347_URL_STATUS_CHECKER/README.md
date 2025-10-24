# URL Checker

A Python utility to check if URLs from a text file are online or broken. The script performs concurrent checks for fast processing and provides detailed status reports.

## Features

- ✅ Concurrent URL checking for improved performance
- 🔍 Validates URL format before checking
- ⚡ Fast HEAD request with GET fallback
- 📊 Real-time progress tracking
- 📝 Detailed summary and optional report file
- ⚙️ Configurable timeout and worker threads
- 🎯 Custom error messages for different exception types

## Status Indicators

The script classifies URLs into the following categories:

- **ONLINE** - URL is accessible (HTTP status < 400)
- **BROKEN** - Connection failed or HTTP error (status ≥ 400)
- **TIMEOUT** - Request exceeded timeout duration
- **INVALID** - Malformed URL format

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install requests
```

## Usage

### Basic Usage

```bash
python url_checker.py <input_file.txt>
```

### Save Detailed Report

```bash
python url_checker.py urls.txt report.txt
```

### Custom Timeout

```bash
python url_checker.py urls.txt --timeout 5
```

### Adjust Concurrent Workers

```bash
python url_checker.py urls.txt --workers 20
```

### Combined Options

```bash
python url_checker.py urls.txt report.txt --timeout 5 --workers 20
```

## Input File Format

Create a text file with one URL per line:

```
https://www.google.com
https://www.github.com
https://example.com/page
https://broken-url-example.com
# Lines starting with # are treated as comments and ignored
```

## Output

### Console Output

The script displays real-time progress:

```
Checking 4 URLs...

[1/4] ONLINE: https://www.google.com
[2/4] ONLINE: https://www.github.com
[3/4] BROKEN: https://broken-url-example.com
[4/4] TIMEOUT: https://slow-server.com

================================================================================
SUMMARY
================================================================================
Total URLs checked: 4
Online: 2
Broken/Timeout: 2
Invalid/Error: 0
================================================================================
```

### Report File (Optional)

When an output file is specified, a detailed report is generated with:

- Timestamp of the check
- Summary statistics
- Grouped URLs by status (BROKEN, TIMEOUT, INVALID, ERROR, ONLINE)
- HTTP status codes (where applicable)
- Detailed error messages

Example report structure:

```
URL Check Report - 2024-10-22 14:30:45
================================================================================

Total URLs checked: 4
Online: 2
Broken/Timeout: 2
Invalid/Error: 0

================================================================================

BROKEN URLs (1):
--------------------------------------------------------------------------------
URL: https://broken-url-example.com
Message: Connection failed

TIMEOUT URLs (1):
--------------------------------------------------------------------------------
URL: https://slow-server.com
Message: Request timed out
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `<input_file.txt>` | Path to file containing URLs (required) | - |
| `[output_report.txt]` | Path to save detailed report (optional) | None |
| `--timeout SECONDS` | Request timeout in seconds | 10 |
| `--workers NUM` | Number of concurrent worker threads | 10 |

## How It Works

1. **URL Validation**: Uses `urllib.parse` to validate URL format
2. **HEAD Request**: Sends a fast HEAD request first to check status
3. **GET Fallback**: If HEAD fails or returns error, tries GET request
4. **Concurrent Processing**: Uses `ThreadPoolExecutor` to check multiple URLs simultaneously
5. **Error Handling**: Catches and categorizes various exceptions (timeout, connection error, redirects)

## Exception Handling

The script handles the following exceptions with custom messages:

- `requests.exceptions.Timeout` - Request timed out
- `requests.exceptions.ConnectionError` - Connection failed
- `requests.exceptions.TooManyRedirects` - Too many redirects
- General exceptions - Displays the specific error message

## Performance Tips

- **Increase workers** for faster checking of large URL lists (e.g., `--workers 50`)
- **Reduce timeout** if you want quicker results and don't mind skipping slow sites (e.g., `--timeout 3`)
- For very large lists (1000+ URLs), consider processing in batches

## Limitations

- Some websites may block automated requests without proper User-Agent headers
- Rate limiting: Checking many URLs from the same domain simultaneously may trigger rate limits
- HEAD requests: Some servers don't properly support HEAD requests
