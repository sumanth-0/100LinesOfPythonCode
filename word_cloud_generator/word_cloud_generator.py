#!/usr/bin/env python3
"""
Word Cloud Generator
Generates a word cloud visualization from input text using wordcloud and matplotlib.
"""

import argparse
import sys
from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_word_cloud(text, output_path=None, width=800, height=400, 
                        background_color='white', colormap='viridis'):
    """
    Generate a word cloud from the given text.
    
    Args:
        text (str): Input text to generate word cloud from
        output_path (str): Path to save the word cloud image
        width (int): Width of the word cloud image
        height (int): Height of the word cloud image
        background_color (str): Background color for the word cloud
        colormap (str): Matplotlib colormap to use
    """
    if not text or not text.strip():
        print("Error: Input text is empty!")
        return
    
    # Generate word cloud
    wordcloud = WordCloud(
        width=width,
        height=height,
        background_color=background_color,
        colormap=colormap,
        relative_scaling=0.5,
        min_font_size=10
    ).generate(text)
    
    # Display the word cloud
    plt.figure(figsize=(width/100, height/100))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    
    # Save or show the word cloud
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Word cloud saved to: {output_path}")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(
        description='Generate a word cloud from text input'
    )
    parser.add_argument(
        'input',
        help='Input text file path or direct text string'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output image file path (e.g., wordcloud.png)',
        default=None
    )
    parser.add_argument(
        '-w', '--width',
        type=int,
        default=800,
        help='Width of the word cloud (default: 800)'
    )
    parser.add_argument(
        '-ht', '--height',
        type=int,
        default=400,
        help='Height of the word cloud (default: 400)'
    )
    parser.add_argument(
        '-bg', '--background',
        default='white',
        help='Background color (default: white)'
    )
    parser.add_argument(
        '-c', '--colormap',
        default='viridis',
        help='Matplotlib colormap (default: viridis)'
    )
    
    args = parser.parse_args()
    
    # Read text from file or use direct input
    input_path = Path(args.input)
    if input_path.exists() and input_path.is_file():
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = args.input
    
    # Generate word cloud
    generate_word_cloud(
        text=text,
        output_path=args.output,
        width=args.width,
        height=args.height,
        background_color=args.background,
        colormap=args.colormap
    )


if __name__ == '__main__':
    main()
