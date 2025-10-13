import random

def generate_username():
    """Generate a random gamer-style username."""
    adjectives = [
        "Shadow", "Crimson", "Cyber", "Silent", "Frost", "Toxic", "Neon",
        "Vortex", "Venom", "Dark", "Phantom", "Blaze", "Inferno", "Storm",
        "Pixel", "Quantum", "Retro", "Omega", "Lunar", "Arcane"
    ]

    nouns = [
        "Knight", "Ninja", "Reaper", "Hunter", "Rogue", "Glitch", "Specter",
        "Drifter", "Sniper", "Ghost", "Pirate", "Wizard", "Titan", "Guardian",
        "Nomad", "Rider", "Blazer", "Walker", "Breaker", "Seeker"
    ]

    number = str(random.randint(10, 999))
    separator = random.choice(["", "_", ".", "-"])
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    username = f"{adjective}{separator}{noun}{number}"
    return username


if __name__ == "__main__":
    print("🎮 Random Gamer Username Generator 🎮")
    for _ in range(5):
        print(generate_username())
