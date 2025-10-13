#!/usr/bin/env python3
"""
Comic Strip Quote Generator
Overlays random quotes on cartoon-style images using PIL.
"""

import os
import random
from pathlib import Path
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Please install Pillow: pip install Pillow")
    exit(1)

# Sample quotes for comic strips
QUOTES = [
    "With great power comes great responsibility!",
    "I'm not saying it was aliens... but it was aliens!",
    "This looks like a job for... me!",
    "Did someone say coffee?",
    "Today's forecast: 99% chance of awesome!",
    "Error 404: Motivation not found",
    "Keep calm and code on!",
    "Debugging is like being a detective in a crime movie where you're also the murderer",
    "There's no place like 127.0.0.1",
    "I speak fluent sarcasm and Python"
]

def create_sample_image(width=800, height=600):
    """Create a sample cartoon-style background."""
    colors = [(255, 220, 180), (180, 220, 255), (255, 200, 200), (200, 255, 200)]
    img = Image.new('RGB', (width, height), random.choice(colors))
    draw = ImageDraw.Draw(img)
    
    # Add some cartoon-style elements
    for _ in range(10):
        x, y = random.randint(0, width), random.randint(0, height)
        r = random.randint(20, 80)
        color = tuple(random.randint(100, 255) for _ in range(3))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=color, outline=(0, 0, 0), width=3)
    
    return img

def add_quote_to_image(image, quote, font_size=40):
    """Add a quote to the image with comic-style formatting."""
    draw = ImageDraw.Draw(image)
    width, height = image.size
    
    # Try to load a bold font, fallback to default
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    # Word wrap the quote
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] < width - 100:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    lines.append(' '.join(current_line))
    
    # Calculate text position (centered)
    line_height = font_size + 10
    total_height = len(lines) * line_height
    y = (height - total_height) // 2
    
    # Draw text with outline for comic effect
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        x = (width - (bbox[2] - bbox[0])) // 2
        
        # Draw outline
        for offset in [(-2,-2), (-2,2), (2,-2), (2,2)]:
            draw.text((x+offset[0], y+offset[1]), line, font=font, fill=(0, 0, 0))
        
        # Draw main text
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += line_height
    
    return image

def main():
    """Generate a comic strip with a random quote."""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Create or load image
    img = create_sample_image()
    
    # Add random quote
    quote = random.choice(QUOTES)
    img = add_quote_to_image(img, quote)
    
    # Save the result
    output_path = output_dir / f"comic_quote_{random.randint(1000, 9999)}.png"
    img.save(output_path)
    print(f"Comic created: {output_path}")
    print(f"Quote: {quote}")

if __name__ == "__main__":
    main()
