"""
Mad Libs Generator
Create funny stories by filling in nouns, verbs, and adjectives into story templates.
Uses only Python's built-in libraries - no external dependencies required.
"""

import random
import re

# Story templates with placeholders
STORIES = [
    ("The Epic Adventure", "Once upon a time, a {adjective} {noun} decided to {verb} to the "
     "{place}. Along the way, they met a {adjective} {animal} who was {verb_ing}. Together, "
     "they found a {adjective} {object} and lived {adverb} ever after!"),
    
    ("The School Day", "Today at school, my {adjective} teacher made us {verb} for {number} hours! "
     "My friend brought a {adjective} {noun} and we decided to {verb} with it. The principal was "
     "so {emotion} that they started {verb_ing} around the {place}!"),
    
    ("The Job Interview", "I walked {adverb} into the office for my interview. The boss, a "
     "{adjective} {noun}, asked me to {verb} a {object}. I was so {emotion} that I accidentally "
     "{verb_past} on their {noun}. Surprisingly, I got the job as a professional {occupation}!"),
    
    ("The Cooking Disaster", "I decided to cook a {adjective} {food} for dinner. I added {number} "
     "cups of {noun} and started to {verb} it {adverb}. Suddenly, the {object} began {verb_ing}! "
     "My {adjective} {animal} ran into the {place} and everything was {adjective}!"),
    
    ("The Vacation", "On my vacation to {place}, I met a {adjective} {occupation} who loved to "
     "{verb}. We spent {number} days {verb_ing} and eating {adjective} {food}. It was the most "
     "{adjective} trip ever! I even brought home a {noun} as a souvenir.")
]

# Word type hints
HINTS = {
    'noun': 'thing', 'verb': 'action', 'adjective': 'describing word',
    'adverb': 'how', 'verb_ing': 'action+ing', 'verb_past': 'past action',
    'animal': 'animal', 'place': 'location', 'object': 'item',
    'emotion': 'feeling', 'food': 'food', 'occupation': 'job', 'number': 'number'
}


def get_inputs(template):
    """Gets user inputs for all placeholders in template."""
    placeholders = list(dict.fromkeys(re.findall(r'\{(\w+)\}', template)))
    inputs = {}
    print("\nFill in the words:\n")
    for p in placeholders:
        val = input(f"{p} ({HINTS.get(p, 'word')}): ").strip()
        inputs[p] = val if val else "thing"
    return inputs


def main():
    """Main function to run the Mad Libs generator."""
    print("=" * 60)
    print("🎭 MAD LIBS GENERATOR 🎭")
    print("=" * 60)
    
    # Select random story
    title, template = random.choice(STORIES)
    print(f"\nStory: {title}")
    print("-" * 60)
    
    # Get inputs and generate story
    inputs = get_inputs(template)
    story = template.format(**inputs)
    
    # Display result
    print("\n" + "=" * 60)
    print("YOUR STORY:")
    print("=" * 60)
    print(f"\n{story}\n")
    print("=" * 60)
    
    # Play again option
    if input("\nCreate another story? (y/n): ").strip().lower() == 'y':
        print("\n")
        main()


if __name__ == "__main__":
    main()