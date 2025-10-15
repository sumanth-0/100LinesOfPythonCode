import requests
import time
import itertools
import sys

def fetch_joke():
    """Fetch a random joke from the Official Joke API."""
    try:
        response = requests.get("https://official-joke-api.appspot.com/jokes/random", timeout=5)
        response.raise_for_status()
        joke = response.json()
        return joke['setup'], joke['punchline']
    except requests.RequestException:
        return "Why did the programmer quit his job?", "Because he didn't get arrays."

def animated_wait(duration=3):
    """Show a spinning animation in the terminal for a given duration."""
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(next(spinner))  # write the next spinner character
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')  # backspace to overwrite

def main():
    setup, punchline = fetch_joke()
    print("\nHere's a joke for you:\n")
    
    # Show the setup
    print(setup)
    
    # Animated suspense before the punchline
    animated_wait(duration=3)
    
    # Reveal punchline
    print(punchline)

if __name__ == "__main__":
    main()
