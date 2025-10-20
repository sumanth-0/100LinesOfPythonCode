import requests
import time

# Fetch response.
response = requests.get("http://www.official-joke-api.appspot.com/random_joke")

# Print the joke if response was successfully fetched.
if response.status_code == 200:
    data = response.json()  # Parses the JSON response
    print(data["setup"], "💭")
    time.sleep(0.7)
    print("... 🤔")
    time.sleep(1.5)
    print(data["punchline"])
    print("😝")
else:
    print(f"Error: {response.status_code}")