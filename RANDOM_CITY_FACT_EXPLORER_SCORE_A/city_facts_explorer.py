import random

# Sample city facts database
city_facts = {
    "New York": {
        "population": "8.6 million",
        "attractions": ["Statue of Liberty", "Central Park", "Times Square"],
        "history": "Founded in 1624 as a trading post by the Dutch."
    },
    "Tokyo": {
        "population": "9.3 million",
        "attractions": ["Shibuya Crossing", "Tokyo Tower", "Senso-ji Temple"],
        "history": "Originally a small fishing village named Edo, it became the capital in 1868."
    },
    "Paris": {
        "population": "2.1 million",
        "attractions": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral"],
        "history": "Founded in the 3rd century BC, it became a major European city in the 12th century."
    },
    "Cairo": {
        "population": "9.5 million",
        "attractions": ["Pyramids of Giza", "The Sphinx", "Egyptian Museum"],
        "history": "Founded in 969 AD, it became the capital of Egypt and a major center of learning."
    },
    "Sydney": {
        "population": "5.3 million",
        "attractions": ["Sydney Opera House", "Harbour Bridge", "Bondi Beach"],
        "history": "Established in 1788, it is the oldest continuously inhabited European settlement in Australia."
    }
}

def get_random_city_fact():
    """Generate a random city fact."""
    city = random.choice(list(city_facts.keys()))
    fact = city_facts[city]
    return city, fact

def main():
    city, fact = get_random_city_fact()
    print(f"City: {city}")
    print(f"Population: {fact['population']}")
    print(f"Attractions: {', '.join(fact['attractions'])}")
    print(f"History: {fact['history']}")

if __name__ == "__main__":
    main()
