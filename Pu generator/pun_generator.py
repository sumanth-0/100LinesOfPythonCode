import random

# Pun data: base phrases with substitution targets and puns
PUNS = [
    {
        "base": "What do you call a {sub} noodle? An impasta!",
        "sub": "fake",
        "pun": "What do you call a fake noodle? An impasta!"
    },
    {
        "base": "I'm on a {sub} diet. I've lost three days already.",
        "sub": "seafood",
        "pun": "I'm on a seafood diet. I've lost three days already."
    },
    {
        "base": "Why don't {sub} play hide and seek? Because good luck hiding when you're always spotted!",
        "sub": "dalmatian",
        "pun": "Why don't dalmatians play hide and seek? Because good luck hiding when you're always spotted!"
    },
    {
        "base": "I used to be a {sub}, but I couldn't find a good conductor.",
        "sub": "baker",
        "pun": "I used to be a baker, but I couldn't find a good conductor."  # Wait, better: actually "I used to play piano by ear, but now I use my hands."
    },
    # More puns
    {
        "base": "Time flies like an arrow. Fruit flies like a {sub}.",
        "sub": "banana",
        "pun": "Time flies like an arrow. Fruit flies like a banana."
    },
    {
        "base": "Why did the {sub} go to art school? To draw a better 'line'!",
        "sub": "scarecrow",
        "pun": "Why did the scarecrow go to art school? To draw a better 'line'!"
    },
    {
        "base": "I'm reading a book on anti-{sub}. I can't put it down!",
        "sub": "gravity",
        "pun": "I'm reading a book on anti-gravity. I can't put it down!"
    },
    {
        "base": "What do you call cheese that isn't yours? {sub}!",
        "sub": "Nacho",
        "pun": "What do you call cheese that isn't yours? Nacho!"
    },
    {
        "base": "Why don't {sub} ever get lost? They always follow the 'current'!",
        "sub": "fish",
        "pun": "Why don't fish ever get lost? They always follow the 'current'!"
    },
    {
        "base": "I told my wife she was drawing her eyebrows too high. She looked {sub}.",
        "sub": "surprised",
        "pun": "I told my wife she was drawing her eyebrows too high. She looked surprised."
    }
]

# Homophone pairs for dynamic substitutions
HOMOPHONES = [
    ("pair", "pear"),
    ("right", "write"),
    ("knight", "night"),
    ("sole", "soul"),
    ("dear", "deer"),
    ("flour", "flower"),
    ("peace", "piece"),
    ("plain", "plane"),
    ("raise", "raze"),
    ("suite", "sweet")
]

def generate_static_pun():
    """Pick a random static pun."""
    pun_data = random.choice(PUNS)
    return pun_data["pun"]

def generate_dynamic_pun():
    """Generate a pun by substituting a homophone in a base sentence."""
    base_sentences = [
        "I bought a new {sub}. It's perfect for the garden!",
        "The {sub} was very important to the story.",
        "We need to {sub} the old building to make way for the new one.",
        "The hotel {sub} was beautifully decorated.",
        "My {sub} friend sent me a letter."
    ]
    sent = random.choice(base_sentences)
    word, sub = random.choice(HOMOPHONES)
    pun_sent = sent.format(sub=sub)
    explanation = f"(Pun on '{word}' vs '{sub}')"
    return f"{pun_sent} {explanation}"

def generate_puns(num_puns=5):
    """Generate a mix of static and dynamic puns."""
    puns = []
    for _ in range(num_puns):
        if random.random() < 0.7:  # 70% static
            puns.append(generate_static_pun())
        else:
            puns.append(generate_dynamic_pun())
    return puns

def main():
    print("Random Pun Generator")
    try:
        num = int(input("How many puns? (default 5): ").strip() or "5")
    except ValueError:
        num = 5
    
    if num <= 0:
        print("No puns? That's a crime against humor!")
        return
    
    puns = generate_puns(num)
    print(f"\nHere are {num} random puns:\n")
    for i, pun in enumerate(puns, 1):
        print(f"{i}. {pun}")
        print()

if __name__ == "__main__":
    main()
