import requests
from bs4 import BeautifulSoup

def get_latest_headlines(url, element, class_name, limit=5):
    """Fetches latest headlines from the specified URL."""
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Failed to retrieve data (status code: {response.status_code})"
    
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all(element, class_=class_name, limit=limit)
    
    if not headlines:
        return "No headlines found."

    return [headline.get_text(strip=True) for headline in headlines]

if __name__ == "__main__":
    # Specify the URL and HTML element details to target
    url = "https://www.bbc.com/news"  # Example URL, replace with your target
    element = "h3"  # Example target HTML element
    class_name = "gs-c-promo-heading__title"  # Example class name for headlines
    
    # Fetch and display headlines
    headlines = get_latest_headlines(url, element, class_name)
    if isinstance(headlines, str):  # Error message
        print(headlines)
    else:
        print("Latest Headlines:")
        for i, headline in enumerate(headlines, 1):
            print(f"{i}. {headline}")
