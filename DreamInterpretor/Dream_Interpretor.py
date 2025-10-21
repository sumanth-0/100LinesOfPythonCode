import random
import re

# Dream symbols and their funny, random symbolic meanings
SYMBOLS = {
    'flying': [
        "You're about to get a surprise promotion... or just need to lay off the hot sauce before bed.",
        "Symbolizes your desire to escape chores—next time, dream of a vacuum that flies itself.",
        "Means you're ready to soar in life, but watch out for that low-hanging power line of regret."
    ],
    'teeth falling out': [
        "A sign that you need to floss more... or less dramatically in conversations.",
        "Indicates upcoming awkward small talk at parties—practice your gum-chewing escape plan.",
        "Foretells a dental bill or a plot twist where you become a pirate (arrr, gold teeth!)."
    ],
    'chased': [
        "You're being pursued by unpaid bills—run faster or negotiate with the abstract monster.",
        "Suggests your subconscious is late for a meeting; tell it to set an alarm.",
        "Means adventure awaits, but it's the kind where you trip over your own shoelaces hilariously."
    ],
    'naked': [
        "Time to bare your soul... or just buy clothes that don't shrink in the wash.",
        "Symbol of vulnerability—embrace it by streaking through your to-do list.",
        "Predicts a wardrobe malfunction or finally admitting you love bad puns."
    ],
    'water': [
        "Emotions are flowing—build a dam with dad jokes to stay afloat.",
        "Indicates a splashy romance or that you left the faucet running again.",
        "Foreshadows a pool party invite... from your inner fish self."
    ],
    'falling': [
        "You're dropping the ball on self-care—catch it with a nap trampoline.",
        "Sign of letting go of grudges, but maybe not from actual heights.",
        "Predicts a freefall into fun, unless it's just your phone slipping mid-scroll."
    ],
    'snake': [
        "Wisdom incoming, or your ex texting at 2 AM—hiss-tory repeating?",
        "Symbolizes transformation: shedding skin like old memes.",
        "Means temptation—resist by not eating the whole pizza in one dream bite."
    ],
    'house': [
        "Your mind's mansion needs dusting—evict those cobwebby worries.",
        "Represents stability, or that leaky roof you keep ignoring IRL.",
        "Foretells home improvements... starting with dream-proof windows."
    ]
}

def detect_symbols(dream_text):
    """Detect common dream symbols in the text."""
    text_lower = dream_text.lower()
    detected = []
    for symbol, _ in SYMBOLS.items():
        if re.search(rf'\b{symbol}\b', text_lower):
            detected.append(symbol)
    if not detected:
        # Random fallback if no symbols
        detected.append(random.choice(list(SYMBOLS.keys())))
    return detected

def interpret_dream(dream_text):
    """Generate a funny interpretation."""
    symbols = detect_symbols(dream_text)
    interpretations = []
    for symbol in random.sample(symbols, min(2, len(symbols))):  # Pick 1-2
        interp = random.choice(SYMBOLS[symbol])
        interpretations.append(f"- {symbol.title()}: {interp}")
    
    overall = random.choice([
        "Overall, your dream screams 'life hack: more naps, fewer worries!'",
        "In summary, your subconscious is a stand-up comedian—book it for open mic.",
        "Big picture: Embrace the chaos; it's just your brain's fanfic gone wild."
    ])
    
    return "\n".join(interpretations) + f"\n\n{overall}"

def main():
    print("Funny Dream Interpreter")
    dream = input("Describe your dream: ").strip()
    if not dream:
        print("No dream? Sweet dreams of unicorns then!")
        return
    
    interpretation = interpret_dream(dream)
    print(f"\nYour Dream Interpretation:\n{interpretation}")

if __name__ == "__main__":
    main()
