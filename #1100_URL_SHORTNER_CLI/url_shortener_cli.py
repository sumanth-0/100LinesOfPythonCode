import argparse
import requests
import sys

# The base API endpoint for shrtco.de (no API key required)
API_ENDPOINT = "https://api.shrtco.de/v2/shorten"

def shorten_url(long_url):
    """
    Shortens a given URL using the shrtco.de API.

    Args:
        long_url (str): The original long URL to shorten.

    Returns:
        str: The shortened URL if successful, otherwise an error message.
    """
    try:
        # A simple check to ensure the URL has a scheme for the API call
        if not long_url.startswith(('http://', 'https://')):
            # Assume https if no scheme is provided
            long_url = 'https://' + long_url
            
        # API call parameters
        params = {'url': long_url}
        
        # Send GET request to the shortening service with a timeout
        response = requests.get(API_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        
        data = response.json()
        
        if data.get('ok') and data.get('result'):
            # Return the full shortened link
            return data['result']['full_short_link']
        else:
            # Handle API-specific errors (e.g., invalid URL format reported by API)
            error_code = data.get('error_code', 'N/A')
            error_msg = data.get('error', 'Unknown error')
            return f"Error shortening URL (Code {error_code}): {error_msg}"
            
    except requests.exceptions.RequestException as e:
        # Catch network errors (e.g., connection timed out, DNS error)
        return f"Network or API Error: {e}"
    except Exception as e:
        # Catch unexpected errors
        return f"An unexpected error occurred: {e}"

def main():
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(
        description="A CLI tool to quickly shorten URLs using an external API."
    )
    parser.add_argument(
        'url',
        type=str,
        help='The URL you want to shorten (e.g., https://google.com).'
    )
    
    args = parser.parse_args()
    
    # Get the shortened URL
    short_link = shorten_url(args.url)
    
    # Print the result to the console
    print("\nOriginal URL:")
    print(f"{args.url}")
    print("\nShortened URL:")
    print(f"{short_link}\n")

if __name__ == "__main__":
    # Check for arguments first to provide clear usage
    if len(sys.argv) < 2:
        print("Usage: python url_shortener_cli.py <url_to_shorten>")
        sys.exit(1)
    
    main()