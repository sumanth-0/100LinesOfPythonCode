#!/usr/bin/env python3
"""
Fake Name Generator
Generates random human names with fake country origins.

This script generates realistic fake names using random patterns
and associates them with various countries around the world.
"""

import random
import sys

# Data for name generation
FIRST_NAMES = {
    "USA": ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth"],
    "UK": ["Oliver", "Olivia", "George", "Amelia", "Harry", "Isla", "Jack", "Ava", "Jacob", "Emily"],
    "India": ["Aarav", "Aadhya", "Vivaan", "Ananya", "Aditya", "Diya", "Arjun", "Pari", "Sai", "Navya"],
    "Japan": ["Haruto", "Yui", "Sota", "Hina", "Yuuto", "Sakura", "Hayato", "Aoi", "Ren", "Yuna"],
    "Germany": ["Ben", "Emma", "Paul", "Mia", "Jonas", "Hannah", "Leon", "Sophia", "Luca", "Anna"],
    "France": ["Louis", "Emma", "Gabriel", "Jade", "Raphael", "Louise", "Arthur", "Alice", "Lucas", "Chloe"],
    "Brazil": ["Miguel", "Alice", "Arthur", "Sophia", "Heitor", "Helena", "Bernardo", "Valentina", "Theo", "Laura"],
    "Spain": ["Hugo", "Lucia", "Martin", "Maria", "Lucas", "Sofia", "Mateo", "Martina", "Leo", "Emma"],
    "Italy": ["Leonardo", "Sofia", "Francesco", "Giulia", "Alessandro", "Aurora", "Lorenzo", "Alice", "Mattia", "Ginevra"],
    "China": ["Wei", "Fang", "Ming", "Li", "Jun", "Ying", "Jian", "Xiu", "Chen", "Mei"]
}

LAST_NAMES = {
    "USA": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"],
    "UK": ["Smith", "Jones", "Taylor", "Brown", "Williams", "Wilson", "Johnson", "Davies", "Patel", "Robinson"],
    "India": ["Kumar", "Sharma", "Patel", "Singh", "Reddy", "Gupta", "Verma", "Joshi", "Mehta", "Nair"],
    "Japan": ["Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe", "Ito", "Yamamoto", "Nakamura", "Kobayashi", "Kato"],
    "Germany": ["Müller", "Schmidt", "Schneider", "Fischer", "Weber", "Meyer", "Wagner", "Becker", "Schulz", "Hoffmann"],
    "France": ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard", "Petit", "Durand", "Leroy", "Moreau"],
    "Brazil": ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes"],
    "Spain": ["Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres"],
    "Italy": ["Rossi", "Russo", "Ferrari", "Esposito", "Bianchi", "Romano", "Colombo", "Ricci", "Marino", "Greco"],
    "China": ["Wang", "Li", "Zhang", "Liu", "Chen", "Yang", "Huang", "Zhao", "Wu", "Zhou"]
}

def generate_fake_name(country=None):
    """Generate a random fake name with country origin."""
    if country and country in FIRST_NAMES:
        selected_country = country
    else:
        selected_country = random.choice(list(FIRST_NAMES.keys()))
    
    first_name = random.choice(FIRST_NAMES[selected_country])
    last_name = random.choice(LAST_NAMES[selected_country])
    
    return f"{first_name} {last_name}", selected_country

def generate_multiple_names(count=10, country=None):
    """Generate multiple fake names."""
    names = []
    for _ in range(count):
        name, origin = generate_fake_name(country)
        names.append((name, origin))
    return names

def main():
    """Main function to run the fake name generator."""
    print("=" * 60)
    print("Fake Name Generator")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            count = 10
    else:
        count = 10
    
    country = sys.argv[2].upper() if len(sys.argv) > 2 and sys.argv[2].upper() in FIRST_NAMES else None
    
    names = generate_multiple_names(count, country)
    
    print(f"\nGenerating {count} fake name(s)...\n")
    for i, (name, origin) in enumerate(names, 1):
        print(f"{i:2d}. {name:30s} (Origin: {origin})")
    
    print("\n" + "=" * 60)
    print(f"Available countries: {', '.join(sorted(FIRST_NAMES.keys()))}")
    print("Usage: python fake_name_generator.py [count] [country]")
    print("=" * 60)

if __name__ == "__main__":
    main()
