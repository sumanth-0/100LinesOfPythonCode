# GitHub Profile Fetcher

A command-line tool to fetch and display GitHub user profile information using the public GitHub API.

## Description

This Python script allows you to quickly view GitHub user profile information including:
- User bio and basic information
- Repository count
- Follower and following count
- Public gists count
- Top 5 repositories sorted by stars
- Location, company, and website (if available)

## Features

- **Simple CLI Interface**: Easy-to-use command-line interface
- **No Authentication Required**: Uses GitHub's public API
- **Comprehensive Profile Data**: Displays all essential user information
- **Top Repositories**: Shows the user's top 5 most starred repositories
- **Error Handling**: Gracefully handles API errors and invalid usernames
- **Clean Output**: Formatted and easy-to-read console output

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone the repository or download the script
2. No additional installation required - all dependencies are built into Python

## Usage

```bash
python github_profile_fetcher.py <github_username>
```

### Example

```bash
python github_profile_fetcher.py octocat
```

### Sample Output

```
Fetching profile for 'octocat'...

============================================================
GitHub Profile: octocat
============================================================

Name: The Octocat
Username: octocat
Profile URL: https://github.com/octocat

Bio: GitHub mascot

                       Statistics                        
------------------------------------------------------------
Public Repositories: 8
Followers: 12345
Following: 9
Public Gists: 8
Location: San Francisco
Company: @github
Website: https://github.blog

              Top Repositories (by stars)                 
------------------------------------------------------------

1. Hello-World
   ⭐ Stars: 2000
   🍴 Forks: 1000
   Description: My first repository on GitHub!
   URL: https://github.com/octocat/Hello-World

============================================================
```

## Implementation Details

- **Total Lines**: Under 100 lines of Python code
- **API Endpoints Used**:
  - User Profile: `https://api.github.com/users/{username}`
  - User Repositories: `https://api.github.com/users/{username}/repos`
- **No Rate Limiting**: Uses public API (60 requests per hour for unauthenticated requests)

## Error Handling

The script handles various error scenarios:
- Invalid or non-existent usernames
- Network connectivity issues
- API rate limiting
- Malformed API responses

## Limitations

- Rate limited to 60 requests per hour (GitHub's public API limit)
- Only displays public profile information
- Shows top 5 repositories only

## Contributing

This project was created for the 100 Lines of Python Code challenge. Contributions are welcome!

## License

MIT License - Feel free to use and modify as needed.

## Related Issues

- Resolves issue #668 from 100LinesOfPythonCode repository
