#!/usr/bin/env python3
"""
Random Username Generator

A comprehensive username generator that creates creative and unique usernames
with various customization options including themes, formats, and styles.

Features:
- Multiple username generation strategies
- Themed username generation (fantasy, sci-fi, nature, tech)
- Customizable length and format
- Special character options
- Number appending options
- Batch generation capability
"""

import random
import string
import argparse
from typing import List, Optional


class UsernameGenerator:
    """Generate random creative usernames with various options."""
    
    # Word lists for different themes
    ADJECTIVES = [
        'Swift', 'Brave', 'Mighty', 'Silent', 'Dark', 'Bright', 'Golden', 'Silver',
        'Mystic', 'Epic', 'Cosmic', 'Quantum', 'Digital', 'Cyber', 'Neon', 'Shadow',
        'Crystal', 'Thunder', 'Storm', 'Frost', 'Blaze', 'Phoenix', 'Dragon', 'Noble'
    ]
    
    NOUNS = [
        'Wolf', 'Tiger', 'Eagle', 'Falcon', 'Warrior', 'Knight', 'Hunter', 'Ninja',
        'Wizard', 'Mage', 'Ranger', 'Rider', 'Seeker', 'Guardian', 'Champion', 'Legend',
        'Master', 'Hero', 'Sage', 'Phantom', 'Spirit', 'Raider', 'Striker', 'Sentinel'
    ]
    
    FANTASY_WORDS = [
        'Aether', 'Elven', 'Rune', 'Arcane', 'Celestial', 'Ethereal', 'Mythic',
        'Enchanted', 'Fabled', 'Immortal', 'Divine', 'Ancient', 'Eternal'
    ]
    
    SCIFI_WORDS = [
        'Astro', 'Nebula', 'Stellar', 'Cosmic', 'Quantum', 'Cyber', 'Nova',
        'Plasma', 'Vector', 'Matrix', 'Binary', 'Circuit', 'Photon', 'Pulse'
    ]
    
    NATURE_WORDS = [
        'Ocean', 'Mountain', 'River', 'Forest', 'Meadow', 'Canyon', 'Summit',
        'Valley', 'Willow', 'Cedar', 'Maple', 'Storm', 'Rain', 'Wind'
    ]
    
    TECH_WORDS = [
        'Code', 'Pixel', 'Data', 'Logic', 'Cache', 'Byte', 'Hack', 'Script',
        'Crypto', 'Node', 'Packet', 'Protocol', 'Firewall', 'Server'
    ]

    def __init__(self):
        self.themes = {
            'fantasy': self.FANTASY_WORDS,
            'scifi': self.SCIFI_WORDS,
            'nature': self.NATURE_WORDS,
            'tech': self.TECH_WORDS
        }

    def generate_basic(self, length: int = 10) -> str:
        """Generate a basic random username with letters and numbers."""
        chars = string.ascii_lowercase + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def generate_compound(self, theme: Optional[str] = None) -> str:
        """Generate a compound username using adjective + noun pattern."""
        adj = random.choice(self.ADJECTIVES)
        noun = random.choice(self.NOUNS)
        
        if theme and theme in self.themes:
            # Mix in a themed word
            themed_word = random.choice(self.themes[theme])
            combinations = [
                f"{adj}{noun}",
                f"{themed_word}{noun}",
                f"{adj}{themed_word}"
            ]
            return random.choice(combinations)
        
        return f"{adj}{noun}"

    def generate_with_numbers(self, base: str, number_style: str = 'suffix') -> str:
        """Add numbers to a username in various styles."""
        num = random.randint(1, 9999)
        
        if number_style == 'suffix':
            return f"{base}{num}"
        elif number_style == 'prefix':
            return f"{num}{base}"
        elif number_style == 'mixed':
            mid = len(base) // 2
            return f"{base[:mid]}{num}{base[mid:]}"
        else:
            return f"{base}{num}"

    def generate_with_separators(self, parts: List[str], separator: str = '_') -> str:
        """Join username parts with separators."""
        valid_separators = ['_', '-', '.', '']
        sep = separator if separator in valid_separators else '_'
        return sep.join(parts)

    def generate_leetspeak(self, username: str) -> str:
        """Convert username to leetspeak style."""
        leet_map = {
            'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5',
            'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5',
            't': '7', 'T': '7', 'l': '1', 'L': '1'
        }
        return ''.join(leet_map.get(c, c) for c in username)

    def generate_username(self, 
                         style: str = 'compound',
                         theme: Optional[str] = None,
                         add_numbers: bool = False,
                         number_style: str = 'suffix',
                         separator: str = '',
                         leetspeak: bool = False,
                         length: int = 10) -> str:
        """Generate a username with specified options."""
        
        if style == 'basic':
            username = self.generate_basic(length)
        elif style == 'compound':
            username = self.generate_compound(theme)
        else:
            username = self.generate_compound(theme)
        
        # Apply separator if parts can be identified
        if separator and style == 'compound':
            adj = random.choice(self.ADJECTIVES)
            noun = random.choice(self.NOUNS)
            username = self.generate_with_separators([adj, noun], separator)
        
        # Add numbers if requested
        if add_numbers:
            username = self.generate_with_numbers(username, number_style)
        
        # Apply leetspeak if requested
        if leetspeak:
            username = self.generate_leetspeak(username)
        
        return username

    def generate_batch(self, count: int, **kwargs) -> List[str]:
        """Generate multiple usernames."""
        return [self.generate_username(**kwargs) for _ in range(count)]


def main():
    """Main function to run the username generator from command line."""
    parser = argparse.ArgumentParser(
        description='Generate random creative usernames with various options'
    )
    parser.add_argument('-n', '--count', type=int, default=1,
                       help='Number of usernames to generate (default: 1)')
    parser.add_argument('-s', '--style', choices=['basic', 'compound'],
                       default='compound', help='Username style (default: compound)')
    parser.add_argument('-t', '--theme', choices=['fantasy', 'scifi', 'nature', 'tech'],
                       help='Theme for username generation')
    parser.add_argument('--numbers', action='store_true',
                       help='Add numbers to usernames')
    parser.add_argument('--number-style', choices=['prefix', 'suffix', 'mixed'],
                       default='suffix', help='Number placement style')
    parser.add_argument('--separator', choices=['_', '-', '.', ''],
                       default='', help='Separator between username parts')
    parser.add_argument('--leetspeak', action='store_true',
                       help='Convert usernames to leetspeak')
    parser.add_argument('-l', '--length', type=int, default=10,
                       help='Length for basic style usernames (default: 10)')
    
    args = parser.parse_args()
    
    generator = UsernameGenerator()
    
    print("\n🎲 Random Username Generator\n")
    print("="*50)
    
    usernames = generator.generate_batch(
        count=args.count,
        style=args.style,
        theme=args.theme,
        add_numbers=args.numbers,
        number_style=args.number_style,
        separator=args.separator,
        leetspeak=args.leetspeak,
        length=args.length
    )
    
    for i, username in enumerate(usernames, 1):
        print(f"{i:3d}. {username}")
    
    print("="*50)
    print(f"\nGenerated {len(usernames)} username(s)\n")


if __name__ == '__main__':
    main()
