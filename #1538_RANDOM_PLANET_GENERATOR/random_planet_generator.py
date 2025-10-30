#!/usr/bin/env python3
"""
🌠 Fictional Planet Generator 🪐
Generates random planets with emoji themes and fun stats.
"""

import random
import string
import time

# -------------------------------
# Emoji Themes 🌌
# -------------------------------
EMOJIS = ["🌍", "🪐", "🌌", "☄️", "💫", "🧬", "🌠", "🌙", "🌟", "🚀", "🔥", "🛰️"]
E = lambda: random.choice(EMOJIS)

# -------------------------------
# Data pools
# -------------------------------
prefixes = ["Zy", "Va", "Kor", "Lun", "Prox", "Ere", "Tau", "Neph", "Ar", "Sol"]
middles = ["th", "ra", "on", "ex", "li", "qu", "za", "pho", "mi", "tor"]
suffixes = ["os", "a", "is", "ar", "on", "ea", "ium", "ara", "or", "en"]

planet_types = [
    "Terrestrial", "Gas Giant", "Ice World", "Ocean Planet",
    "Desert Planet", "Lava Planet", "Jungle World", "Barren Rock"
]

atmospheres = [
    "Nitrogen-Oxygen", "Methane", "Carbon Dioxide", "Hydrogen-Helium",
    "Ammonia", "Sulfuric", "Thin", "None"
]

life_forms = ["None", "Microbial", "Plant", "Animal", "Intelligent"]

# -------------------------------
# Helpers
# -------------------------------
def generate_name():
    return random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)

def random_stat(base, variance):
    return round(random.uniform(base - variance, base + variance), 2)

def generate_planet():
    """Generate one random planet profile."""
    name = generate_name()
    p_type = random.choice(planet_types)
    atmosphere = random.choice(atmospheres)
    gravity = random_stat(1.0, 0.8)
    temperature = random.randint(-200, 500)
    radius = random.randint(1000, 70000)
    life = random.choices(life_forms, weights=[40, 25, 15, 10, 5])[0]
    moons = random.randint(0, 10)
    habitability = max(0, min(100, 100 - abs(temperature - 15)/5 - abs(gravity - 1)*20))
    return {
        "Name": name,
        "Type": p_type,
        "Atmosphere": atmosphere,
        "Gravity (g)": gravity,
        "Temperature (°C)": temperature,
        "Radius (km)": radius,
        "Moons": moons,
        "Life": life,
        "Habitability (%)": round(habitability, 1)
    }

def display_planet(p):
    """Pretty-print a planet's stats with random emojis."""
    print(f"\n{E()}  Planet: {p['Name']} {E()}")
    print("-" * 40)
    for k, v in p.items():
        if k != "Name":
            print(f"{E()} {k:<18}: {v}")
    print("-" * 40)

# -------------------------------
# Main
# -------------------------------
def main():
    theme = E()
    print(f"{theme} Fictional Planet Generator {E()}\n")
    n = input("How many planets to generate? (default 3): ").strip()
    n = int(n) if n.isdigit() else 3

    for i in range(n):
        planet = generate_planet()
        display_planet(planet)
        if i < n - 1:
            time.sleep(0.5)

    print(f"\n{E()} Exploration complete. Safe travels, explorer! {E()}")

if __name__ == "__main__":
    main()
