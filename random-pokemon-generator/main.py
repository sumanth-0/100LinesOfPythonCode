import requests
import random
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_data(pokemon_id):
    """Fetch raw Pokémon data by ID."""
    response = requests.get(f"{API_URL}{pokemon_id}")
    response.raise_for_status()
    return response.json()

def parse_pokemon_data(data):
    """Extract name, types, stats, and image URL from Pokémon data."""
    name = data['name'].capitalize()
    types = [type_info['type']['name'].capitalize() for type_info in data['types']]
    stats = {stat_info['stat']['name']: stat_info['base_stat'] for stat_info in data['stats']}
    image_url = data['sprites']['front_default']
    return {
        "Name": name,
        "Types": types,
        "Stats": stats,
        "Image URL": image_url
    }

def get_random_pokemon():
    """Generate a random Pokémon ID and retrieve parsed data."""
    random_id = random.randint(1, 1000)
    raw_data = get_pokemon_data(random_id)
    return parse_pokemon_data(raw_data)

def display_pokemon():
    """Fetch and display a random Pokémon in the Tkinter GUI."""
    try:
        pokemon_data = get_random_pokemon()
        
        name_label.config(text=f"Name: {pokemon_data['Name']}", font=("Arial", 12, "bold"))
        types_label.config(text=f"Type: {', '.join(pokemon_data['Types'])}", font=("Arial", 12, "bold"))
        
        stats_text = "\n".join([f"{stat.capitalize()}: {value}" for stat, value in pokemon_data['Stats'].items()])
        stats_label.config(text=stats_text, font=("Arial", 10), justify="center")
        
        response = requests.get(pokemon_data['Image URL'])
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((150, 150), Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        
        image_label.config(image=img_tk)
        image_label.image = img_tk  

    except requests.HTTPError as e:
        name_label.config(text=f"HTTP Error: {e}")
    except Exception as e:
        name_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Random Pokémon Generator")
root.geometry("400x450")

title_label = tk.Label(root, text="Random Pokémon Generator", font=("Arial", 16, "bold"), justify="center")
title_label.pack(pady=10)

generate_button = tk.Button(root, text="Generate", command=display_pokemon, font=("Arial", 12))
generate_button.pack(pady=10)

image_label = tk.Label(root)
image_label.pack(pady=(5, 10))  

name_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
name_label.pack(anchor="center", padx=20, pady=(5, 0))

types_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
types_label.pack(anchor="center", padx=20, pady=(5, 0))

stats_label = tk.Label(root, text="", font=("Arial", 10), justify="center")
stats_label.pack(anchor="center", padx=20, pady=(5, 0))

root.mainloop()
