import requests
import json
import sys
from typing import Optional 


def get_ip_geolocation(ip_address: Optional[str]) -> None:
    """
    Fetches and prints geolocation details for a given IP address
    by querying the stable ip-api.com web service.

    Args:
        ip_address: The IP address string to look up. If an empty string 
                    or None is provided, it returns the public IP of the 
                    machine running the script.
    """
    
    
    API_URL = f"http://ip-api.com/json/{ip_address or ''}" 
    
    lookup_target = ip_address if ip_address else 'Current Machine IP'
    print(f"\nSearching for location data for: {lookup_target}...")
    
    try:
        # Request data from the API with a timeout
        response = requests.get(API_URL, timeout=5)
        
        # Will raise an exception for HTTP errors (like 429 Too Many Requests)
        response.raise_for_status() 
        
        data = response.json()
        
        # Check for failure status specific to the IP-API service
        if data.get("status") == "fail":
            print(f"Error: Lookup failed. Reason: {data.get('message', 'Invalid query or reserved IP.')}", file=sys.stderr)
            return
            
        print("\n--- Location Found! ---")
        # Extract and print details using .get() for safety
        print(f"  IP Address:    {data.get('query', 'N/A')}")
        print(f"  City:          {data.get('city', 'N/A')}")
        print(f"  Region/State:  {data.get('regionName', 'N/A')}")
        print(f"  Country:       {data.get('country', 'N/A')}")
        print(f"  Coordinates:   Lat {data.get('lat', 'N/A')}, Lon {data.get('lon', 'N/A')}")
        print(f"  Time Zone:     {data.get('timezone', 'N/A')}")
        print(f"  Provider:      {data.get('isp', 'N/A')}")
        print("-----------------------")

    # Handle network issues (connection failure, timeout, HTTP error)
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork Error: Could not connect or request failed. ({e.__class__.__name__})", file=sys.stderr)
    # Handle data parsing issues (if response is not valid JSON)
    except json.JSONDecodeError:
        print("\nAPI Response Error: Data received was invalid JSON.", file=sys.stderr)


if __name__ == "__main__":
    user_input = input("Which IP should I check? (Hit Enter for your own IP): ").strip()
    get_ip_geolocation(user_input)