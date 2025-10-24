# Book Title Generator

import random

adjectives = [
    # Appearance
    "beautiful", "elegant", "bright", "shiny", "colorful", "dark", "tall", "short", "sleek", "rugged",
    "attractive", "plain", "glossy", "sparkling", "dull", "radiant", "faded", "bulky", "slender", "graceful",

    # Personality / Emotion
    "kind", "cheerful", "brave", "honest", "stubborn", "gentle", "nervous", "patient", "ambitious", "thoughtful",
    "confident", "polite", "rude", "moody", "generous", "optimistic", "pessimistic", "loyal", "shy", "curious",

    # Intensity / Quantity
    "abundant", "scarce", "few", "many", "several", "immense", "tiny", "enormous", "slight", "significant",

    # Condition / Quality
    "clean", "dirty", "broken", "smooth", "rough", "stable", "fragile", "reliable", "efficient", "defective",
    "active", "passive", "damaged", "operational", "sturdy", "delicate", "firm", "flexible", "weak", "powerful",

    # Time / Age
    "ancient", "new", "recent", "modern", "young", "old", "early", "late", "timeless", "temporary",

    # Environment / Setting
    "noisy", "quiet", "crowded", "empty", "peaceful", "stormy", "warm", "chilly", "humid", "dry",

    # Abstract Qualities
    "creative", "logical", "innovative", "complex", "simple", "chaotic", "organized", "efficient", "consistent", "unpredictable",

    # Value / Worth
    "cheap", "expensive", "valuable", "worthless", "affordable", "luxurious", "rare", "common", "desirable", "precious",

    # Fantasy / Mystery / Mythical
    "enchanted", "mystical", "cursed", "divine", "ethereal", "ghostly", "shadowy", "magical", "mysterious",
    "sacred", "forbidden", "arcane", "legendary", "heroic", "sinister", "haunted", "hidden", "invisible",
    "fiery", "icy", "eternal", "royal", "darkened", "spectral", "luminous", "secretive", "celestial", "ancient"
]

nouns = [
    # People & Roles
    "teacher", "student", "artist", "engineer", "doctor", "manager", "child", "friend", "neighbor", "leader",

    # Places
    "city", "village", "country", "school", "office", "park", "restaurant", "mountain", "beach", "museum",

    # Objects / Things
    "book", "phone", "computer", "chair", "table", "car", "key", "lamp", "bottle", "clock",

    # Animals
    "dog", "cat", "bird", "horse", "elephant", "tiger", "lion", "fish", "rabbit", "monkey",

    # Nature
    "tree", "flower", "river", "ocean", "hill", "stone", "cloud", "rain", "sun", "wind",

    # Ideas / Abstract Concepts
    "freedom", "love", "happiness", "courage", "knowledge", "power", "truth", "success", "peace", "justice",

    # Time & Events
    "day", "night", "morning", "evening", "week", "month", "year", "festival", "meeting", "celebration",

    # Food & Drink
    "apple", "bread", "cake", "coffee", "tea", "pizza", "sandwich", "milk", "water", "chocolate",

    # Technology & Tools
    "machine", "engine", "robot", "network", "database", "software", "hardware", "screen", "cable", "keyboard",

    # Economy & Work
    "job", "company", "market", "business", "salary", "investment", "customer", "product", "service", "trade",

    # Mystery / Crime / Supernatural
    "detective", "clue", "secret", "shadow", "ghost", "whisper", "potion", "curse", "riddle", "villain",
    "mystery", "labyrinth", "mirror", "symbol", "prophecy", "assassin", "spy", "fog", "mask", "illusion",

    # Fantasy / Magic / Myth
    "dragon", "wizard", "sword", "castle", "kingdom", "elf", "dwarf", "goblin", "troll", "unicorn",
    "phoenix", "spell", "crystal", "portal", "realm", "guardian", "knight", "crown", "treasure", "spirit"
]

while(True):
    ch = int(input("Enter choice:\n1-Title\n2-Exit\n"))
    if ch == 2:
        break
    n = int(input("Enter number of titles to generate: "))
    for i in range(n):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        print(f"The {adjective.capitalize()} {noun.capitalize()}")
    print()