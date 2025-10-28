# GitHub Repo Info Fetcher

A Python tool to fetch and display all public repositories and their statistics for any GitHub user. Get comprehensive information including stars, forks, languages, and more.

## Features

- 🔍 Fetch all public repositories for any GitHub user
- ⭐ View total stars and forks across all repositories
- 📊 Sort repositories by stars, forks, or last updated
- 💾 Export data to JSON format
- 🎯 Filter top N repositories
- 📈 Display detailed repository statistics
- 🔑 Support for GitHub Personal Access Token (higher rate limits)
- 👤 User profile information (bio, location, followers, etc.)

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

Fetch all repositories for a user:
```bash
python github_fetcher.py <username>
```

Example:
```bash
python github_fetcher.py torvalds
```

### Sort Repositories

Sort by stars (default):
```bash
python github_fetcher.py octocat --sort stars
```

Sort by forks:
```bash
python github_fetcher.py github --sort forks
```

Sort by last updated:
```bash
python github_fetcher.py microsoft --sort updated
```

### Show Top Repositories

Display only the top 10 repositories:
```bash
python github_fetcher.py google --top 10
```

Show top 5 most starred repositories:
```bash
python github_fetcher.py facebook --sort stars --top 5
```

### Save to JSON

Export results to a JSON file:
```bash
python github_fetcher.py github --output github_repos.json
```

### Use Personal Access Token

For higher rate limits (recommended for heavy usage):
```bash
python github_fetcher.py username --token YOUR_GITHUB_TOKEN
```

### Combined Options

```bash
python github_fetcher.py tensorflow --sort stars --top 20 --output tf_repos.json --token YOUR_TOKEN
```

## Command-Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `<username>` | GitHub username (required) | `torvalds` |
| `--sort FIELD` | Sort by: `stars`, `forks`, or `updated` | `--sort stars` |
| `--output FILE` | Save results to JSON file | `--output repos.json` |
| `--top N` | Show only top N repositories | `--top 10` |
| `--token TOKEN` | GitHub personal access token | `--token ghp_xxx...` |

## Output Format

### Console Output

```
================================================================================
GitHub User: torvalds
================================================================================
Name: Linus Torvalds
Bio: Creator of Linux
Location: Portland, OR

Public Repositories: 8
Followers: 150000
Following: 0

Total Stars: ⭐ 180000
Total Forks: 🍴 50000
================================================================================

Repositories (sorted by stars):
--------------------------------------------------------------------------------

1. linux
   Description: Linux kernel source tree
   URL: https://github.com/torvalds/linux
   ⭐ Stars: 150000 | 🍴 Forks: 45000 | Language: C
   Updated: 2024-10-22

2. subsurface
   Description: Subsurface divelog
   URL: https://github.com/torvalds/subsurface
   ⭐ Stars: 2000 | 🍴 Forks: 500 | Language: C
   Updated: 2024-10-15
...
```

### JSON Output

When using `--output`, the data is saved in the following format:

```json
{
  "user": {
    "username": "torvalds",
    "name": "Linus Torvalds",
    "bio": "Creator of Linux",
    "location": "Portland, OR",
    "blog": "",
    "public_repos": 8,
    "followers": 150000,
    "following": 0
  },
  "repositories": [
    {
      "name": "linux",
      "full_name": "torvalds/linux",
      "description": "Linux kernel source tree",
      "url": "https://github.com/torvalds/linux",
      "stars": 150000,
      "forks": 45000,
      "watchers": 150000,
      "language": "C",
      "created_at": "2011-09-04T22:48:12Z",
      "updated_at": "2024-10-22T10:30:00Z",
      "size": 3500000,
      "open_issues": 500,
      "is_fork": false,
      "topics": ["linux", "kernel", "operating-system"]
    }
  ],
  "fetched_at": "2024-10-22T14:30:45.123456"
}
```

## GitHub API Rate Limits

### Without Authentication
- 60 requests per hour per IP address
- Sufficient for occasional use

### With Personal Access Token
- 5,000 requests per hour
- Recommended for frequent use or fetching users with many repositories

### Creating a Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name
4. Select scopes: `public_repo` (or no scopes needed for public data)
5. Click "Generate token"
6. Copy the token and use it with `--token` option

**Note:** Keep your token secure and never commit it to version control!

## Repository Information

For each repository, the tool fetches:

- **Name** - Repository name
- **Description** - Repository description
- **URL** - Direct link to the repository
- **Stars** - Number of stars (⭐)
- **Forks** - Number of forks (🍴)
- **Watchers** - Number of watchers
- **Language** - Primary programming language
- **Created Date** - When the repository was created
- **Updated Date** - Last update timestamp
- **Size** - Repository size in KB
- **Open Issues** - Number of open issues
- **Is Fork** - Whether it's a forked repository
- **Topics** - Repository topics/tags

## Examples

### Fetch popular user repositories

```bash
# Check out Linus Torvalds' repositories
python github_fetcher.py torvalds

# See GitHub's official repositories
python github_fetcher.py github --sort stars --top 15

# Explore Google's open source projects
python github_fetcher.py google --sort forks --output google_repos.json

# Check Microsoft's most recently updated repos
python github_fetcher.py microsoft --sort updated --top 20
```

### Research and Analysis

```bash
# Compare repository statistics
python github_fetcher.py facebook --output facebook.json
python github_fetcher.py google --output google.json

# Find most forked projects
python github_fetcher.py apache --sort forks --top 10

# Track active development
python github_fetcher.py rust-lang --sort updated
```

## Error Handling

The tool handles common errors gracefully:

- **User not found**: Displays clear error message
- **API rate limit exceeded**: Suggests using a personal access token
- **Network errors**: Reports connection issues
- **Invalid token**: Notifies about authentication problems

## Limitations

- Only fetches **public repositories** (private repos require authentication and proper scopes)
- Subject to GitHub API rate limits
- Large organizations with 1000+ repositories may take time to fetch all data
- Some user profile fields may be empty if not set by the user

## Performance Tips

- Use `--top N` to limit results for users with many repositories
- Use a personal access token for higher rate limits
- For repeated queries on the same user, save to JSON and reuse the data
- The tool automatically paginates through all repositories (100 per page)

## Use Cases

- 📊 **Portfolio Analysis** - Analyze developer activity and popular projects
- 🔍 **Research** - Study open source projects and their popularity
- 📈 **Trending** - Track repository growth and activity
- 🎓 **Learning** - Discover popular projects in specific languages
- 💼 **Recruitment** - Review candidate's public contributions
- 📝 **Documentation** - Generate repository lists for documentation

## Troubleshooting

### Rate Limit Exceeded

**Problem:** "API rate limit exceeded" error

**Solution:** Use a personal access token with `--token` option

### User Not Found

**Problem:** "User 'username' not found" error

**Solution:** Verify the username is correct and the account exists

### Slow Performance

**Problem:** Takes long time to fetch repositories

**Solution:** Use `--top N` to limit results or ensure good internet connection
