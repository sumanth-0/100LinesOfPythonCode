#!/usr/bin/env python3
"""
Keyword Highlighter - Highlights specific keywords in text with colors
A simple tool to search and highlight keywords in text files or strings.
"""

import sys
import re
from typing import List, Tuple


class KeywordHighlighter:
    """A class to highlight keywords in text with ANSI color codes."""
    
    # ANSI color codes for terminal highlighting
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'reset': '\033[0m',
        'bold': '\033[1m',
    }
    
    def __init__(self, case_sensitive: bool = False):
        """Initialize the highlighter.
        
        Args:
            case_sensitive: Whether keyword matching should be case-sensitive
        """
        self.case_sensitive = case_sensitive
        self.keywords = {}
    
    def add_keyword(self, keyword: str, color: str = 'yellow'):
        """Add a keyword to highlight with a specific color.
        
        Args:
            keyword: The keyword to highlight
            color: The color to use for highlighting
        """
        if color not in self.COLORS:
            color = 'yellow'
        self.keywords[keyword] = color
    
    def highlight_text(self, text: str) -> str:
        """Highlight all keywords in the given text.
        
        Args:
            text: The text to process
            
        Returns:
            Text with ANSI color codes for highlighting
        """
        highlighted_text = text
        
        for keyword, color in self.keywords.items():
            flags = 0 if self.case_sensitive else re.IGNORECASE
            color_code = self.COLORS[color] + self.COLORS['bold']
            reset_code = self.COLORS['reset']
            
            pattern = re.escape(keyword)
            replacement = f"{color_code}{keyword}{reset_code}"
            highlighted_text = re.sub(pattern, replacement, highlighted_text, flags=flags)
        
        return highlighted_text
    
    def process_file(self, filename: str) -> str:
        """Read and highlight keywords in a file.
        
        Args:
            filename: Path to the file to process
            
        Returns:
            Highlighted file content
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.highlight_text(content)
        except FileNotFoundError:
            return f"Error: File '{filename}' not found."
        except Exception as e:
            return f"Error reading file: {str(e)}"


def main():
    """Main function demonstrating the keyword highlighter."""
    print("=" * 50)
    print("Keyword Highlighter Demo")
    print("=" * 50)
    
    # Create highlighter instance
    highlighter = KeywordHighlighter(case_sensitive=False)
    
    # Add keywords with different colors
    highlighter.add_keyword('python', 'green')
    highlighter.add_keyword('code', 'blue')
    highlighter.add_keyword('highlight', 'yellow')
    highlighter.add_keyword('keyword', 'cyan')
    
    # Sample text to highlight
    sample_text = """Python is a powerful programming language.
This Python code demonstrates how to highlight keywords in text.
The keyword highlighter can highlight multiple keywords with different colors.
You can use it to emphasize important code sections or documentation."""
    
    print("\nOriginal Text:")
    print("-" * 50)
    print(sample_text)
    
    print("\n\nHighlighted Text:")
    print("-" * 50)
    highlighted = highlighter.highlight_text(sample_text)
    print(highlighted)
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
