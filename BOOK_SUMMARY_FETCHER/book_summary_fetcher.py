import requests

def fetch_book_summary(title):
    # Using Open Library API or an equivalent for book data
    url = f"https://openlibrary.org/search.json?title={title}"
    response = requests.get(url)
    data = response.json()
    
    if data['numFound'] > 0:
        book = data['docs'][0]
        title = book.get('title', 'No title available')
        author = book.get('author_name', ['Unknown author'])[0]
        summary = book.get('first_sentence', 'No summary available')
        
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Summary: {summary}")
    else:
        print("No summary found for the given title.")

def main():
    book_title = input("Enter the book title: ")
    fetch_book_summary(book_title)

if __name__ == "__main__":
    main()
