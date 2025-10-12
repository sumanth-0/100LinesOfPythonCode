#!/usr/bin/env python3
"""
Text-to-Handwriting Generator
Converts input text to handwriting-style image using PIL and handwriting fonts.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import textwrap


def create_handwriting_image(
    text,
    output_path="handwriting.png",
    font_size=40,
    line_spacing=20,
    margin=50,
    page_width=800,
    bg_color=(255, 255, 255),
    text_color=(0, 0, 51),
):
    """
    Create a handwriting-style image from text.

    Args:
        text: Input text to convert
        output_path: Path to save the output image
        font_size: Size of the font
        line_spacing: Spacing between lines
        margin: Margin around the text
        page_width: Width of the output image
        bg_color: Background color (RGB tuple)
        text_color: Text color (RGB tuple)
    """
    # Try to use a handwriting-style font, fallback to default
    try:
        # Try common handwriting font names
        font_names = ["Segoe Script", "Bradley Hand", "Comic Sans MS", "Arial"]
        font = None
        for font_name in font_names:
            try:
                font = ImageFont.truetype(font_name, font_size)
                break
            except:
                continue
        if font is None:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()

    # Wrap text to fit page width
    max_chars = (page_width - 2 * margin) // (font_size // 2)
    wrapped_lines = []
    for paragraph in text.split("\n"):
        if paragraph.strip():
            wrapped_lines.extend(textwrap.wrap(paragraph, width=max_chars))
        else:
            wrapped_lines.append("")

    # Calculate image height
    line_height = font_size + line_spacing
    page_height = margin * 2 + len(wrapped_lines) * line_height

    # Create image
    img = Image.new("RGB", (page_width, page_height), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw text
    y = margin
    for line in wrapped_lines:
        draw.text((margin, y), line, fill=text_color, font=font)
        y += line_height

    # Save image
    img.save(output_path)
    print(f"Handwriting image saved to: {output_path}")


def main():
    """Main function to run the text-to-handwriting generator."""
    print("Text-to-Handwriting Generator")
    print("=" * 40)

    # Get input from user
    print("\nEnter your text (press Ctrl+D or Ctrl+Z when done):")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    text = "\n".join(lines)

    if not text.strip():
        print("No text provided. Exiting.")
        return

    # Get output filename
    output_path = input("\nEnter output filename (default: handwriting.png): ").strip()
    if not output_path:
        output_path = "handwriting.png"

    # Create handwriting image
    create_handwriting_image(text, output_path)


if __name__ == "__main__":
    main()
