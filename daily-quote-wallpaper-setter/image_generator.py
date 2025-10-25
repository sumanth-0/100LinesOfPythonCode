# daily-quote-wallpaper-setter/image_generator.py
from PIL import Image, ImageDraw, ImageFont
from typing import Tuple, List

FONT_PATH = "arial.ttf" 
MARGIN = 100

def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> List[str]:
    """Wraps text to fit within the specified maximum width."""
    lines = []
    if not text: return lines
    words = text.split()
    current_line = ""
    
    for word in words:
        line_plus_word = current_line + " " + word
        # Calculate text width (approximation using draw.textlength in modern PIL)
        text_width = draw.textlength(line_plus_word.strip(), font=font) 
        
        if text_width <= max_width:
            current_line = line_plus_word
        else:
            if current_line:
                lines.append(current_line.strip())
            current_line = word
            
    if current_line:
        lines.append(current_line.strip())
        
    return lines

def generate_wallpaper(img: Image.Image, quote: str, author: str) -> str:
    """Overlays the quote on the image and saves it."""
    draw = ImageDraw.Draw(img)
    OUTPUT_PATH = 'daily_wallpaper.png'
    
    try:
        font = ImageFont.truetype(FONT_PATH, 40)
        font_small = ImageFont.truetype(FONT_PATH, 30)
    except IOError:
        print("Using default font.")
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()

    full_text = quote + "\n" + author
    image_width, image_height = img.size
    max_text_width = image_width - 2 * MARGIN
    wrapped_lines = wrap_text(draw, full_text, font, max_text_width)
    
    line_height = font.size * 1.5 
    total_text_height = len(wrapped_lines) * line_height
    y_start = (image_height - total_text_height) / 2
    
    for line in wrapped_lines:
        text_width = draw.textlength(line, font=font)
        x_start = (image_width - text_width) / 2
        draw.text((x_start, y_start), line, font=font, fill=(255, 255, 255), align="center")
        y_start += line_height
    
    img.save(OUTPUT_PATH)
    return os.path.abspath(OUTPUT_PATH)

# End of image_generator.py (approx. 78 lines)
