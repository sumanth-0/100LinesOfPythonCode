#!/usr/bin/env python3
"""
AI Dungeon Master - A Text-Based RPG Game
A simple AI-powered dungeon master that generates scenarios and handles player actions.
"""

import random
import re

# Game state and configuration
PLAYER = {"hp": 100, "gold": 50, "inventory": ["sword", "potion"]}

# Scenario templates for dynamic story generation
SCENARIOS = [
    "You enter a {adj} {location}. A {creature} {action}!",
    "A {adj} {character} approaches you in the {location}.",
    "You discover a {adj} {object} in the {location}.",
    "Strange {sound} echo through the {location}."
]

ADJECTIVES = ["dark", "mysterious", "ancient", "glowing", "cursed", "forgotten"]
LOCATIONS = ["dungeon", "forest", "cave", "castle", "temple", "ruins"]
CREATURES = ["goblin", "dragon", "skeleton", "wolf", "troll", "ghost"]
ACTIONS = ["attacks you", "blocks your path", "guards treasure", "demands tribute"]
CHARACTERS = ["merchant", "wizard", "knight", "thief", "hermit"]
OBJECTS = ["chest", "sword", "amulet", "scroll", "potion"]
SOUNDS = ["whispers", "footsteps", "howls", "chains rattling"]

def generate_scenario():
    """Generate a random scenario using templates."""
    template = random.choice(SCENARIOS)
    return template.format(
        adj=random.choice(ADJECTIVES),
        location=random.choice(LOCATIONS),
        creature=random.choice(CREATURES),
        action=random.choice(ACTIONS),
        character=random.choice(CHARACTERS),
        object=random.choice(OBJECTS),
        sound=random.choice(SOUNDS)
    )

def handle_action(action, scenario):
    """Process player actions and return outcomes."""
    action = action.lower()
    
    if re.search(r"attack|fight|strike", action):
        if random.random() > 0.5:
            PLAYER["gold"] += random.randint(10, 30)
            return f"You defeated the enemy! Gained {PLAYER['gold'] - 50} gold."
        else:
            damage = random.randint(10, 30)
            PLAYER["hp"] -= damage
            return f"You took {damage} damage! HP: {PLAYER['hp']}"
    
    elif re.search(r"run|flee|escape", action):
        return "You escape safely and continue your journey."
    
    elif re.search(r"talk|speak|negotiate", action):
        if "character" in scenario or "merchant" in scenario:
            return "The character offers you information about nearby treasure."
        return "There's no one to talk to here."
    
    elif re.search(r"search|explore|investigate", action):
        if random.random() > 0.6:
            item = random.choice(["potion", "gold coin", "map", "key"])
            PLAYER["inventory"].append(item)
            return f"You found a {item}!"
        return "You found nothing of interest."
    
    elif re.search(r"heal|potion|rest", action):
        if "potion" in PLAYER["inventory"]:
            PLAYER["hp"] = min(100, PLAYER["hp"] + 30)
            PLAYER["inventory"].remove("potion")
            return f"You healed! HP: {PLAYER['hp']}"
        return "You don't have any potions."
    
    return "You pause and observe your surroundings carefully."

def display_status():
    """Display player status."""
    return f"\nHP: {PLAYER['hp']} | Gold: {PLAYER['gold']} | Items: {', '.join(PLAYER['inventory'])}"

def main():
    """Main game loop."""
    print("=== AI DUNGEON MASTER ===")
    print("Commands: attack, run, talk, search, heal, status, quit")
    print("Type your actions in natural language!\n")
    
    while PLAYER["hp"] > 0:
        scenario = generate_scenario()
        print(f"\n{scenario}")
        print(display_status())
        
        action = input("\nWhat do you do? > ")
        
        if action.lower() in ["quit", "exit", "q"]:
            print("Thanks for playing!")
            break
        
        outcome = handle_action(action, scenario)
        print(f"\n>>> {outcome}")
        
        if PLAYER["hp"] <= 0:
            print("\n💀 You have been defeated! Game Over.")
            break

if __name__ == "__main__":
    main()
