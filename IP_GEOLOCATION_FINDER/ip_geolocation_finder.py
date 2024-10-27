import requests

def get_geolocation(ip_address):
    """Fetch geolocation data for the given IP address."""
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data. Please check the IP address and try again.")
        return None

def display_geolocation(data):
    """Display the geolocation data in a user-friendly format."""
    if data:
        print(f"IP Address: {data.get('ip', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"Postal Code: {data.get('postal', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")

def main():
    """Main function to run the IP Geolocation Finder."""
    ip_address = input("Enter the IP address to find its geolocation: ")
    data = get_geolocation(ip_address)
    display_geolocation(data)

if __name__ == "__main__":
    main()
