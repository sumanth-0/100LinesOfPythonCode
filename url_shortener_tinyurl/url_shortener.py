"""
URL Shortener using TinyURL API
Shortens long URLs using the TinyURL web API with CLI and importable functions.
"""

import sys
import requests
from urllib.parse import quote


def shorten_url(long_url):
    """Shortens a URL using the TinyURL API."""
    # Ensure the URL has a proper scheme
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'https://' + long_url
    
    try:
        # TinyURL API endpoint
        api_url = f"http://tinyurl.com/api-create.php?url={quote(long_url)}"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            shortened_url = response.text.strip()
            if shortened_url.startswith('http'):
                return shortened_url
            else:
                return f"Error: Invalid response - {shortened_url}"
        else:
            return f"Error: API returned status code {response.status_code}"
            
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Check your internet connection."
    except requests.exceptions.ConnectionError:
        return "Error: Failed to connect to TinyURL. Check your connection."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"


def shorten_multiple_urls(urls):
    """Shortens multiple URLs and returns a dict of results."""
    return {url: shorten_url(url) for url in urls}


def main():
    """Main function for command-line usage."""
    print("=" * 50)
    print("URL Shortener using TinyURL API")
    print("=" * 50)
    
    # Check if URL was provided as command-line argument
    if len(sys.argv) > 1:
        url_to_shorten = ' '.join(sys.argv[1:])
        print(f"\nOriginal URL: {url_to_shorten}")
        short_url = shorten_url(url_to_shorten)
        print(f"Shortened URL: {short_url}\n")
    else:
        # Interactive mode
        print("\nEnter 'q' to quit")
        print("-" * 50)
        
        while True:
            url_input = input("\nEnter URL to shorten: ").strip()
            
            if url_input.lower() == 'q':
                print("Thanks for using URL Shortener!")
                break
            
            if not url_input:
                print("Error: Please enter a valid URL")
                continue
            
            short_url = shorten_url(url_input)
            print(f"Shortened URL: {short_url}")


if __name__ == "__main__":
    main()

