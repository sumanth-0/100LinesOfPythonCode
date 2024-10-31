import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Replace with your SerpAPI key
API_KEY = os.getenv('SERP_API_KEY')

def fetch_food_info(food_name):
    # Search for the food item on Wikipedia
    wiki_url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={food_name}&utf8=&srlimit=1'
    
    wiki_response = requests.get(wiki_url)
    
    if wiki_response.status_code == 200:
        wiki_data = wiki_response.json()
        search_results = wiki_data.get('query', {}).get('search', [])
        
        if search_results:
            page_title = search_results[0]['title']
            page_info_url = f'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro=&explaintext=&titles={page_title}'
            
            # Fetch the summary of the page
            page_info_response = requests.get(page_info_url)
            if page_info_response.status_code == 200:
                page_info_data = page_info_response.json()
                page_id = next(iter(page_info_data['query']['pages']))
                description = page_info_data['query']['pages'][page_id].get('extract', 'No description available.')
            else:
                description = 'No description available.'
        else:
            description = 'No description available.'
    else:
        print(f"Error fetching data from Wikipedia: {wiki_response.status_code}")
        description = 'No description available.'

    # Search for the food item on Google using SerpAPI
    search_url = f'https://serpapi.com/search.json?q={food_name}&hl=en&gl=us&api_key={API_KEY}'
    
    response = requests.get(search_url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract the thumbnail image URL from the first search result
        image_url = data.get('organic_results', [{}])[0].get('thumbnail', 'No thumbnail available.')
        
        return {
            'description': description,
            'image_url': image_url
        }
    else:
        print(f"Error fetching data from SerpAPI: {response.status_code}")
        return None

def main():
    user_input = input("Enter the name of the street food you want to know about: ")
    food_info = fetch_food_info(user_input)
    
    if food_info:
        print(f"\n**{user_input.title()}**")
        print(f"Description: {food_info['description']}")
        print(f"Thumbnail Image: {food_info['image_url']}")

if __name__ == "__main__":
    main()
