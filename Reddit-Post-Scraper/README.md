# Reddit Post Scraper

A command-line tool to fetch and display the latest posts from any Reddit subreddit.

## Description

This Python script fetches the top posts from a user-supplied Reddit subreddit using Reddit's public JSON API. It displays post titles, authors, upvotes, comments count, timestamps, and URLs in a formatted manner.

## Features

- Fetch hot posts from any public subreddit
- Display post information including:
  - Title
  - Author
  - Upvotes count
  - Comments count
  - Posted timestamp
  - Post URL
- Customizable number of posts to fetch
- Interactive CLI interface
- Command-line arguments support
- No API key required (uses Reddit's public JSON API)

## Prerequisites

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository or download the script

2. Install required dependencies:
```bash
pip install requests
```

## Usage

### Interactive Mode

Run the script without arguments for interactive prompts:

```bash
python reddit_post_scraper.py
```

You will be prompted to:
1. Enter the subreddit name
2. Specify the number of posts to fetch (default: 10)

### Command-line Mode

Provide subreddit name and optional post limit as arguments:

```bash
python reddit_post_scraper.py <subreddit> [limit]
```

Examples:

```bash
# Fetch 10 posts from r/python
python reddit_post_scraper.py python

# Fetch 25 posts from r/programming
python reddit_post_scraper.py programming 25

# Fetch 5 posts from r/learnpython
python reddit_post_scraper.py learnpython 5
```

## Sample Output

```
================================================================================
                             Reddit Post Scraper                              
================================================================================

Fetching posts from r/python...

================================================================================
Found 10 posts
================================================================================

[1] New Python Feature Released
    Author: python_dev
    Upvotes: 1234 | Comments: 56
    Posted: 2025-10-11 10:30:45
    URL: https://www.reddit.com/r/python/comments/...
    ----------------------------------------------------------------------------

[2] Python Tips and Tricks
    Author: code_master
    Upvotes: 987 | Comments: 43
    Posted: 2025-10-11 09:15:22
    URL: https://www.reddit.com/r/python/comments/...
    ----------------------------------------------------------------------------
```

## Technical Details

- Uses Reddit's public JSON API (no authentication required)
- User-Agent header is set to identify the scraper
- Handles errors gracefully with informative messages
- Timestamps are converted from Unix epoch to readable format
- Under 100 lines of Python code

## Error Handling

The script handles various error scenarios:
- Invalid subreddit names
- Network connectivity issues
- API response parsing errors
- Empty or malformed user input

## Limitations

- Only fetches posts from public subreddits
- Rate-limited by Reddit's API (recommended to add delays between requests if fetching frequently)
- Maximum posts per request may vary based on Reddit's API limits

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Related Issue

This implementation addresses issue #693 from the 100LinesOfPythonCode repository.

## License

This project is open source and available under the repository's license terms.
