import requests
import json

def fetch_pokemon_details(pokemon_name):
    """Fetch and return Pokémon details from PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_details(data):
    """Display key Pokémon details."""
    if not data:
        return
    
    print(f"\n--- {data['name'].title()} ---")
    print(f"ID: {data['id']}")
    print(f"Height: {data['height']} decimetres")
    print(f"Weight: {data['weight']} hectograms")
    print("Types:")
    for type_info in data['types']:
        print(f"  - {type_info['type']['name'].title()}")
    print("Abilities:")
    for ability_info in data['abilities']:
        ability = ability_info['ability']['name']
        hidden = " (Hidden)" if ability_info['is_hidden'] else ""
        print(f"  - {ability.title()}{hidden}")
    
    # Base stats
    print("Base Stats:")
    for stat in data['stats']:
        print(f"  {stat['stat']['name'].title()}: {stat['base_stat']}")

def main():
    print("Pokémon Details Fetcher")
    pokemon_name = input("Enter Pokémon name (e.g., 'pikachu'): ").strip()
    if not pokemon_name:
        print("No name provided.")
        return
    
    data = fetch_pokemon_details(pokemon_name)
    if data:
        display_details(data)
    else:
        print("Failed to fetch details.")

if __name__ == "__main__":
    main()
