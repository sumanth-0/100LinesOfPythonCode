# wallpaper_setter.py
"""
Script to fetch a random quote, overlay it on a background image, and set it as the desktop wallpaper.
"""
import requests
from PIL import Image, ImageDraw, ImageFont
import os
import sys
import platform
import ctypes # For Windows
import random
from io import BytesIO

# --- CONFIGURATION ---
QUOTE_API_URL = "https://api.quotable.io/random" # Simple public quote API
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080
OUTPUT_PATH = 'daily_wallpaper.png'
FONT_PATH = "arial.ttf" # Use a standard font or provide a path
BACKGROUND_IMAGE_URL = "https://picsum.photos/1920/1080" # Random background image API

# --- API FETCHING ---

def fetch_random_quote() -> str:
    """Fetches a random quote from a public API."""
    print("Fetching random quote...")
    try:
        response = requests.get(QUOTE_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        quote = data.get('content', "Be the change that you wish to see in the world.")
        author = data.get('author', "Unknown")
        return f'"{quote}"\n— {author}'
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}. Using fallback quote.")
        return "Failure is the opportunity to begin again more intelligently.\n— Henry Ford"

def fetch_background_image() -> Image.Image:
    """Fetches a random background image and returns it as a PIL Image object."""
    print("Fetching random background image...")
    try:
        response = requests.get(BACKGROUND_IMAGE_URL, stream=True, timeout=10)
        response.raise_for_status()
        return Image.open(BytesIO(response.content)).resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}. Using a solid black background.")
        return Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT), color='black')

# --- IMAGE PROCESSING ---

def generate_wallpaper(quote_text: str) -> str:
    """Generates the image file with the quote overlaid."""
    img = fetch_background_image()
    draw = ImageDraw.Draw(img)
    
    # Try to load a font, otherwise use the default Pillow font
    try:
        font = ImageFont.truetype(FONT_PATH, 40)
    except IOError:
        print("Using default font. Install 'arial.ttf' for better output.")
        font = ImageFont.load_default()

    # Text wrapping logic
    margin = 50
    fill_color = (255, 255, 255) # White text
    
    # Simple line break logic for text wrapping
    def wrap_text(text, font, max_width):
        lines = []
        if not text: return lines
        words = text.split()
        current_line = ""
        for word in words:
            # Check if the line + new word is too wide
            if draw.textsize(current_line + " " + word, font=font)[0] <= max_width:
                current_line += " " + word
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word
        if current_line:
            lines.append(current_line.strip())
        return lines

    # Wrap the text to fit the image width
    max_text_width = IMAGE_WIDTH - 2 * margin
    wrapped_lines = wrap_text(quote_text, font, max_text_width)
    
    # Calculate total height of the text block
    line_height = draw.textsize("Hg", font=font)[1] * 1.2
    total_text_height = len(wrapped_lines) * line_height
    
    # Center text vertically and horizontally
    y_start = (IMAGE_HEIGHT - total_text_height) / 2
    
    for line in wrapped_lines:
        text_width, _ = draw.textsize(line, font=font)
        x_start = (IMAGE_WIDTH - text_width) / 2
        draw.text((x_start, y_start), line, font=font, fill=fill_color, align="center")
        y_start += line_height
    
    img.save(OUTPUT_PATH)
    print(f"Wallpaper saved to {os.path.abspath(OUTPUT_PATH)}")
    return os.path.abspath(OUTPUT_PATH)

# --- SYSTEM INTEGRATION ---

def set_wallpaper(image_path: str):
    """Sets the given image file as the desktop wallpaper based on OS."""
    os_name = platform.system()
    print(f"Attempting to set wallpaper for OS: {os_name}")

    try:
        if os_name == "Windows":
            # Windows API call via ctypes
            SPI_SETDESKWALLPAPER = 20
            # Needs full path with double backslashes
            path = image_path.replace('/', '\\')
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
            print("Successfully set wallpaper on Windows.")
            
        elif os_name == "Darwin": # macOS
            # macOS uses a shell command (AppleScript)
            script = f'tell application "Finder" to set desktop picture to POSIX file "{image_path}"'
            os.system(f"osascript -e '{script}'")
            print("Successfully set wallpaper on macOS (AppleScript).")

        elif os_name == "Linux":
            # Linux is complex; try common DE commands (gnome, cinnamon, etc.)
            desktop_environment = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
            
            if 'gnome' in desktop_environment or 'unity' in desktop_environment:
                os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{image_path}")
            elif 'cinnamon' in desktop_environment:
                os.system(f"gsettings set org.cinnamon.desktop.background picture-uri file://{image_path}")
            elif 'xfce' in desktop_environment:
                os.system(f"xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s {image_path}")
            else:
                print("Warning: Unknown Linux desktop environment. Could not set wallpaper automatically.")
                return

        else:
            print(f"Warning: OS '{os_name}' not supported for automatic wallpaper setting.")
            return
            
    except Exception as e:
        print(f"Error setting wallpaper: {e}")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Ensure dependencies are installed (requests, pandas, pillow)
    if "Pillow" not in sys.modules and "requests" not in sys.modules:
        print("Please install required packages: pip install requests pillow")
        sys.exit(1)
        
    quote = fetch_random_quote()
    if not quote:
        print("Could not retrieve a quote. Exiting.")
        sys.exit(1)
        
    image_path = generate_wallpaper(quote)
    set_wallpaper(image_path)