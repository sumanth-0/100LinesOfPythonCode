## Python Code: Random Emoji Canvas

import random
from PIL import Image, ImageDraw, ImageFont
import os

# --- 1. CONFIGURATION ---
WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOR = "white"
OUTPUT_FILE = "random_emoji_canvas.png"
EMOJI_SIZE = 50  # Font size for emojis
NUM_EMOJIS = 25  # Total number of emojis to place

# IMPORTANT: You MUST set a FONT_PATH that supports color emojis for your OS.
# If this path is wrong, you will see blank rectangles instead of emojis.

# --- Auto-Detect Font Path (Best Effort) ---
FONT_PATH = "arial.ttf" # Default fallback for systems where it exists

if os.name == 'nt':  # Windows
    # Common path for Segoe UI Emoji, which handles color emojis on Windows
    win_path = "C:/Windows/Fonts/seguiemj.ttf"
    if os.path.exists(win_path):
        FONT_PATH = win_path
elif os.uname()[0] == 'Darwin':  # macOS
    # Path for Apple Color Emoji font
    mac_path = "/System/Library/Fonts/Apple Color Emoji.ttc"
    if os.path.exists(mac_path):
        FONT_PATH = mac_path
# ------------------------------------------

# List of colorful emojis to choose from
EMOJI_LIST = ['✨', '🔥', '🚀', '💡', '🌟', '💖', '💯', '🐍', '🤖', '🎉', 
              '✅', '❌', '🥳', '😎', '🍕', '🐱', '🐶', '💻', '💡', '🌎']

try:
    emoji_font = ImageFont.truetype(FONT_PATH, EMOJI_SIZE)
    print(f"Using font: {FONT_PATH}")
except IOError:
    print(f"🚨 Warning: Could not load specific font at '{FONT_PATH}'. Using default font.")
    print("   If you see rectangles, please update FONT_PATH to your system's color emoji font.")
    emoji_font = ImageFont.load_default()

# --- 2. MAIN GENERATION FUNCTION ---
def generate_random_canvas():
    # 2.1 Create the canvas
    # Using 'RGB' mode for basic image color. For complex emojis, a mode like 'RGBA' or
    # proper font loading is key.
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)

    print(f"Generating image {OUTPUT_FILE} ({WIDTH}x{HEIGHT})...")
    
    # 2.2 Place emojis randomly
    for _ in range(NUM_EMOJIS):
        # 1. Select Content
        emoji = random.choice(EMOJI_LIST)
        
        # 2. Get Emoji Bounding Box (needed to prevent overflow)
        # Note: Bounding box calculation can be complex. This uses a simpler estimate.
        x_max_limit = WIDTH - EMOJI_SIZE 
        y_max_limit = HEIGHT - EMOJI_SIZE 
        
        # 3. Determine Random Position
        x = random.randint(0, x_max_limit)
        y = random.randint(0, y_max_limit)
        
        position = (x, y)
        
        # 4. Draw the emoji
        # Color is set to black, but the font file dictates the actual emoji color.
        draw.text(position, emoji, font=emoji_font, fill=(0, 0, 0))

    # 2.3 Save the image
    img.save(OUTPUT_FILE, "PNG")

    print(f"✅ Success! Image saved as {OUTPUT_FILE}.")


if __name__ == "__main__":
    generate_random_canvas()
