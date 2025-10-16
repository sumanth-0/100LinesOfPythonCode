import requests
import random

def get_random_fact():
    try:
        # Using a free fun facts API
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
        response.raise_for_status()  # Check for errors
        data = response.json()
        print("\n🎲 Random Fun Fact:")
        print(data['text'])
    except Exception as e:
        print("⚠️ Couldn't fetch a fun fact, showing one from local list instead.\n")
        # Fallback local list of facts
        local_facts = [
            "Honey never spoils — archaeologists found 3000-year-old honey still edible!",
            "Bananas are berries, but strawberries aren’t!",
            "Octopuses have three hearts.",
            "A group of flamingos is called a flamboyance.",
            "Your brain uses about 20% of your body’s oxygen and calories."
        ]
        print(random.choice(local_facts))

if __name__ == "__main__":
    print("🌍 Welcome to the Random Fun Fact Fetcher!")
    get_random_fact()
