import requests
import json
import sys

def get_joke(api_url="https://official-joke-api.appspot.com/random_joke"):
    """Fetches a random joke from the specified API endpoint."""
    try:
        # Make the GET request to the API
        response = requests.get(api_url)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status() 
        
        # Parse the JSON response
        data = response.json()
        
        # The Official Joke API returns a dictionary with 'setup' and 'punchline' keys
        setup = data.get("setup")
        punchline = data.get("punchline")
        
        if setup and punchline:
            # Print the joke parts clearly
            print("\n— JOKE OF THE DAY —")
            print("-" * 20)
            print(f"SETUP: {setup}")
            # The punchline is hidden until the user presses Enter
            input("...Press Enter for the punchline...") 
            print(f"PUNCHLINE: {punchline}")
            print("-" * 20)
        else:
            print("Error: Could not find joke content in the API response.")
            # Print the whole response for debugging
            # print(data) 

    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}", file=sys.stderr)
        print("Please check your internet connection.", file=sys.stderr)
    except json.JSONDecodeError:
        print("Error: Could not decode JSON response from API.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    get_joke()