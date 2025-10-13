#!/usr/bin/env python3
"""
Random Flag Creator
Generates random flag patterns using PIL (Pillow)
"""

import random
from PIL import Image, ImageDraw
import os

def random_color():
    """Generate a random RGB color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def create_horizontal_stripes(width, height, num_stripes):
    """Create a flag with horizontal stripes."""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    stripe_height = height // num_stripes
    
    for i in range(num_stripes):
        color = random_color()
        y1 = i * stripe_height
        y2 = (i + 1) * stripe_height if i < num_stripes - 1 else height
        draw.rectangle([0, y1, width, y2], fill=color)
    
    return img

def create_vertical_stripes(width, height, num_stripes):
    """Create a flag with vertical stripes."""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    stripe_width = width // num_stripes
    
    for i in range(num_stripes):
        color = random_color()
        x1 = i * stripe_width
        x2 = (i + 1) * stripe_width if i < num_stripes - 1 else width
        draw.rectangle([x1, 0, x2, height], fill=color)
    
    return img

def create_quadrant_flag(width, height):
    """Create a flag with four colored quadrants."""
    img = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(img)
    mid_w, mid_h = width // 2, height // 2
    
    draw.rectangle([0, 0, mid_w, mid_h], fill=random_color())
    draw.rectangle([mid_w, 0, width, mid_h], fill=random_color())
    draw.rectangle([0, mid_h, mid_w, height], fill=random_color())
    draw.rectangle([mid_w, mid_h, width, height], fill=random_color())
    
    return img

def create_border_flag(width, height, border_size):
    """Create a flag with a colored border and center."""
    img = Image.new('RGB', (width, height), random_color())
    draw = ImageDraw.Draw(img)
    draw.rectangle([border_size, border_size, width - border_size, height - border_size], 
                   fill=random_color())
    return img

def create_random_flag(width=600, height=400, filename="random_flag.png"):
    """Generate a random flag and save it."""
    flag_types = [
        lambda: create_horizontal_stripes(width, height, random.randint(2, 5)),
        lambda: create_vertical_stripes(width, height, random.randint(2, 5)),
        lambda: create_quadrant_flag(width, height),
        lambda: create_border_flag(width, height, random.randint(20, 60))
    ]
    
    flag = random.choice(flag_types)()
    flag.save(filename)
    print(f"Flag saved as '{filename}'")
    return filename

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate random flag patterns")
    parser.add_argument("-w", "--width", type=int, default=600, help="Flag width (default: 600)")
    parser.add_argument("-H", "--height", type=int, default=400, help="Flag height (default: 400)")
    parser.add_argument("-o", "--output", default="random_flag.png", help="Output filename")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of flags to generate")
    
    args = parser.parse_args()
    
    for i in range(args.number):
        if args.number > 1:
            filename = f"{os.path.splitext(args.output)[0]}_{i+1}.png"
        else:
            filename = args.output
        create_random_flag(args.width, args.height, filename)
