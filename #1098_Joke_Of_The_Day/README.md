# Random Joke Fetcher

A simple Python script that fetches a random joke from the **[Official Joke API](https://official-joke-api.appspot.com/)** and displays it interactively.

---

##  Overview

This script uses the `requests` and `json` libraries to retrieve a random joke from the internet.  
It prints the setup first, waits for you to press **Enter**, and then reveals the punchline — perfect for a quick laugh in the terminal!

---

##  Features

- Fetches a **random joke** from a public API  
- Handles **network errors** and **invalid responses** gracefully  
- Uses **interactive input** for a fun reveal  
- Simple and beginner-friendly Python example for working with APIs

---

## Requirements

Make sure you have Python 3 installed.  
You also need to install the required dependency:

```bash
pip install requests
```
Usage:
Clone or download this script.

Run the script using:

```
bash
```
Copy code , paste it, then run
```
python joke_fetcher.py
```
You’ll see the setup first, then press Enter to reveal the punchline!

Example Output 
```
— JOKE OF THE DAY —
--------------------
SETUP: Why did the scarecrow win an award?
...Press Enter for the punchline...
PUNCHLINE: Because he was outstanding in his field!
--------------------
```
 Error Handling :

The script handles:

Network connection issues

Invalid API responses

JSON decoding errors

All errors are printed to stderr for better debugging.

Code Structure :

python
```
def get_joke(api_url="https://official-joke-api.appspot.com/random_joke"):
    """Fetches a random joke from the specified API endpoint."""
```
API call: Uses requests.get()

Error handling: Catches RequestException, JSONDecodeError, and general exceptions

Output: Prints setup and punchline interactively