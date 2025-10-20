#!/usr/bin/env python3
"""
Random Poem Generator
Generates random poems in various styles and lengths.
"""

import random
import argparse
import sys
from typing import List, Dict

# Poetry components and word banks
ADJECTIVES = [
    'silent', 'golden', 'silver', 'crimson', 'azure', 'gentle', 'fierce',
    'ancient', 'mystical', 'radiant', 'shadowy', 'velvet', 'crystal',
    'whispered', 'eternal', 'fleeting', 'endless', 'serene', 'turbulent',
    'fragrant', 'luminous', 'dark', 'bright', 'tender', 'wild'
]

NOUNS = [
    'moon', 'stars', 'ocean', 'mountain', 'forest', 'river', 'wind',
    'rose', 'dream', 'memory', 'shadow', 'light', 'heart', 'soul',
    'sky', 'dawn', 'dusk', 'night', 'day', 'season', 'time', 'path',
    'journey', 'love', 'hope', 'desire', 'fate'
]

VERBS = [
    'whispers', 'dances', 'flows', 'shimmers', 'blooms', 'fades',
    'awakens', 'sleeps', 'dreams', 'wanders', 'sings', 'weeps',
    'burns', 'glows', 'trembles', 'soars', 'falls', 'rises',
    'echoes', 'calls', 'reaches', 'embraces', 'remembers', 'forgets'
]

PREPOSITIONS = [
    'through', 'across', 'beneath', 'above', 'within', 'beyond',
    'among', 'between', 'under', 'over'
]

RHYME_PAIRS = [
    ('night', 'light', 'sight', 'flight'),
    ('day', 'way', 'say', 'ray'),
    ('rain', 'pain', 'gain', 'chain'),
    ('sea', 'free', 'tree', 'be'),
    ('sky', 'fly', 'high', 'sigh'),
    ('love', 'dove', 'above', 'thereof'),
    ('dream', 'stream', 'gleam', 'beam'),
    ('heart', 'part', 'art', 'start')
]


class PoemGenerator:
    """Generates random poems in various styles."""
    
    def __init__(self, seed=None):
        if seed:
            random.seed(seed)
    
    def generate_haiku(self) -> str:
        """Generate a haiku (5-7-5 syllable pattern)."""
        # Simplified haiku generation
        line1 = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)} {random.choice(VERBS)}"
        line2 = f"{random.choice(PREPOSITIONS)} the {random.choice(ADJECTIVES)} {random.choice(NOUNS)}"
        line3 = f"{random.choice(NOUNS)} {random.choice(VERBS)} {random.choice(['softly', 'gently', 'wildly'])}"
        return f"{line1}\n{line2}\n{line3}"
    
    def generate_limerick(self) -> str:
        """Generate a limerick (AABBA rhyme scheme)."""
        rhyme_set = random.choice(RHYME_PAIRS)
        adj1 = random.choice(ADJECTIVES)
        adj2 = random.choice(ADJECTIVES)
        noun1 = random.choice(NOUNS)
        noun2 = random.choice(NOUNS)
        verb1 = random.choice(VERBS)
        
        return f"""There once was a {adj1} {noun1}
That danced in the {rhyme_set[0]}
With {adj2} grace so {rhyme_set[1]}
It would {verb1} out of {rhyme_set[2]}
Until morning brought {rhyme_set[3]}"""
    
    def generate_quatrain(self) -> str:
        """Generate a quatrain (ABAB rhyme scheme)."""
        rhyme_set1 = random.choice(RHYME_PAIRS)
        rhyme_set2 = random.choice([r for r in RHYME_PAIRS if r != rhyme_set1])
        
        line1 = f"The {random.choice(ADJECTIVES)} {random.choice(NOUNS)} in the {rhyme_set1[0]}"
        line2 = f"{random.choice(VERBS).capitalize()} {random.choice(PREPOSITIONS)} the {rhyme_set2[0]}"
        line3 = f"Where {random.choice(NOUNS)} and {random.choice(NOUNS)} unite in {rhyme_set1[1]}"
        line4 = f"And {random.choice(ADJECTIVES)} {random.choice(NOUNS)} takes {rhyme_set2[1]}"
        
        return f"{line1}\n{line2}\n{line3}\n{line4}"
    
    def generate_free_verse(self, lines: int = 6) -> str:
        """Generate a free verse poem."""
        poem_lines = []
        for _ in range(lines):
            if random.random() < 0.5:
                # Simple line
                line = f"{random.choice(ADJECTIVES)} {random.choice(NOUNS)} {random.choice(VERBS)}"
            else:
                # Complex line
                line = f"{random.choice(PREPOSITIONS)} the {random.choice(ADJECTIVES)} {random.choice(NOUNS)}, {random.choice(ADJECTIVES)} {random.choice(NOUNS)} {random.choice(VERBS)}"
            poem_lines.append(line.capitalize())
        return '\n'.join(poem_lines)
    
    def generate_sonnet(self) -> str:
        """Generate a 14-line sonnet (simplified)."""
        lines = []
        for i in range(14):
            if i % 2 == 0:
                line = f"The {random.choice(ADJECTIVES)} {random.choice(NOUNS)} that {random.choice(VERBS)} {random.choice(PREPOSITIONS)} the {random.choice(NOUNS)}"
            else:
                line = f"And {random.choice(ADJECTIVES)} {random.choice(NOUNS)} in {random.choice(ADJECTIVES)} {random.choice(NOUNS)}"
            lines.append(line.capitalize())
        return '\n'.join(lines)
    
    def generate_acrostic(self, word: str) -> str:
        """Generate an acrostic poem from a word."""
        lines = []
        for char in word.upper():
            line = f"{char}{random.choice(ADJECTIVES)[1:]} {random.choice(NOUNS)} {random.choice(VERBS)}"
            lines.append(line.capitalize())
        return '\n'.join(lines)


def main():
    """Main function to run the poem generator."""
    parser = argparse.ArgumentParser(
        description='Generate random poems in various styles',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '-s', '--style',
        choices=['haiku', 'limerick', 'quatrain', 'free', 'sonnet', 'acrostic'],
        default='haiku',
        help='Style of poem to generate (default: haiku)'
    )
    
    parser.add_argument(
        '-l', '--lines',
        type=int,
        default=6,
        help='Number of lines for free verse (default: 6)'
    )
    
    parser.add_argument(
        '-w', '--word',
        type=str,
        help='Word for acrostic poem'
    )
    
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help='Number of poems to generate (default: 1)'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        help='Random seed for reproducibility'
    )
    
    args = parser.parse_args()
    
    # Validate acrostic word
    if args.style == 'acrostic' and not args.word:
        print("Error: Acrostic style requires a word (-w/--word)", file=sys.stderr)
        sys.exit(1)
    
    generator = PoemGenerator(seed=args.seed)
    
    for i in range(args.number):
        if args.number > 1:
            print(f"\n--- Poem {i + 1} ---")
        
        if args.style == 'haiku':
            poem = generator.generate_haiku()
        elif args.style == 'limerick':
            poem = generator.generate_limerick()
        elif args.style == 'quatrain':
            poem = generator.generate_quatrain()
        elif args.style == 'free':
            poem = generator.generate_free_verse(args.lines)
        elif args.style == 'sonnet':
            poem = generator.generate_sonnet()
        elif args.style == 'acrostic':
            poem = generator.generate_acrostic(args.word)
        
        print(poem)
        print()  # Empty line after poem


if __name__ == '__main__':
    main()
