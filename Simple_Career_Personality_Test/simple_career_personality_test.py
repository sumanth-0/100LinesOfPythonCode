import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('SERP_API_KEY') # SERP API KEY

def fetch_career_suggestions(query):
    # SERP API URL and parameters
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google",
        "q": query,
        "api_key": API_KEY,
        "num": 10,  # Fetch more results to increase chances of finding non-ads
        "no_ads": "true",  # This parameter attempts to exclude ads
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("organic_results", [])
        # Filter results to exclude any that have indicators of ads/promotions
        filtered_results = [
            result for result in results 
            if "ad" not in result.get("link", "").lower() 
            and "sponsored" not in result.get("title", "").lower()
        ]
        return filtered_results
    else:
        print("Error fetching data from SERP API")
        return []

def career_test():
    print("Welcome to the Career Inspiration Test!\n")

    # Open-ended questions
    interests = input("What are your main interests? (e.g., technology, art, environment, etc.): ")
    skills = input("What skills do you excel in? (e.g., problem-solving, communication, analysis, etc.): ")
    work_style = input("What is your preferred work environment? (e.g., independent, team-based, hands-on, etc.): ")

    # Constructing a dynamic search query
    query = f"career options for {interests} with {skills} skills in a {work_style} environment"
    print(f"\nSearching careers for: {query}\n")

    # Fetch and display results
    search_results = fetch_career_suggestions(query)

    print("\n--- Career Suggestions ---\n")
    if search_results:
        for result in search_results:
            print(f"Title: {result.get('title')}")
            print(f"Snippet: {result.get('snippet')}")
            print(f"Link: {result.get('link')}\n")
    else:
        print("No career suggestions found. Please try different inputs.")

if __name__ == "__main__":
    career_test()
