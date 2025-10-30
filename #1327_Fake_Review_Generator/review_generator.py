import random

# --- Vocabulary Lists ---
# Adjectives used for positive/negative descriptions
ADJECTIVES = [
    "fantastic", "terrible", "sturdy", "flimsy", "sleek", "clunky", 
    "amazing", "disappointing", "bright", "dull", "essential", 
    "optional", "superb", "mediocre", "revolutionary", "obsolete"
]

# Nouns representing products or components
NOUNS = [
    "widget", "gizmo", "thingamajig", "unit", "assembly", "device", 
    "container", "accessory", "gadget", "system", "module", "bracket"
]

# Verbs used in action phrases
VERBS = [
    "exceeded", "barely met", "destroyed", "fulfilled", "simplified", 
    "complicated", "revolutionized", "maintained", "improved"
]

# Review sentence structures
TEMPLATES = [
    "This {adj1} {noun} {verb} my expectations. I highly recommend it.",
    "I was shocked by how {adj1} and {adj2} this {noun} is for the price.",
    "A must-have for anyone who needs a {adj1} {noun}.",
    "The {noun} is {adj1}, but the {noun} component feels {adj2}.",
    "Wish I had bought this {adj1} {noun} sooner! It {verb} my daily routine.",
    "Honestly, it's pretty {adj1}. Don't waste your money on this {adj2} {noun}.",
    "It works, but nothing {adj1} about it. Just {verb} what was advertised."
]

# --- Core Function ---

def generate_review():
    """Generates a single fake product review using random selections."""
    
    # Select random words and template
    adj1 = random.choice(ADJECTIVES)
    # Ensure adj1 and adj2 are different for better variety
    adj2 = random.choice([a for a in ADJECTIVES if a != adj1]) 
    noun1 = random.choice(NOUNS)
    noun2 = random.choice([n for n in NOUNS if n != noun1])
    verb = random.choice(VERBS)
    template = random.choice(TEMPLATES)

    # Use a dictionary to safely format the template string
    review_parts = {
        'adj1': adj1,
        'adj2': adj2,
        'noun': noun1,  # Use noun1 as the main subject
        'noun_comp': noun2, # Use noun2 for a secondary component
        'verb': verb
    }

    # Format the template, handling cases where only 'noun' is used
    # This uses the .format() method and relies on the template structure
    try:
        review = template.format(
            adj1=adj1,
            adj2=adj2,
            noun=noun1,
            verb=verb
        )
    except KeyError:
        # Handle template that only uses a subset of words (e.g., only adj1, noun, verb)
        review = template.format(**review_parts) 

    # Capitalize the first letter for proper sentence structure
    return review[0].upper() + review[1:]

# --- Execution ---

if __name__ == "__main__":
    # Define how many reviews to generate
    NUM_REVIEWS = 5
    
    print(f"\n--- Generating {NUM_REVIEWS} Fake Product Reviews ---\n")
    
    for i in range(1, NUM_REVIEWS + 1):
        review = generate_review()
        print(f"Review {i}: {review}\n")

    print("--------------------------------------------------\n")
    print("Tip: Change NUM_REVIEWS or the word lists to generate more content!")