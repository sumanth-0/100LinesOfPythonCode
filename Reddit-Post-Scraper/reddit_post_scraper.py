#!/usr/bin/env python3
"""
Reddit Post Scraper
Fetch the latest posts from a user-supplied Reddit subreddit.
"""

import requests
import sys
from datetime import datetime


def fetch_reddit_posts(subreddit, limit=10):
    """
    Fetch top posts from a subreddit using Reddit's JSON API.
    
    Args:
        subreddit (str): Name of the subreddit
        limit (int): Number of posts to fetch (default: 10)
    
    Returns:
        list: List of post dictionaries
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Reddit Post Scraper/1.0'}
    
    try:
        response = requests.get(url, headers=headers, params={'limit': limit})
        response.raise_for_status()
        data = response.json()
        return data['data']['children']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except KeyError:
        print("Error: Unable to parse Reddit response")
        return []


def display_posts(posts):
    """
    Display post information in a formatted manner.
    
    Args:
        posts (list): List of post data from Reddit API
    """
    if not posts:
        print("No posts found or error occurred.")
        return
    
    print(f"\n{'='*80}")
    print(f"Found {len(posts)} posts")
    print(f"{'='*80}\n")
    
    for idx, post in enumerate(posts, 1):
        post_data = post['data']
        title = post_data.get('title', 'N/A')
        author = post_data.get('author', 'N/A')
        upvotes = post_data.get('ups', 0)
        comments = post_data.get('num_comments', 0)
        url = f"https://www.reddit.com{post_data.get('permalink', '')}"
        created = datetime.fromtimestamp(post_data.get('created_utc', 0))
        
        print(f"[{idx}] {title}")
        print(f"    Author: {author}")
        print(f"    Upvotes: {upvotes} | Comments: {comments}")
        print(f"    Posted: {created.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"    URL: {url}")
        print(f"    {'-'*76}\n")


def main():
    """
    Main function to run the Reddit Post Scraper CLI.
    """
    print("=" * 80)
    print("Reddit Post Scraper".center(80))
    print("=" * 80)
    
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    else:
        subreddit = input("\nEnter subreddit name: ").strip()
        if not subreddit:
            print("Error: Subreddit name cannot be empty.")
            sys.exit(1)
        
        try:
            limit = int(input("Number of posts to fetch (default 10): ").strip() or 10)
        except ValueError:
            limit = 10
    
    print(f"\nFetching posts from r/{subreddit}...\n")
    posts = fetch_reddit_posts(subreddit, limit)
    display_posts(posts)


if __name__ == "__main__":
    main()
