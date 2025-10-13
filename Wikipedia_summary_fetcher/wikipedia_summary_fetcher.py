"""
Wikipedia Summary Fetcher
A simple script to fetch one-line summaries from Wikipedia using the Wikipedia API.
No external libraries required - uses only Python's built-in urllib and json modules.
"""

import urllib.request
import urllib.parse
import json
import sys


def fetch_wikipedia_summary(topic):
    """
    Fetches a concise summary for a given topic from Wikipedia.
    
    Args:
        topic (str): The topic to search for on Wikipedia
        
    Returns:
        str: A one-line summary of the topic, or an error message
    """
    # Wikipedia API endpoint for extracting page content
    base_url = "https://en.wikipedia.org/api/rest_v1/page/summary/"
    
    # URL encode the topic to handle special characters and spaces
    encoded_topic = urllib.parse.quote(topic.replace(" ", "_"))
    url = base_url + encoded_topic
    
    try:
        # Create a request with a proper User-Agent header
        # Wikipedia requires this to identify the client
        request = urllib.request.Request(
            url,
            headers={
                'User-Agent': 'WikipediaSummaryFetcher/1.0 (Educational Project)'
            }
        )
        
        # Make the HTTP request to Wikipedia API
        with urllib.request.urlopen(request, timeout=10) as response:
            # Read and parse the JSON response
            data = json.loads(response.read().decode('utf-8'))
            
            # Extract the summary (extract field contains the first paragraph)
            summary = data.get('extract', 'No summary available.')
            
            return summary
            
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"Error: Topic '{topic}' not found on Wikipedia."
        else:
            return f"Error: HTTP {e.code} - {e.reason}"
            
    except urllib.error.URLError as e:
        return f"Error: Network connection failed - {e.reason}"
        
    except json.JSONDecodeError:
        return "Error: Failed to parse Wikipedia response."
        
    except Exception as e:
        return f"Error: An unexpected error occurred - {str(e)}"


def main():
    """
    Main function to handle user input and display results.
    """
    print("=" * 60)
    print("Wikipedia Summary Fetcher")
    print("=" * 60)
    
    # Check if topic was provided as command line argument
    if len(sys.argv) > 1:
        # Join all arguments to handle multi-word topics
        topic = " ".join(sys.argv[1:])
    else:
        # Interactive mode - prompt user for input
        topic = input("\nEnter a topic to search: ").strip()
    
    # Validate input
    if not topic:
        print("Error: Please provide a valid topic.")
        return
    
    print(f"\nSearching for: {topic}")
    print("-" * 60)
    
    # Fetch and display the summary
    summary = fetch_wikipedia_summary(topic)
    print(f"\n{summary}\n")
    print("=" * 60)


if __name__ == "__main__":
    main()