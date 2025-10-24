import requests
import time

def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        setup = joke.get("setup")
        punchline = joke.get("punchline")

        print(setup)
        time.sleep(3)  # wait 3 seconds for comedic timing
        print(punchline)
    else:
        print("Failed to fetch a joke 😅")

if __name__ == "__main__":
    get_random_joke()
