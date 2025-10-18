"""
Random Wikipedia Paragraph Fetcher
Fetches and displays the first paragraph of a random Wikipedia article.
"""

import requests
import sys


def get_random_wikipedia_article():
    """
    Fetch a random Wikipedia article and return its title and first paragraph.
    
    Returns:
        tuple: (title, first_paragraph) or (None, None) if error occurs
    """
    try:
        # API endpoint for random Wikipedia article
        random_url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
        
        # Make request to get random article
        response = requests.get(random_url, timeout=10)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract title and first paragraph (extract)
        title = data.get('title', 'Unknown Title')
        first_paragraph = data.get('extract', 'No content available.')
        article_url = data.get('content_urls', {}).get('desktop', {}).get('page', '')
        
        return title, first_paragraph, article_url
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article: {e}")
        return None, None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None, None


def display_article(title, paragraph, url):
    """
    Display the article information in a formatted way.
    
    Args:
        title: Article title
        paragraph: First paragraph text
        url: URL to the full article
    """
    print("\n" + "=" * 70)
    print(f"📖 RANDOM WIKIPEDIA ARTICLE")
    print("=" * 70)
    print(f"\n🔖 Title: {title}\n")
    print(f"📝 First Paragraph:\n{paragraph}\n")
    print(f"🔗 Read more: {url}")
    print("=" * 70 + "\n")


def main():
    """
    Main function to run the Wikipedia random article fetcher.
    """
    print("\n🌐 Fetching a random Wikipedia article...\n")
    
    title, paragraph, url = get_random_wikipedia_article()
    
    if title and paragraph:
        display_article(title, paragraph, url)
        
        # Ask if user wants another article
        while True:
            choice = input("Would you like another random article? (y/n): ").strip().lower()
            if choice == 'y':
                print("\n🌐 Fetching another random article...\n")
                title, paragraph, url = get_random_wikipedia_article()
                if title and paragraph:
                    display_article(title, paragraph, url)
                else:
                    print("Failed to fetch article. Exiting...")
                    sys.exit(1)
            elif choice == 'n':
                print("\n👋 Thank you for using Random Wikipedia Article Fetcher!")
                break
            else:
                print("Please enter 'y' or 'n'.")
    else:
        print("Failed to fetch article. Please check your internet connection.")
        sys.exit(1)


if __name__ == "__main__":
    main()
