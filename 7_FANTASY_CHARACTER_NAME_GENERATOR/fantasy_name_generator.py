import random

# Define name segments for different character types
NAME_PARTS = {
    "wizard": ["Al", "El", "Mar", "Xan", "Val", "Tor", "Zeph"],
    "warrior": ["Rok", "Thar", "Gra", "Fen", "Zur", "Mor", "Kar"],
    "elf": ["Ae", "Lia", "Eri", "Sal", "Val", "Cel", "Nym"]
}

NAME_SUFFIXES = {
    "wizard": ["dor", "sor", "nius", "las", "thor", "thos"],
    "warrior": ["gan", "mir", "gorn", "farn", "roth", "lorn"],
    "elf": ["wyn", "iel", "thal", "lis", "thea", "riel"]
}

def generate_name(character_type, length=2):
    if character_type not in NAME_PARTS:
        print("Invalid character type. Choose from wizard, warrior, or elf.")
        return None
    
    name_parts = random.choice(NAME_PARTS[character_type])
    suffix = random.choice(NAME_SUFFIXES[character_type])
    name = name_parts + suffix
    
    if length == 3:  # Add an extra syllable for longer names
        extra_part = random.choice(NAME_PARTS[character_type])
        name = extra_part + name
    
    return name.capitalize()

def main():
    print("Fantasy Character Name Generator\n")
    character_type = input("Choose character type (wizard, warrior, elf): ").strip().lower()
    length = input("Choose name length (2 for short, 3 for long): ").strip()
    length = int(length) if length in ("2", "3") else 2
    
    name = generate_name(character_type, length)
    if name:
        print(f"Generated Name: {name}")

if __name__ == "__main__":
    main()
