#!/usr/bin/env python3
"""
Reddit Top Posts Viewer
Displays top posts from a specified subreddit with title and link.
"""

import requests
import json
import sys
from datetime import datetime


class RedditTopPostsViewer:
    """Fetches and displays top posts from Reddit without authentication."""
    
    def __init__(self):
        self.base_url = "https://www.reddit.com"
        self.headers = {'User-Agent': 'Python Reddit Top Posts Viewer 1.0'}
    
    def fetch_top_posts(self, subreddit, limit=10, time_filter='day'):
        """
        Fetch top posts from a subreddit.
        
        Args:
            subreddit: Name of the subreddit
            limit: Number of posts to fetch (default: 10)
            time_filter: Time period - 'hour', 'day', 'week', 'month', 'year', 'all'
        """
        url = f"{self.base_url}/r/{subreddit}/top.json"
        params = {'limit': limit, 't': time_filter}
        
        try:
            response = requests.get(url, headers=self.headers, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching posts: {e}")
            return None
    
    def display_posts(self, data):
        """Display posts in a formatted manner."""
        if not data or 'data' not in data:
            print("No data available.")
            return
        
        posts = data['data']['children']
        if not posts:
            print("No posts found.")
            return
        
        print("\n" + "="*80)
        print(f"Top {len(posts)} Posts")
        print("="*80 + "\n")
        
        for idx, post in enumerate(posts, 1):
            post_data = post['data']
            title = post_data.get('title', 'No Title')
            url = f"https://www.reddit.com{post_data.get('permalink', '')}"
            score = post_data.get('score', 0)
            author = post_data.get('author', 'Unknown')
            created = post_data.get('created_utc', 0)
            created_time = datetime.fromtimestamp(created).strftime('%Y-%m-%d %H:%M:%S')
            
            print(f"{idx}. {title}")
            print(f"   Author: u/{author}")
            print(f"   Score: {score:,} | Posted: {created_time}")
            print(f"   Link: {url}")
            print("-" * 80 + "\n")


def main():
    """Main function to run the Reddit Top Posts Viewer."""
    viewer = RedditTopPostsViewer()
    
    # Get subreddit from user
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
    else:
        subreddit = input("Enter subreddit name (e.g., python): ").strip()
    
    if not subreddit:
        print("Subreddit name cannot be empty!")
        return
    
    # Get number of posts
    try:
        limit = int(input("Number of posts to view (default 10): ") or 10)
        limit = min(max(limit, 1), 100)  # Limit between 1-100
    except ValueError:
        limit = 10
    
    # Get time filter
    print("\nTime filters: hour, day, week, month, year, all")
    time_filter = input("Select time filter (default 'day'): ").strip().lower() or 'day'
    valid_filters = ['hour', 'day', 'week', 'month', 'year', 'all']
    if time_filter not in valid_filters:
        time_filter = 'day'
    
    print(f"\nFetching top {limit} posts from r/{subreddit}...\n")
    data = viewer.fetch_top_posts(subreddit, limit, time_filter)
    viewer.display_posts(data)


if __name__ == "__main__":
    main()
