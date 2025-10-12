#!/usr/bin/env python3
"""
GitHub Profile Fetcher
Fetches and displays GitHub user profile information including bio, repo count,
follower count, and top repositories using the public GitHub API.
"""

import sys
import urllib.request
import urllib.error
import json
from typing import Dict, List, Any


def fetch_user_profile(username: str) -> Dict[str, Any]:
    """Fetch user profile data from GitHub API."""
    url = f"https://api.github.com/users/{username}"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        else:
            print(f"Error: HTTP {e.code} - {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching profile: {e}")
        sys.exit(1)


def fetch_user_repos(username: str) -> List[Dict[str, Any]]:
    """Fetch user repositories from GitHub API."""
    url = f"https://api.github.com/users/{username}/repos?sort=stars&per_page=5"
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching repositories: {e}")
        return []


def display_profile(profile: Dict[str, Any], repos: List[Dict[str, Any]]) -> None:
    """Display formatted user profile information."""
    print("\n" + "="*60)
    print(f"GitHub Profile: {profile['login']}")
    print("="*60)
    
    # Basic information
    print(f"\nName: {profile.get('name', 'N/A')}")
    print(f"Username: {profile['login']}")
    print(f"Profile URL: {profile['html_url']}")
    
    # Bio
    bio = profile.get('bio', 'N/A')
    print(f"\nBio: {bio if bio else 'No bio available'}")
    
    # Statistics
    print(f"\n{'Statistics':^60}")
    print("-"*60)
    print(f"Public Repositories: {profile.get('public_repos', 0)}")
    print(f"Followers: {profile.get('followers', 0)}")
    print(f"Following: {profile.get('following', 0)}")
    print(f"Public Gists: {profile.get('public_gists', 0)}")
    
    # Location and company
    if profile.get('location'):
        print(f"Location: {profile['location']}")
    if profile.get('company'):
        print(f"Company: {profile['company']}")
    if profile.get('blog'):
        print(f"Website: {profile['blog']}")
    
    # Top repositories
    if repos:
        print(f"\n{'Top Repositories (by stars)':^60}")
        print("-"*60)
        for idx, repo in enumerate(repos, 1):
            print(f"\n{idx}. {repo['name']}")
            print(f"   ⭐ Stars: {repo.get('stargazers_count', 0)}")
            print(f"   🍴 Forks: {repo.get('forks_count', 0)}")
            if repo.get('description'):
                print(f"   Description: {repo['description']}")
            print(f"   URL: {repo['html_url']}")
    
    print("\n" + "="*60 + "\n")


def main():
    """Main function to run the GitHub Profile Fetcher."""
    if len(sys.argv) != 2:
        print("Usage: python github_profile_fetcher.py <github_username>")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"Fetching profile for '{username}'...")
    
    profile = fetch_user_profile(username)
    repos = fetch_user_repos(username)
    display_profile(profile, repos)


if __name__ == "__main__":
    main()
