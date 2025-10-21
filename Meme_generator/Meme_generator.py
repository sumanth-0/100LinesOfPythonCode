from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import sys

def load_image(image_path):
    """Load image from file or URL."""
    try:
        if image_path.startswith('http'):
            response = requests.get(image_path)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(image_path)
        return img.convert('RGB')
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def add_captions(img, top_text, bottom_text, font_size=40):
    """Add top and bottom captions to image."""
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Get image dimensions
    width, height = img.size
    
    # Text wrapping function
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split()
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] > max_width:
                if current_line:
                    lines.append(current_line.strip())
                    current_line = word + " "
                else:
                    lines.append(word)
            else:
                current_line = test_line
        if current_line:
            lines.append(current_line.strip())
        return lines
    
    # Top text
    top_lines = wrap_text(top_text.upper(), font, width - 20)
    y_offset = 10
    for line in top_lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) / 2
        draw.text((x, y_offset), line, fill='white', font=font, stroke_width=2, stroke_fill='black')
        y_offset += font_size + 5
    
    # Bottom text
    bottom_lines = wrap_text(bottom_text.upper(), font, width - 20)
    y_offset = height - (len(bottom_lines) * (font_size + 5)) - 10
    for line in bottom_lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (width - text_width) / 2
        draw.text((x, y_offset), line, fill='white', font=font, stroke_width=2, stroke_fill='black')
        y_offset += font_size + 5
    
    return img

def main():
    if len(sys.argv) < 4:
        print("Usage: python meme_generator.py <image_path_or_url> <top_text> <bottom_text> [output_path]")
        return
    
    image_path = sys.argv[1]
    top_text = sys.argv[2]
    bottom_text = sys.argv[3]
    output_path = sys.argv[4] if len(sys.argv) > 4 else "meme_output.jpg"
    
    img = load_image(image_path)
    if img:
        meme = add_captions(img, top_text, bottom_text)
        meme.save(output_path)
        print(f"Meme saved as {output_path}")
    else:
        print("Failed to create meme.")

if __name__ == "__main__":
    main()
