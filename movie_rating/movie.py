import requests
import argparse
import sys

# Replace with your OMDb API key
API_KEY = "your_key_here"
API_URL = "http://www.omdbapi.com/"

def fetch_movie_rating(title: str):
    try:
        params = {
            "t": title,
            "apikey": API_KEY
        }
        res = requests.get(API_URL, params=params)
        res.raise_for_status()
        data = res.json()

        if data.get("Response", "False") == "False":
            print(f"Movie not found: {title}")
            return

        print(f"\nTitle: {data.get('Title', 'N/A')}")
        print(f"Year: {data.get('Year', 'N/A')}")
        print(f"IMDb Rating: {data.get('imdbRating', 'N/A')}/10")
        print(f"Genre: {data.get('Genre', 'N/A')}")
        print(f"Director: {data.get('Director', 'N/A')}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Movie Ratings CLI — Fetch IMDb ratings for any movie")
    parser.add_argument("title", help="Movie title to look up")
    args = parser.parse_args()

    fetch_movie_rating(args.title)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        title = input("Enter movie title: ").strip()
        fetch_movie_rating(title)
    else:
        main()

