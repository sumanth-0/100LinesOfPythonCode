import requests

def get_routes(api_key, start_location, end_location):
    url = f"https://api.publictransport.com/v1/routes?start={start_location}&end={end_location}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('routes', [])
    else:
        print("Error fetching data from API")
        return []

def display_routes(routes):
    if not routes:
        print("No routes found.")
        return
    
    for idx, route in enumerate(routes, start=1):
        print(f"Route {idx}:")
        for leg in route.get('legs', []):
            print(f"  Mode: {leg['mode']}")
            print(f"  Departure: {leg['departure']}")
            print(f"  Arrival: {leg['arrival']}")
            print(f"  Duration: {leg['duration']}")
            print()

def main():
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    start_location = input("Enter the start location: ")
    end_location = input("Enter the end location: ")
    
    print("Fetching routes...")
    routes = get_routes(api_key, start_location, end_location)
    display_routes(routes)

if __name__ == "__main__":
    main()
