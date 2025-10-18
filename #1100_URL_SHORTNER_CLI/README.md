# URL Shortener CLI

A small, focused Python command-line tool to shorten URLs using the shrtco.de API. Designed to be compact (under 100 lines) and simple to use from a terminal.

## Features

- Shortens a single URL from the command line
- Minimal dependencies (requests)
- Clear output suitable for piping or scripts

## Requirements

- Python 3.7+
- requests

Install requests (or all deps) with:

pip install -r requirements.txt

or

pip install requests

## Installation

1. Clone or copy this repository into a folder.
2. Ensure `requests` is installed (see Requirements).
3. Run the script from the folder containing `url_shortener_cli.py`.

## Usage

Basic usage (positional argument):

python url_shortener_cli.py https://example.com/very/long/url

If the script supports flags (example placeholders — check the script for exact options):

python url_shortener_cli.py --help

or

python url_shortener_cli.py -u https://example.com

## Example

Input:

python url_shortener_cli.py https://docs.google.com/document/d/1Xp9n8Oa4X1Z0Yw7y_W0t2Q1b1L1E2L7fC2T3Y1S4T5F6G7H8J9K0L/edit

Output:

Original URL:
https://docs.google.com/document/d/1Xp9n8Oa4X1Z0Yw7y_W0t2Q1b1L1E2L7fC2T3Y1S4T5F6G7H8J9K0L/edit

Shortened URL:
https://shrtco.de/dl2f7a

## Error handling

- The script will print a clear error message when:
  - the API returns an error,
  - the input URL is missing or malformed,
  - there is a network problem.

Check exit codes or pipe the output to other tools if you need programmatic handling.

## Notes

- This tool uses the public shrtco.de API. Review their terms before using it in production.
- The CLI is intentionally compact — if you want more features (batch shortening, clipboard copy, JSON output), consider extending the script.

## Contributing

Ideas, fixes, or improvements are welcome via pull requests or issues.

## License

Specify your project license here (e.g., MIT). Replace this line with the actual license text or a link.

<!-- ...existing code... -->