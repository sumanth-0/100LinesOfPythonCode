#!/usr/bin/env python3
"""
Random Font Style Text Generator
Converts normal text into random styled Unicode text (bold, italic, cursive, etc.)

This script provides various Unicode text transformations including:
- Bold (Mathematical Bold)
- Italic (Mathematical Italic)
- Bold Italic
- Script/Cursive
- Monospace
- Sans-serif
- Double-struck
- Fraktur/Gothic
- Circled
- Squared
- Inverted/Flipped
- Reversed
- Strikethrough
- Underline
- Bubble text
- Small caps
"""

import random
import sys


class FontStyleConverter:
    """Class to convert text into various Unicode font styles"""
    
    def __init__(self):
        # Unicode character mappings for different styles
        self.styles = {
            'bold': self._create_mapping(0x1D400, 0x1D419, 0x1D41A, 0x1D433),
            'italic': self._create_mapping(0x1D434, 0x1D44D, 0x1D44E, 0x1D467),
            'bold_italic': self._create_mapping(0x1D468, 0x1D481, 0x1D482, 0x1D49B),
            'script': self._create_mapping(0x1D49C, 0x1D4B5, 0x1D4B6, 0x1D4CF, 
                                          exceptions={0x1D49C: 'B', 0x1D49E: 'E', 0x1D49F: 'F',
                                                     0x1D4A2: 'H', 0x1D4A5: 'L', 0x1D4A6: 'M'}),
            'monospace': self._create_mapping(0x1D670, 0x1D689, 0x1D68A, 0x1D6A3),
            'double_struck': self._create_mapping(0x1D538, 0x1D551, 0x1D552, 0x1D56B),
            'sans_serif': self._create_mapping(0x1D5A0, 0x1D5B9, 0x1D5BA, 0x1D5D3),
            'sans_serif_bold': self._create_mapping(0x1D5D4, 0x1D5ED, 0x1D5EE, 0x1D607),
        }
    
    def _create_mapping(self, upper_start, upper_end, lower_start, lower_end, exceptions=None):
        """Create character mapping for a specific style"""
        mapping = {}
        
        # Map uppercase letters A-Z
        for i in range(26):
            char = chr(ord('A') + i)
            unicode_char = chr(upper_start + i)
            if exceptions and (upper_start + i) in exceptions:
                continue
            mapping[char] = unicode_char
        
        # Map lowercase letters a-z
        for i in range(26):
            char = chr(ord('a') + i)
            unicode_char = chr(lower_start + i)
            if exceptions and (lower_start + i) in exceptions:
                continue
            mapping[char] = unicode_char
        
        return mapping
    
    def convert_text(self, text, style):
        """Convert text to specified style"""
        if style not in self.styles:
            return text
        
        mapping = self.styles[style]
        result = []
        
        for char in text:
            result.append(mapping.get(char, char))
        
        return ''.join(result)
    
    def circled_text(self, text):
        """Convert text to circled characters"""
        circled_map = {}
        # Circled uppercase A-Z (U+24B6 to U+24CF)
        for i in range(26):
            circled_map[chr(ord('A') + i)] = chr(0x24B6 + i)
        # Circled lowercase uses same as uppercase
        for i in range(26):
            circled_map[chr(ord('a') + i)] = chr(0x24B6 + i)
        # Circled numbers 0-9
        for i in range(10):
            circled_map[str(i)] = chr(0x2460 + i - 1) if i > 0 else '⓪'
        
        return ''.join(circled_map.get(char, char) for char in text)
    
    def squared_text(self, text):
        """Convert text to squared characters"""
        squared_map = {}
        # Squared uppercase A-Z (U+1F130 to U+1F149)
        for i in range(26):
            squared_map[chr(ord('A') + i)] = chr(0x1F130 + i)
            squared_map[chr(ord('a') + i)] = chr(0x1F130 + i)
        
        return ''.join(squared_map.get(char, char) for char in text)
    
    def inverted_text(self, text):
        """Flip text upside down"""
        flip_map = {
            'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ',
            'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l',
            'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ',
            's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ', 'w': 'ʍ', 'x': 'x',
            'y': 'ʎ', 'z': 'z',
            'A': '∀', 'B': 'q', 'C': 'Ɔ', 'D': 'p', 'E': 'Ǝ', 'F': 'Ⅎ',
            'G': '⅁', 'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '˥',
            'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ', 'Q': 'Ò', 'R': 'ɹ',
            'S': 'S', 'T': '⊥', 'U': '∩', 'V': 'Λ', 'W': 'M', 'X': 'X',
            'Y': '⅄', 'Z': 'Z',
            '!': '¡', '?': '¿', '.': '˙', ',': '\'', '\'': ',',
            '1': 'Ɩ', '2': 'ᄅ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ',
            '6': '9', '7': 'ㄥ', '8': '8', '9': '6', '0': '0'
        }
        return ''.join(flip_map.get(char, char) for char in text[::-1])
    
    def bubble_text(self, text):
        """Convert text to bubble/circled style"""
        bubble_map = {}
        # Negative circled uppercase
        for i in range(26):
            bubble_map[chr(ord('A') + i)] = chr(0x1F150 + i)
            bubble_map[chr(ord('a') + i)] = chr(0x1F150 + i)
        
        return ''.join(bubble_map.get(char, char) for char in text)
    
    def small_caps(self, text):
        """Convert text to small caps"""
        small_caps_map = {
            'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ',
            'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ',
            'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ',
            's': 'ꜱ', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
            'y': 'ʏ', 'z': 'ᴢ'
        }
        return ''.join(small_caps_map.get(char.lower(), char) for char in text)
    
    def get_all_styles(self):
        """Return list of all available styles"""
        return ['bold', 'italic', 'bold_italic', 'script', 'monospace',
                'double_struck', 'sans_serif', 'sans_serif_bold', 'circled',
                'squared', 'inverted', 'bubble', 'small_caps']
    
    def apply_style(self, text, style):
        """Apply specified style to text"""
        if style in self.styles:
            return self.convert_text(text, style)
        elif style == 'circled':
            return self.circled_text(text)
        elif style == 'squared':
            return self.squared_text(text)
        elif style == 'inverted':
            return self.inverted_text(text)
        elif style == 'bubble':
            return self.bubble_text(text)
        elif style == 'small_caps':
            return self.small_caps(text)
        else:
            return text


def main():
    """Main function to run the font style converter"""
    converter = FontStyleConverter()
    
    print("=" * 60)
    print("Random Font Style Text Generator")
    print("=" * 60)
    
    # Get input text
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("\nEnter text to convert: ")
    
    if not text:
        print("No text provided!")
        return
    
    print(f"\nOriginal text: {text}\n")
    print("-" * 60)
    
    # Display all available styles
    styles = converter.get_all_styles()
    
    # Option to show all styles or random style
    choice = input("\nShow [A]ll styles or [R]andom style? (A/R): ").strip().upper()
    
    if choice == 'R' or choice == '':
        # Select random style
        random_style = random.choice(styles)
        result = converter.apply_style(text, random_style)
        print(f"\n{random_style.upper().replace('_', ' ')}:")
        print(f"{result}\n")
    else:
        # Show all styles
        print("\nAll available styles:\n")
        for style in styles:
            result = converter.apply_style(text, style)
            print(f"{style.upper().replace('_', ' ')}:")
            print(f"  {result}\n")
    
    print("=" * 60)


if __name__ == "__main__":
    main()
