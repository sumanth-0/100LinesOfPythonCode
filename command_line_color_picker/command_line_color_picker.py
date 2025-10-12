#!/usr/bin/env python3
"""Command Line Color Picker - Converts colors between formats and displays them."""

import sys
import re

# Common color names mapped to hex values
COLOR_NAMES = {
    'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF', 'white': '#FFFFFF',
    'black': '#000000', 'yellow': '#FFFF00', 'cyan': '#00FFFF', 'magenta': '#FF00FF',
    'orange': '#FFA500', 'purple': '#800080', 'pink': '#FFC0CB', 'gray': '#808080',
    'brown': '#A52A2A', 'lime': '#00FF00', 'navy': '#000080', 'teal': '#008080'
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    """Convert RGB to hex color."""
    return f'#{r:02X}{g:02X}{b:02X}'

def parse_color(color_input):
    """Parse color input and return RGB tuple."""
    color_input = color_input.strip().lower()
    
    # Check if it's a color name
    if color_input in COLOR_NAMES:
        return hex_to_rgb(COLOR_NAMES[color_input])
    
    # Check if it's hex format
    hex_match = re.match(r'^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$', color_input)
    if hex_match:
        return hex_to_rgb(color_input)
    
    # Check if it's RGB format like "rgb(255, 0, 0)" or "255,0,0" or "255 0 0"
    rgb_match = re.match(r'^rgb?\(?\s*(\d+)[\s,]+?(\d+)[\s,]+?(\d+)\s*\)?$', color_input)
    if rgb_match:
        r, g, b = map(int, rgb_match.groups())
        if all(0 <= v <= 255 for v in (r, g, b)):
            return (r, g, b)
    
    return None

def display_color(r, g, b):
    """Display color block in terminal using ANSI escape codes."""
    # ANSI escape code for RGB background color
    color_block = f'\033[48;2;{r};{g};{b}m' + '  ' * 10 + '\033[0m'
    print(f"\n{color_block}\n")

def display_color_info(r, g, b):
    """Display all color format information."""
    hex_color = rgb_to_hex(r, g, b)
    
    # Display color block
    display_color(r, g, b)
    
    # Display formats
    print("Color Formats:")
    print(f"  HEX: {hex_color}")
    print(f"  RGB: rgb({r}, {g}, {b})")
    print(f"  R: {r}, G: {g}, B: {b}")
    
    # Check if it matches a known color name
    for name, hex_val in COLOR_NAMES.items():
        if hex_val.upper() == hex_color.upper():
            print(f"  Name: {name.capitalize()}")
            break

def main():
    """Main function to run the color picker."""
    if len(sys.argv) < 2:
        print("Usage: python command_line_color_picker.py <color>")
        print("\nExamples:")
        print("  python command_line_color_picker.py red")
        print("  python command_line_color_picker.py '#FF0000'")
        print("  python command_line_color_picker.py 'rgb(255, 0, 0)'")
        print("  python command_line_color_picker.py '255,0,0'")
        sys.exit(1)
    
    color_input = ' '.join(sys.argv[1:])
    rgb = parse_color(color_input)
    
    if rgb is None:
        print(f"Error: Invalid color format '{color_input}'")
        sys.exit(1)
    
    display_color_info(*rgb)

if __name__ == '__main__':
    main()
