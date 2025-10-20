import requests
import random

def fetch_poem_by_theme(theme):
    """Fetch a poem that includes the theme keyword using PoetryDB API."""
    try:
        # Search poems that contain the theme word
        url = f"https://poetrydb.org/lines/{theme}"
        response = requests.get(url)
        data = response.json()

        if not data or isinstance(data, dict) and "status" in data:
            print(f"\n❌ No poem found with the theme '{theme}'. Try another word.")
            return

        # Pick a random poem from the results
        poem = random.choice(data)
        title = poem.get("title", "Untitled")
        author = poem.get("author", "Unknown")
        lines = poem.get("lines", [])

        print(f"\n📜 {title} — {author}\n")
        for line in lines[:min(8, len(lines))]:
            print(line)
        print("\n~ End ~\n")

    except Exception as e:
        print(f"⚠️ Error fetching poem: {e}")

if __name__ == "__main__":
    theme = input("Enter a theme or keyword (e.g. love, rain, night): ").strip()
    fetch_poem_by_theme(theme)
