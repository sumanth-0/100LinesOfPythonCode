import requests
import re
import wikipediaapi
import random

def get_random_wikipedia_summary():
    """
    Fetches the first paragraph of a random Wikipedia page with proper headers
    """
    try:
        # Set proper headers to avoid 403 error
        headers = {
            'User-Agent': 'RandomWikiBot/1.0 (https://example.com; contact@example.com)',
            'Accept': 'application/json'
        }
        
        # Get a random Wikipedia page
        random_url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
        response = requests.get(random_url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract the title and extract (first paragraph)
        title = data.get('title', 'Unknown Title')
        extract = data.get('extract', 'No summary available.')
        
        # Clean up the extract (remove reference markers like [1], [2], etc.)
        clean_extract = re.sub(r'\[\d+\]', '', extract)
        
        return title, clean_extract.strip()
        
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching data: {e}"
    except Exception as e:
        return None, f"An error occurred: {e}"

def get_random_wikipedia_alternative():
    """
    Alternative method using different Wikipedia API endpoint
    """
    try:
        headers = {
            'User-Agent': 'RandomWikiBot/1.0 (https://example.com; contact@example.com)',
            'Accept': 'application/json'
        }
        
        # First get a random page title
        random_url = "https://en.wikipedia.org/w/api.php"
        params = {
            'action': 'query',
            'list': 'random',
            'rnnamespace': 0,
            'rnlimit': 1,
            'format': 'json'
        }
        
        response = requests.get(random_url, params=params, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        random_page = data['query']['random'][0]
        page_title = random_page['title']
        
        # Now get the summary for that page
        summary_url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + requests.utils.quote(page_title)
        response = requests.get(summary_url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        extract = data.get('extract', 'No summary available.')
        clean_extract = re.sub(r'\[\d+\]', '', extract).strip()
        
        return page_title, clean_extract
        
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching data: {e}"
    except Exception as e:
        return None, f"An error occurred: {e}"

def get_random_wikipedia_with_library():
    """
    Method using wikipedia-api library (install with: pip install wikipedia-api)
    """
    try:
        # Initialize with proper user agent
        wiki_wiki = wikipediaapi.Wikipedia(
            user_agent='RandomWikiBot/1.0 (https://example.com; contact@example.com)',
            language='en'
        )
        
        # Get random pages until we find one with content
        for _ in range(3):  # Try up to 3 times
            random_page = wiki_wiki.random(pages=1)
            if random_page and random_page.exists():
                summary = random_page.summary
                if summary:
                    # Get just the first paragraph
                    first_para = summary.split('\n\n')[0]
                    clean_summary = re.sub(r'\[\d+\]', '', first_para).strip()
                    return random_page.title, clean_summary
        
        return None, "Could not find a suitable random page"
            
    except Exception as e:
        return None, f"An error occurred: {e}"

def main():
    print("Fetching a random Wikipedia page...\n")
    
    # Try the first method
    title, summary = get_random_wikipedia_summary()
    
    if not title:
        print("First method failed, trying alternative method...\n")
        # Try alternative method
        title, summary = get_random_wikipedia_alternative()
    
    if not title:
        print("Alternative method failed, trying library method...\n")
        # Try library method
        title, summary = get_random_wikipedia_with_library()
    
    if title:
        print(f"Title: {title}")
        print("-" * 50)
        print(f"Summary:\n{summary}")
    else:
        print(f"All methods failed. Last error: {summary}")

if __name__ == "__main__":
    main()