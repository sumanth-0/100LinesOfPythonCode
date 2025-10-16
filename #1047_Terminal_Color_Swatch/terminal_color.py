#!/usr/bin/env python3
import argparse
import os
import random
import sys


def generate_color():
    """Return a tuple (r, g, b) with random 0-255 values."""
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def rgb_to_hex(rgb):
    """Convert an (r, g, b) tuple to a hex string like '#1a2b3c'."""
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def supports_truecolor():
    """
    Heuristic for truecolor (24-bit) support.

    Many modern terminals set COLORTERM=truecolor or have "24bit" in TERM.
    This is not perfect but works well in practice.
    """
    colorterm = os.environ.get("COLORTERM", "").lower()
    term = os.environ.get("TERM", "").lower()
    return "truecolor" in colorterm or "24bit" in term


def print_color_block(rgb, label, block_width=12):
    """
    Print a colored block followed by its hex label.

    Uses ANSI 24-bit background escape sequences:
      \x1b[48;2;R;G;Bm  -> set background RGB
      \x1b[38;2;R;G;Bm  -> optionally set foreground RGB
      \x1b[0m           -> reset
    """
    r, g, b = rgb
    # Background fill (use spaces to make a block)
    bg = f"\x1b[48;2;{r};{g};{b}m" + " " * block_width + "\x1b[0m"
    # Choose a readable foreground: black or white depending on brightness
    brightness = (r * 299 + g * 587 + b * 114) / 1000
    fg_rgb = (0, 0, 0) if brightness > 128 else (255, 255, 255)
    fg = f"\x1b[38;2;{fg_rgb[0]};{fg_rgb[1]};{fg_rgb[2]}m"
    print(f"{bg}  {fg}{label}\x1b[0m")


def display_palette(count):
    """Generate and display `count` random colors."""
    if not supports_truecolor():
        print(
            "Warning: your terminal may not support truecolor (24-bit). "
            "Colors might look off."
        )
    for _ in range(count):
        rgb = generate_color()
        hex_code = rgb_to_hex(rgb)
        print_color_block(rgb, hex_code)


def parse_args(argv):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Display a palette of random colors with hex codes."
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=8,
        help="number of colors to show (default: 8)",
    )
    return parser.parse_args(argv)


def main(argv=None):
    """Entry point."""
    args = parse_args(argv or sys.argv[1:])
    count = max(1, min(64, args.count))  # keep count reasonable
    display_palette(count)


if __name__ == "__main__":
    main()