#!/usr/bin/env python3
"""GitHub Repository Info CLI - Shows stars, forks, and issues count."""
import sys
import json
import urllib.request
import urllib.error
from typing import Dict, Optional


class GitHubRepoInfo:
    """Fetches and displays GitHub repository information."""
    BASE_API_URL = "https://api.github.com/repos"

    def __init__(self, owner: str, repo: str):
        self.owner = owner
        self.repo = repo
        self.api_url = f"{self.BASE_API_URL}/{owner}/{repo}"

    def fetch_repo_data(self) -> Optional[Dict]:
        """Fetch repository data from GitHub API."""
        try:
            req = urllib.request.Request(self.api_url)
            req.add_header('User-Agent', 'GitHub-Repo-Info-CLI')
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                return data
        except urllib.error.HTTPError as e:
            print(f"Error: HTTP {e.code} - {e.reason}")
            if e.code == 404:
                print("Repository not found. Check owner and repo name.")
            return None
        except urllib.error.URLError as e:
            print(f"Error: Failed to reach server - {e.reason}")
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    def display_info(self, data: Dict) -> None:
        """Display formatted repository information."""
        print("\n" + "="*50)
        print(f"Repository: {data['full_name']}")
        print("="*50)
        print(f"\nDescription: {data.get('description', 'No description')}")
        print(f"\n⭐ Stars: {data['stargazers_count']}")
        print(f"🍴 Forks: {data['forks_count']}")
        print(f"❗ Open Issues: {data['open_issues_count']}")
        print(f"\n👁️  Watchers: {data['watchers_count']}")
        print(f"📝 Language: {data.get('language', 'Not specified')}")
        print(f"🔗 URL: {data['html_url']}")
        print("\n" + "="*50)

    def run(self) -> bool:
        """Execute the main workflow: fetch and display repo info."""
        print(f"Fetching info for {self.owner}/{self.repo}...")
        data = self.fetch_repo_data()
        if data:
            self.display_info(data)
            return True
        return False


def parse_repo_url(url: str) -> Optional[tuple]:
    """Parse GitHub repository URL to extract owner and repo name."""
    if "github.com" in url:
        parts = url.rstrip('/').split('/')
        if len(parts) >= 2:
            return parts[-2], parts[-1]
    return None


def parse_arguments() -> tuple:
    """Parse command-line arguments and return owner and repo."""
    if len(sys.argv) < 2:
        print("Usage: python github_repo_info.py <owner/repo> or <url>")
        print("Example: python github_repo_info.py octocat/Hello-World")
        sys.exit(1)
    arg = sys.argv[1]
    if '/' in arg and "github.com" not in arg:
        owner, repo = arg.split('/', 1)
    elif "github.com" in arg:
        result = parse_repo_url(arg)
        if result:
            owner, repo = result
        else:
            print("Error: Invalid GitHub URL")
            sys.exit(1)
    else:
        print("Error: Invalid format. Use owner/repo or URL")
        sys.exit(1)
    return owner, repo


def main():
    """Main function to handle CLI arguments and run the tool."""
    owner, repo = parse_arguments()
    gh_info = GitHubRepoInfo(owner, repo)
    success = gh_info.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
