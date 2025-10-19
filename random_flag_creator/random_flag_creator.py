#!/usr/bin/env python3
"""
Random Flag Creator
Generates random flags with ASCII/colors or PNG images via PIL.

Features:
- ASCII flag generation with ANSI colors
- PNG flag generation using PIL
- Multiple flag patterns (horizontal stripes, vertical stripes, cross, diagonal)
- Random color generation
- Customizable flag dimensions
"""

import random
import sys
from typing import List, Tuple

try:
    from PIL import Image, ImageDraw
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("Warning: PIL not available. PNG generation will be disabled.")
    print("Install with: pip install Pillow")

# ANSI color codes for terminal output
COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'MAGENTA': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'BLACK': '\033[90m',
    'RESET': '\033[0m'
}

# RGB values for PIL
RGB_COLORS = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (0, 0, 255),      # Blue
    (255, 255, 0),    # Yellow
    (255, 0, 255),    # Magenta
    (0, 255, 255),    # Cyan
    (255, 255, 255),  # White
    (0, 0, 0),        # Black
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
]

FLAG_PATTERNS = ['horizontal', 'vertical', 'cross', 'diagonal', 'checker']


def random_color_rgb() -> Tuple[int, int, int]:
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def random_ansi_color() -> str:
    """Get a random ANSI color code."""
    return random.choice(list(COLORS.values())[:-1])  # Exclude RESET


def generate_ascii_horizontal_flag(width: int = 40, height: int = 15, stripes: int = 3) -> str:
    """Generate a horizontal striped flag in ASCII with colors."""
    result = []
    stripe_colors = [random_ansi_color() for _ in range(stripes)]
    stripe_height = height // stripes
    
    for i in range(height):
        stripe_idx = min(i // stripe_height, stripes - 1)
        color = stripe_colors[stripe_idx]
        line = color + '█' * width + COLORS['RESET']
        result.append(line)
    
    return '\n'.join(result)


def generate_ascii_vertical_flag(width: int = 40, height: int = 15, stripes: int = 3) -> str:
    """Generate a vertical striped flag in ASCII with colors."""
    result = []
    stripe_colors = [random_ansi_color() for _ in range(stripes)]
    stripe_width = width // stripes
    
    for i in range(height):
        line = ""
        for j in range(stripes):
            color = stripe_colors[j]
            line += color + '█' * stripe_width + COLORS['RESET']
        result.append(line)
    
    return '\n'.join(result)


def generate_ascii_cross_flag(width: int = 40, height: int = 15) -> str:
    """Generate a cross pattern flag in ASCII with colors."""
    bg_color = random_ansi_color()
    cross_color = random_ansi_color()
    result = []
    
    mid_h = height // 2
    mid_w = width // 2
    
    for i in range(height):
        line = ""
        for j in range(width):
            if i == mid_h or j == mid_w:
                line += cross_color + '█' + COLORS['RESET']
            else:
                line += bg_color + '█' + COLORS['RESET']
        result.append(line)
    
    return '\n'.join(result)


def generate_png_horizontal_flag(width: int = 300, height: int = 200, stripes: int = 3, filename: str = 'flag_horizontal.png'):
    """Generate a horizontal striped flag as PNG."""
    if not PIL_AVAILABLE:
        print("Error: PIL is not available for PNG generation.")
        return
    
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    stripe_colors = [random.choice(RGB_COLORS) for _ in range(stripes)]
    stripe_height = height // stripes
    
    for i in range(stripes):
        y_start = i * stripe_height
        y_end = (i + 1) * stripe_height if i < stripes - 1 else height
        draw.rectangle([(0, y_start), (width, y_end)], fill=stripe_colors[i])
    
    img.save(filename)
    print(f"Flag saved as {filename}")


def generate_png_vertical_flag(width: int = 300, height: int = 200, stripes: int = 3, filename: str = 'flag_vertical.png'):
    """Generate a vertical striped flag as PNG."""
    if not PIL_AVAILABLE:
        print("Error: PIL is not available for PNG generation.")
        return
    
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    stripe_colors = [random.choice(RGB_COLORS) for _ in range(stripes)]
    stripe_width = width // stripes
    
    for i in range(stripes):
        x_start = i * stripe_width
        x_end = (i + 1) * stripe_width if i < stripes - 1 else width
        draw.rectangle([(x_start, 0), (x_end, height)], fill=stripe_colors[i])
    
    img.save(filename)
    print(f"Flag saved as {filename}")


def generate_png_cross_flag(width: int = 300, height: int = 200, filename: str = 'flag_cross.png'):
    """Generate a cross pattern flag as PNG."""
    if not PIL_AVAILABLE:
        print("Error: PIL is not available for PNG generation.")
        return
    
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    
    bg_color = random.choice(RGB_COLORS)
    cross_color = random.choice(RGB_COLORS)
    
    # Draw background
    draw.rectangle([(0, 0), (width, height)], fill=bg_color)
    
    # Draw cross
    cross_width = width // 6
    cross_height = height // 6
    
    # Vertical bar
    draw.rectangle([(width // 2 - cross_width // 2, 0), 
                   (width // 2 + cross_width // 2, height)], fill=cross_color)
    
    # Horizontal bar
    draw.rectangle([(0, height // 2 - cross_height // 2), 
                   (width, height // 2 + cross_height // 2)], fill=cross_color)
    
    img.save(filename)
    print(f"Flag saved as {filename}")


def main():
    """
    Main function to generate random flags.
    """
    print("=" * 50)
    print("Random Flag Creator")
    print("=" * 50)
    print()
    
    # Generate ASCII flags
    print("1. Horizontal Striped Flag (ASCII):")
    print(generate_ascii_horizontal_flag(width=40, height=10, stripes=3))
    print()
    
    print("2. Vertical Striped Flag (ASCII):")
    print(generate_ascii_vertical_flag(width=40, height=10, stripes=4))
    print()
    
    print("3. Cross Pattern Flag (ASCII):")
    print(generate_ascii_cross_flag(width=40, height=10))
    print()
    
    # Generate PNG flags if PIL is available
    if PIL_AVAILABLE:
        print("Generating PNG flags...")
        generate_png_horizontal_flag(width=300, height=200, stripes=3, filename='flag_horizontal.png')
        generate_png_vertical_flag(width=300, height=200, stripes=3, filename='flag_vertical.png')
        generate_png_cross_flag(width=300, height=200, filename='flag_cross.png')
        print("\nPNG flags generated successfully!")
    else:
        print("Skipping PNG generation (PIL not available)")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
