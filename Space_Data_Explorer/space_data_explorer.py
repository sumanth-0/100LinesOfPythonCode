import requests
from dotenv import load_dotenv
import os

load_dotenv()
nasa_api_key = os.getenv('NASA_API_KEY')
def fetch_nasa_data(endpoint, params=None):
    base_url = "https://api.nasa.gov"
    response = requests.get(f"{base_url}{endpoint}", params=params)
    response.raise_for_status()
    return response.json()

def display_picture_of_the_day():
    data = fetch_nasa_data("/planetary/apod", params={"api_key": nasa_api_key})
    print("\nPicture of the Day:")
    print(f"Title: {data['title']}")
    print(f"URL: {data['url']}")
    print(f"Explanation: {data['explanation']}")

def display_mars_rover_images(rover="Curiosity"):
    data = fetch_nasa_data(f"/mars-photos/api/v1/rovers/{rover}/photos",
                            params={"sol": 1000, "api_key": nasa_api_key})
    print(f"\nMars Rover {rover} Images:")
    for photo in data['photos'][:5]:  # Display first 5 images
        print(f"Image URL: {photo['img_src']}")

def display_near_earth_objects():
    data = fetch_nasa_data("/neo/rest/v1/neo/browse",
                            params={"api_key": nasa_api_key})
    print("\nNear Earth Objects:")
    for obj in data['near_earth_objects'][:5]:  # Display first 5 objects
        print(f"Name: {obj['name']}, Diameter (meters): {obj['estimated_diameter']['meters']['estimated_diameter_max']}")

if __name__ == "__main__":
    while True:
        user_input = input("What would you like to see? (picture, mars, asteroids, or 'done' to exit): ").strip().lower()
        
        if user_input == "done":
            print("Exiting the program.")
            break
        elif user_input == "picture":
            display_picture_of_the_day()
        elif user_input == "mars":
            display_mars_rover_images()
        elif user_input == "asteroids":
            display_near_earth_objects()
        else:
            print("Invalid option. Please try again.")
