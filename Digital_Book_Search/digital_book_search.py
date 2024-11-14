import requests
from dotenv import load_dotenv
import os

load_dotenv()
def search_books(query):
    """Search for books using Google Books API."""
    url = "https://www.googleapis.com/books/v1/volumes"
    api_key = os.getenv('API_KEY')
    params = {
        "q": query,
        "maxResults": 5,  # Limit results for brevity
        "key": api_key  # Replace with your Google API key
    }
    response = requests.get(url, params=params)
    return response.json()

def display_books(books):
    """Display book information."""
    if 'items' not in books:
        print("No results found.")
        return

    for item in books['items']:
        title = item['volumeInfo'].get('title', 'No title available')
        authors = ', '.join(item['volumeInfo'].get('authors', ['Unknown author']))
        description = item['volumeInfo'].get('description', 'No description available')
        rating = item['volumeInfo'].get('averageRating', 'No rating available')
        print(f"Title: {title}")
        print(f"Authors: {authors}")
        print(f"Description: {description}")
        print(f"Rating: {rating}")
        print('-' * 40)

def main():
    """Main function to run the book search application."""
    print("Welcome to the Book Search Application!")
    query = input("Enter a book title, author, or keyword: ")
    
    books = search_books(query)
    display_books(books)

if __name__ == "__main__":
    main()
