# Reddit Top Post Viewer

## Description
A command-line tool to display top posts from any subreddit in your terminal. This tool fetches and displays Reddit's top posts with details including title, author, score, comment count, and direct link to the post.

## Prerequisites
- Python 3.6 or higher
- `requests` library

## Installation

1. Install the required dependency:
```bash
pip install requests
```

2. Make the script executable (optional):
```bash
chmod +x reddit_viewer.py
```

## Usage

### Basic Usage
View top 10 posts from a subreddit:
```bash
python reddit_viewer.py python
```

### Custom Limit
Specify the number of posts to display (1-100):
```bash
python reddit_viewer.py python --limit 20
```
or
```bash
python reddit_viewer.py python -l 20
```

### Help
Display help information:
```bash
python reddit_viewer.py --help
```

## Examples

```bash
# View top 10 posts from r/programming
python reddit_viewer.py programming

# View top 25 posts from r/learnpython
python reddit_viewer.py learnpython --limit 25

# View top 5 posts from r/news
python reddit_viewer.py news -l 5
```

## Features
- ✨ Simple CLI interface with argument parsing
- 🎯 Fetches top posts from any public subreddit
- 📊 Displays key post information (title, author, score, comments)
- 🔗 Direct links to view posts on Reddit
- ⚡ No Reddit API authentication required
- 📏 Approximately 100 lines of Python code

## Output Format

The tool displays posts in the following format:
```
================================================================================
Top 10 Posts from r/python
================================================================================

1. Example Post Title
   Author: u/username | Score: 1234 | Comments: 56
   URL: https://reddit.com/r/python/comments/...

2. Another Example Post
   Author: u/another_user | Score: 890 | Comments: 23
   URL: https://reddit.com/r/python/comments/...
...
```

## Notes
- This tool uses Reddit's public JSON API (no authentication required)
- The tool displays top posts from the past day by default
- Maximum limit is 100 posts per Reddit's API restrictions
- Long post titles are truncated to 70 characters for better readability

## Contributing
This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

## Issue
Created for issue [#989](https://github.com/sumanth-0/100LinesOfPythonCode/issues/989) - Reddit Top Post Viewer

## License
Follows the repository's license.
