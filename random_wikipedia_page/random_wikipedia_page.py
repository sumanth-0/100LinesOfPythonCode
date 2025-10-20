#!/usr/bin/env python3
"""
Random Wikipedia Page Fetcher

This script fetches and displays a random Wikipedia article using the Wikipedia API.
It provides detailed information about the article including title, summary, URL,
categories, and word count. The script includes error handling, user interaction,
and colorful console output for better user experience.

Author: GitHub User
Date: October 2025
Issue: #1037
"""

import requests
import json
import sys
import time
from typing import Dict, Optional, List
import textwrap
import os

# ANSI color codes for terminal output
class Colors:
    """ANSI color codes for terminal formatting"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print an attractive header for the application"""
    header = f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║        🌍 RANDOM WIKIPEDIA ARTICLE FETCHER 📚               ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}
    """
    print(header)

def fetch_random_wikipedia_article() -> Optional[Dict]:
    """
    Fetch a random Wikipedia article using the Wikipedia API.
    
    Returns:
        Dictionary containing article data or None if request fails
    """
    api_url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    
    try:
        print(f"{Colors.OKCYAN}🔄 Fetching random Wikipedia article...{Colors.ENDC}")
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        print(f"{Colors.FAIL}❌ Error: Request timed out. Please check your internet connection.{Colors.ENDC}")
        return None
    except requests.exceptions.ConnectionError:
        print(f"{Colors.FAIL}❌ Error: Unable to connect to Wikipedia. Check your internet.{Colors.ENDC}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"{Colors.FAIL}❌ Error: {str(e)}{Colors.ENDC}")
        return None

def get_article_categories(page_title: str) -> List[str]:
    """
    Fetch categories for a Wikipedia article.
    
    Args:
        page_title: Title of the Wikipedia page
    
    Returns:
        List of category names
    """
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'titles': page_title,
        'prop': 'categories',
        'format': 'json',
        'cllimit': 10
    }
    
    try:
        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        pages = data.get('query', {}).get('pages', {})
        for page_id, page_data in pages.items():
            categories = page_data.get('categories', [])
            return [cat['title'].replace('Category:', '') for cat in categories]
        return []
    except Exception:
        return []

def format_text(text: str, width: int = 80) -> str:
    """Format text to fit within specified width"""
    return '\n'.join(textwrap.wrap(text, width=width))

def display_article_info(article_data: Dict):
    """
    Display formatted information about the Wikipedia article.
    
    Args:
        article_data: Dictionary containing article information
    """
    title = article_data.get('title', 'Unknown')
    extract = article_data.get('extract', 'No summary available.')
    url = article_data.get('content_urls', {}).get('desktop', {}).get('page', 'N/A')
    description = article_data.get('description', 'No description available')
    
    # Get additional metadata
    page_id = article_data.get('pageid', 'N/A')
    lang = article_data.get('lang', 'en')
    
    # Count words in extract
    word_count = len(extract.split())
    
    # Fetch categories
    print(f"{Colors.OKCYAN}🔍 Fetching additional details...{Colors.ENDC}")
    categories = get_article_categories(title)
    
    # Display formatted output
    print(f"\n{Colors.BOLD}{Colors.OKGREEN}{'='*80}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}📄 ARTICLE TITLE:{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.OKBLUE}{title}{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}{Colors.HEADER}📝 DESCRIPTION:{Colors.ENDC}")
    print(f"{Colors.WARNING}{description}{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}{Colors.HEADER}📚 SUMMARY:{Colors.ENDC}")
    formatted_extract = format_text(extract, width=78)
    print(f"{formatted_extract}\n")
    
    print(f"{Colors.BOLD}{Colors.HEADER}🔗 ARTICLE URL:{Colors.ENDC}")
    print(f"{Colors.OKCYAN}{Colors.UNDERLINE}{url}{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}{Colors.HEADER}ℹ️  METADATA:{Colors.ENDC}")
    print(f"  • Page ID: {Colors.OKGREEN}{page_id}{Colors.ENDC}")
    print(f"  • Language: {Colors.OKGREEN}{lang.upper()}{Colors.ENDC}")
    print(f"  • Word Count: {Colors.OKGREEN}{word_count}{Colors.ENDC}\n")
    
    if categories:
        print(f"{Colors.BOLD}{Colors.HEADER}🏷️  CATEGORIES:{Colors.ENDC}")
        for idx, category in enumerate(categories[:5], 1):
            print(f"  {idx}. {Colors.OKGREEN}{category}{Colors.ENDC}")
        if len(categories) > 5:
            print(f"  ... and {len(categories) - 5} more")
        print()
    
    print(f"{Colors.BOLD}{Colors.OKGREEN}{'='*80}{Colors.ENDC}\n")

def main():
    """
    Main function to run the Random Wikipedia Article Fetcher.
    Handles user interaction and program flow.
    """
    try:
        while True:
            clear_screen()
            print_header()
            
            # Fetch random article
            article_data = fetch_random_wikipedia_article()
            
            if article_data:
                display_article_info(article_data)
                
                # Ask user if they want another article
                print(f"{Colors.BOLD}Would you like to fetch another random article?{Colors.ENDC}")
                choice = input(f"{Colors.OKCYAN}Enter 'y' for yes, any other key to exit: {Colors.ENDC}").strip().lower()
                
                if choice != 'y':
                    print(f"\n{Colors.OKGREEN}✨ Thank you for using Random Wikipedia Article Fetcher! Goodbye! 👋{Colors.ENDC}\n")
                    break
            else:
                print(f"\n{Colors.FAIL}Failed to fetch article. Please try again later.{Colors.ENDC}")
                break
                
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}⚠️  Program interrupted by user.{Colors.ENDC}")
        print(f"{Colors.OKGREEN}Goodbye! 👋{Colors.ENDC}\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}❌ Unexpected error: {str(e)}{Colors.ENDC}\n")
        sys.exit(1)

if __name__ == "__main__":
    # Check if requests module is available
    try:
        import requests
    except ImportError:
        print(f"{Colors.FAIL}❌ Error: 'requests' module not found.{Colors.ENDC}")
        print(f"{Colors.WARNING}Please install it using: pip install requests{Colors.ENDC}")
        sys.exit(1)
    
    main()
