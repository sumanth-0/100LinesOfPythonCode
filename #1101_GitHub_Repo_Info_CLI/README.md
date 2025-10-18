# GitHub Repo Info CLI

A command-line tool to fetch and display GitHub repository information including stars, forks, and open issues count.

## Features

- Fetch repository statistics from GitHub API
- Display stars, forks, and open issues count
- Show additional info like watchers, language, and description
- Support for both `owner/repo` format and full GitHub URLs
- Clean and formatted output

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Usage

### Using owner/repo format:
```bash
python github_repo_info.py octocat/Hello-World
```

### Using GitHub URL:
```bash
python github_repo_info.py https://github.com/octocat/Hello-World
```

## Output Example

```
Fetching info for octocat/Hello-World...

==================================================
Repository: octocat/Hello-World
==================================================

Description: My first repository on GitHub!

⭐ Stars: 2000
🍴 Forks: 1500
❗ Open Issues: 50

👁️  Watchers: 2000
📝 Language: Python
🔗 URL: https://github.com/octocat/Hello-World

==================================================
```

## Error Handling

The tool handles various error scenarios:
- Invalid repository names
- Network connection issues
- Repository not found (404 errors)
- Invalid GitHub URLs

## Implementation Details

- Uses GitHub REST API v3
- Makes authenticated requests with User-Agent header
- Implements proper error handling for HTTP errors
- Timeout set to 10 seconds for API requests

## Issue

Solves issue #1101: GitHub Repo Info CLI - Show stars, forks, and issues count of a GitHub repository.
