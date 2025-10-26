import requests
import sys
import json
from datetime import datetime
from typing import Optional

class GitHubRepoFetcher:
    """Fetch public repository information for a GitHub user."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None):
        """
        Initialize the GitHub API client.
        
        Args:
            token: Optional GitHub personal access token for higher rate limits
        """
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Repo-Fetcher'
        }
        if token:
            self.headers['Authorization'] = f'token {token}'
    
    def get_user_info(self, username: str) -> dict:
        """
        Get basic user information.
        
        Args:
            username: GitHub username
            
        Returns:
            dict: User information
        """
        url = f"{self.BASE_URL}/users/{username}"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 404:
            raise ValueError(f"User '{username}' not found")
        elif response.status_code == 403:
            raise Exception("API rate limit exceeded. Consider using a personal access token.")
        elif response.status_code != 200:
            raise Exception(f"API error: {response.status_code}")
        
        return response.json()
    
    def get_repositories(self, username: str) -> list:
        """
        Get all public repositories for a user.
        
        Args:
            username: GitHub username
            
        Returns:
            list: List of repository information
        """
        repos = []
        page = 1
        per_page = 100
        
        while True:
            url = f"{self.BASE_URL}/users/{username}/repos"
            params = {
                'per_page': per_page,
                'page': page,
                'type': 'public',
                'sort': 'updated'
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            
            if response.status_code == 404:
                raise ValueError(f"User '{username}' not found")
            elif response.status_code == 403:
                raise Exception("API rate limit exceeded. Consider using a personal access token.")
            elif response.status_code != 200:
                raise Exception(f"API error: {response.status_code}")
            
            data = response.json()
            
            if not data:
                break
            
            repos.extend(data)
            page += 1
        
        return repos
    
    def format_repo_info(self, repo: dict) -> dict:
        """
        Extract and format relevant repository information.
        
        Args:
            repo: Repository data from GitHub API
            
        Returns:
            dict: Formatted repository information
        """
        return {
            'name': repo['name'],
            'full_name': repo['full_name'],
            'description': repo['description'] or 'No description',
            'url': repo['html_url'],
            'stars': repo['stargazers_count'],
            'forks': repo['forks_count'],
            'watchers': repo['watchers_count'],
            'language': repo['language'] or 'Not specified',
            'created_at': repo['created_at'],
            'updated_at': repo['updated_at'],
            'size': repo['size'],
            'open_issues': repo['open_issues_count'],
            'is_fork': repo['fork'],
            'topics': repo.get('topics', [])
        }

def print_user_summary(user_info: dict, repos: list):
    """Print a summary of user and repository information."""
    print("\n" + "="*80)
    print(f"GitHub User: {user_info['login']}")
    print("="*80)
    
    if user_info.get('name'):
        print(f"Name: {user_info['name']}")
    if user_info.get('bio'):
        print(f"Bio: {user_info['bio']}")
    if user_info.get('location'):
        print(f"Location: {user_info['location']}")
    if user_info.get('blog'):
        print(f"Website: {user_info['blog']}")
    
    print(f"\nPublic Repositories: {user_info['public_repos']}")
    print(f"Followers: {user_info['followers']}")
    print(f"Following: {user_info['following']}")
    
    total_stars = sum(repo['stars'] for repo in repos)
    total_forks = sum(repo['forks'] for repo in repos)
    
    print(f"\nTotal Stars: ⭐ {total_stars}")
    print(f"Total Forks: 🍴 {total_forks}")
    print("="*80)

def print_repositories(repos: list, sort_by: str = 'stars'):
    """
    Print repository information.
    
    Args:
        repos: List of repository information
        sort_by: Sort repositories by 'stars', 'forks', or 'updated'
    """
    if sort_by == 'stars':
        sorted_repos = sorted(repos, key=lambda x: x['stars'], reverse=True)
    elif sort_by == 'forks':
        sorted_repos = sorted(repos, key=lambda x: x['forks'], reverse=True)
    elif sort_by == 'updated':
        sorted_repos = sorted(repos, key=lambda x: x['updated_at'], reverse=True)
    else:
        sorted_repos = repos
    
    print(f"\nRepositories (sorted by {sort_by}):")
    print("-"*80)
    
    for i, repo in enumerate(sorted_repos, 1):
        print(f"\n{i}. {repo['name']}")
        print(f"   Description: {repo['description']}")
        print(f"   URL: {repo['url']}")
        print(f"   ⭐ Stars: {repo['stars']} | 🍴 Forks: {repo['forks']} | Language: {repo['language']}")
        print(f"   Updated: {repo['updated_at'][:10]}")
        
        if repo['is_fork']:
            print(f"   [FORKED REPOSITORY]")

def save_to_json(data: dict, filename: str):
    """Save data to JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\nData saved to: {filename}")
    except Exception as e:
        print(f"\nError saving to file: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python github_fetcher.py <username> [options]")
        print("\nOptions:")
        print("  --token TOKEN        GitHub personal access token (for higher rate limits)")
        print("  --sort FIELD         Sort by: stars, forks, or updated (default: stars)")
        print("  --output FILE        Save results to JSON file")
        print("  --top N              Show only top N repositories")
        print("\nExamples:")
        print("  python github_fetcher.py torvalds")
        print("  python github_fetcher.py octocat --sort forks --top 10")
        print("  python github_fetcher.py github --output github_repos.json")
        print("  python github_fetcher.py username --token YOUR_GITHUB_TOKEN")
        sys.exit(1)
    
    username = sys.argv[1]
    token = None
    sort_by = 'stars'
    output_file = None
    top_n = None
    
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--token' and i + 1 < len(sys.argv):
            token = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--sort' and i + 1 < len(sys.argv):
            sort_by = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--output' and i + 1 < len(sys.argv):
            output_file = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == '--top' and i + 1 < len(sys.argv):
            top_n = int(sys.argv[i + 1])
            i += 2
        else:
            i += 1
    
    try:
        print(f"Fetching repositories for user: {username}...")
        
        fetcher = GitHubRepoFetcher(token)
        
        user_info = fetcher.get_user_info(username)
        
        raw_repos = fetcher.get_repositories(username)
        repos = [fetcher.format_repo_info(repo) for repo in raw_repos]
        
        if top_n:
            if sort_by == 'stars':
                repos = sorted(repos, key=lambda x: x['stars'], reverse=True)[:top_n]
            elif sort_by == 'forks':
                repos = sorted(repos, key=lambda x: x['forks'], reverse=True)[:top_n]
            elif sort_by == 'updated':
                repos = sorted(repos, key=lambda x: x['updated_at'], reverse=True)[:top_n]
        
        print_user_summary(user_info, repos)
        
        print_repositories(repos, sort_by)
        
        if output_file:
            data = {
                'user': {
                    'username': user_info['login'],
                    'name': user_info.get('name'),
                    'bio': user_info.get('bio'),
                    'location': user_info.get('location'),
                    'blog': user_info.get('blog'),
                    'public_repos': user_info['public_repos'],
                    'followers': user_info['followers'],
                    'following': user_info['following']
                },
                'repositories': repos,
                'fetched_at': datetime.now().isoformat()
            }
            save_to_json(data, output_file)
        
        print("\n" + "="*80)
        print("✓ Fetch completed successfully!")
        print("="*80)
        
    except ValueError as e:
        print(f"\nError: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()