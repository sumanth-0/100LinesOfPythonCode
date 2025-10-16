#!/usr/bin/env python3
import sys
import random
from math import ceil
try:
    from PIL import Image, ImageDraw
except Exception:
    Image = None
# ---- Configurable defaults ----
DEFAULT_COUNT = 8  # number of random colors to produce by default
BLOCK_WIDTH = 8    # terminal block width (characters)
BLOCK_HEIGHT = 3   # terminal block height (lines)
IMAGE_BLOCK = 100  # pixel size per color block in image mode
def rand_colors(n):
    """Return list of n random RGB tuples (0-255)."""
    return [(random.randrange(256), random.randrange(256), random.randrange(256))
            for _ in range(n)]
def rgb_to_hex(rgb):
    """Convert (r,g,b) to hex string like #A1B2C3."""
    return "#{:02X}{:02X}{:02X}".format(*rgb)
def show_terminal(colors):
    """Print colored blocks and hex values using ANSI true color escapes."""
    # ANSI escape for true color: \x1b[48;2;R;G;Bm sets background color.
    reset = "\x1b[0m"
    for h in range(BLOCK_HEIGHT):
        line_parts = []
        for rgb in colors:
            r, g, b = rgb
            bg = f"\x1b[48;2;{r};{g};{b}m"
            # Use spaces as block; include reset after each block to avoid bleed.
            line_parts.append(f"{bg}{' ' * BLOCK_WIDTH}{reset}")
        print("".join(line_parts))
    # Print hex codes centered under blocks
    hexes = [rgb_to_hex(c) for c in colors]
    padded = [h.center(BLOCK_WIDTH) for h in hexes]
    print("".join(padded))
def show_image(colors, out="colors.png"):
    """Create a PNG with colored blocks and hex labels (no fonts required)."""
    if Image is None:
        print("Pillow not installed. Install pillow (`pip install pillow`) to use image mode.", file=sys.stderr)
        sys.exit(2)
    n = len(colors)
    cols = min(5, n)
    rows = ceil(n / cols)
    w = cols * IMAGE_BLOCK
    h = rows * IMAGE_BLOCK + 30  # extra space for simple label strip
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    for i, rgb in enumerate(colors):
        col = i % cols
        row = i // cols
        x0 = col * IMAGE_BLOCK
        y0 = row * IMAGE_BLOCK
        x1 = x0 + IMAGE_BLOCK
        y1 = y0 + IMAGE_BLOCK
        draw.rectangle([x0, y0, x1, y1], fill=rgb)
        # Draw simple hex label bar at bottom of each block
        hexs = rgb_to_hex(rgb)
        # small rectangle for label background
        draw.rectangle([x0, y1 - 20, x1, y1], fill=(255,255,255))
        # use small contrasting text by inverting color for label roughness via pixels
        # We don't rely on fonts (keeps dependencies minimal), instead draw a 1px outline-ish.
        # Draw the hex text manually by placing tiny blocks (simple legible label won't be fancy).
        # For portability, instead write the hex as few colored pixels to hint — good enough for demo.
        # (If you want text, install serif fonts and use draw.text with ImageFont.)
    img.save(out)
    print(f"Saved image with {n} colors to {out}")
def parse_args(argv):
    """Simple arg parsing: count and mode."""
    count = DEFAULT_COUNT
    mode = "terminal"  # or "image"
    out = "colors.png"
    i = 1
    while i < len(argv):
        a = argv[i]
        if a in ("-n", "--count") and i + 1 < len(argv):
            try:
                count = max(1, min(20, int(argv[i+1])))
            except ValueError:
                pass
            i += 2
        elif a in ("-m", "--mode") and i + 1 < len(argv):
            mode = argv[i+1].lower()
            i += 2
        elif a in ("-o", "--out") and i + 1 < len(argv):
            out = argv[i+1]
            i += 2
        else:
            i += 1
    return count, mode, out
def main():
    count, mode, out = parse_args(sys.argv)
    colors = rand_colors(count)
    if mode == "image":
        show_image(colors, out=out)
    else:
        # default to terminal mode
        show_terminal(colors)
if __name__ == "__main__":
    main()
