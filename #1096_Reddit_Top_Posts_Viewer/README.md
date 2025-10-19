# Reddit Top Posts Viewer

## Description
A Python script that fetches and displays the top posts from any subreddit using Reddit's public JSON API. No authentication required!

## Features
- Fetch top posts from any public subreddit
- Customizable number of posts (1-100)
- Multiple time filter options (hour, day, week, month, year, all)
- Displays post title, author, score, timestamp, and link
- Clean, formatted output in the terminal
- User-friendly command-line interface

## Requirements
```bash
pip install requests
```

## Usage

### Interactive Mode
```bash
python reddit_top_posts_viewer.py
```
You'll be prompted to enter:
- Subreddit name
- Number of posts to view
- Time filter period

### Command Line Mode
```bash
python reddit_top_posts_viewer.py python
```
Pass the subreddit name as an argument, then follow the prompts for additional options.

## Example Output
```
================================================================================
Top 5 Posts
================================================================================

1. Getting Started with Python in 2025
   Author: u/pythondev
   Score: 2,543 | Posted: 2025-10-18 10:30:00
   Link: https://www.reddit.com/r/python/comments/...
--------------------------------------------------------------------------------

2. Best Python Libraries for Data Science
   Author: u/datascientist
   Score: 1,892 | Posted: 2025-10-18 08:15:00
   Link: https://www.reddit.com/r/python/comments/...
--------------------------------------------------------------------------------
```

## Time Filters
- `hour` - Top posts from the last hour
- `day` - Top posts from the last 24 hours (default)
- `week` - Top posts from the last week
- `month` - Top posts from the last month
- `year` - Top posts from the last year
- `all` - Top posts of all time

## Code Features
- Object-oriented design with RedditTopPostsViewer class
- Error handling for network requests
- Input validation for user inputs
- Clean separation of concerns (fetch, display, main)
- Under 100 lines of Python code

## Notes
- Uses Reddit's public JSON API (no API key required)
- Rate limiting applies - be respectful with requests
- Only works with public subreddits
- Requires internet connection

## Issue Reference
This solution addresses Issue #1096: Reddit Top Posts Viewer

## Author
Contributed to 100LinesOfPythonCode repository
