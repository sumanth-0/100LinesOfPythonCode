#!/usr/bin/env python3
"""
Reddit Top Post Viewer
Displays top posts from a subreddit in the terminal.
"""

import requests
import sys
import argparse
from typing import List, Dict


class RedditTopPostViewer:
    """CLI tool to display top posts from a subreddit."""
    
    def __init__(self, subreddit: str, limit: int = 10):
        self.subreddit = subreddit
        self.limit = min(limit, 100)  # Reddit API limit
        self.base_url = f"https://www.reddit.com/r/{subreddit}/top.json"
    
    def fetch_posts(self) -> List[Dict]:
        """Fetch top posts from the subreddit."""
        try:
            headers = {'User-Agent': 'RedditTopPostViewer/1.0'}
            params = {'limit': self.limit, 't': 'day'}  # Time filter: day
            response = requests.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data['data']['children']
        except requests.RequestException as e:
            print(f"Error fetching posts: {e}")
            sys.exit(1)
    
    def display_posts(self, posts: List[Dict]):
        """Display posts in a formatted manner."""
        if not posts:
            print(f"No posts found in r/{self.subreddit}")
            return
        
        print(f"\n{'='*80}")
        print(f"Top {len(posts)} Posts from r/{self.subreddit}")
        print(f"{'='*80}\n")
        
        for idx, post in enumerate(posts, 1):
            post_data = post['data']
            title = post_data.get('title', 'No Title')
            author = post_data.get('author', 'Unknown')
            score = post_data.get('score', 0)
            num_comments = post_data.get('num_comments', 0)
            url = f"https://reddit.com{post_data.get('permalink', '')}"
            
            # Truncate long titles
            if len(title) > 70:
                title = title[:67] + "..."
            
            print(f"{idx}. {title}")
            print(f"   Author: u/{author} | Score: {score} | Comments: {num_comments}")
            print(f"   URL: {url}")
            print()
    
    def run(self):
        """Main execution method."""
        print(f"Fetching top posts from r/{self.subreddit}...")
        posts = self.fetch_posts()
        self.display_posts(posts)


def main():
    """Main function to parse arguments and run the viewer."""
    parser = argparse.ArgumentParser(
        description='Display top posts from a subreddit in terminal.'
    )
    parser.add_argument(
        'subreddit',
        type=str,
        help='Name of the subreddit (without r/ prefix)'
    )
    parser.add_argument(
        '-l', '--limit',
        type=int,
        default=10,
        help='Number of posts to display (default: 10, max: 100)'
    )
    
    args = parser.parse_args()
    
    # Validate subreddit name
    if not args.subreddit or args.subreddit.startswith('r/'):
        print("Error: Enter subreddit name without 'r/' prefix")
        sys.exit(1)
    
    viewer = RedditTopPostViewer(args.subreddit, args.limit)
    viewer.run()


if __name__ == "__main__":
    main()
