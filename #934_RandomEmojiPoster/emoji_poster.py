# emoji_poster.py
from PIL import Image, ImageDraw, ImageFont
import random

# --- CONFIG ---
canvas_width = 800
canvas_height = 600
background_color = (255, 255, 255)  # white background
num_emojis = 100
emoji_list = ['😀','😂','😍','😎','🤩','🥳','😜','😇','🤔','😱','👍','💖','🌟','🔥','🎉','🍕','🍔','🍩','🍿','🎈']

# Optional: path to a .ttf font that supports emojis
# On Windows: "seguiemj.ttf" often works, on Mac "AppleColorEmoji.ttc", or you can use default system font
font_path = "seguiemj.ttf"
font_size = 40

# --- CREATE CANVAS ---
canvas = Image.new('RGB', (canvas_width, canvas_height), background_color)
draw = ImageDraw.Draw(canvas)

# Load emoji-supporting font
try:
    font = ImageFont.truetype(font_path, font_size)
except:
    font = ImageFont.load_default()
    print("Warning: Emoji font not loaded, may not render emojis correctly.")

# --- PLACE EMOJIS ---
for _ in range(num_emojis):
    emoji = random.choice(emoji_list)
    x = random.randint(0, canvas_width - font_size)
    y = random.randint(0, canvas_height - font_size)
    color = tuple(random.randint(0, 255) for _ in range(3))
    draw.text((x, y), emoji, font=font, fill=color)

# --- SAVE POSTER ---
canvas.save("emoji_poster.png")
print("Emoji poster created: emoji_poster.png")
