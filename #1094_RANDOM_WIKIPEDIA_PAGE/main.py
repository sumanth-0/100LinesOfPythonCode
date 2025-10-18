import requests
import tkinter as tk

def fetch_random_wikipedia_page():
    URL = "https://en.wikipedia.org/w/api.php"

    # Get random page from Wikipedia
    PARAMS_RANDOM = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,
        "rnlimit": 1
    }

    HEADERS = {
        "User-Agent": "RandomWikipediaPage/1.0 (https://github.com/alexdimmock95)"
    }
    try:
        R = requests.get(url=URL, params=PARAMS_RANDOM, headers=HEADERS)
        print(R.url)

        DATA = R.json()

        random_page = DATA["query"]["random"][0]
        title = random_page["title"]

        # Get first paragraph of the random page
        PARAMS_EXTRACT = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True
        }
        R2 = requests.get(URL, params=PARAMS_EXTRACT, headers=HEADERS)
        DATA2 = R2.json()
        pages = DATA2["query"]["pages"]
        page_content = next(iter(pages.values()))

        # Update UI
        title_label.config(text=page_content["title"])
        extract_text.delete("1.0", tk.END)
        extract_text.insert(tk.END, page_content["extract"])

    except Exception as e:
        title_label.config(text="Error fetching page")
        extract_text.delete("1.0", tk.END)
        extract_text.insert(tk.END, str(e))

# --- Main Window ---
root = tk.Tk()
root.title("Random Wikipedia Page")
root.geometry("600x400")

# --- Widgets ---
title_label = tk.Label(root, text="Press 'Get Random Page'", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

extract_text = tk.Text(root, wrap="word", height=15, width=70)
extract_text.pack(padx=10, pady=10)

fetch_button = tk.Button(root, text="Get Random Page", command=fetch_random_wikipedia_page)
fetch_button.pack(pady=10)

# --- Run App ---
root.mainloop()