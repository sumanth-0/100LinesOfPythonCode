# daily-quote-wallpaper-setter/main_setter.py
import os
import sys
import platform
import ctypes
import subprocess # Added for common Linux desktop environments

# Import modules from the same directory
from api_fetcher import fetch_random_quote, fetch_background_image
from image_generator import generate_wallpaper 

def set_wallpaper_windows(image_path: str):
    """Sets the wallpaper on Windows systems via SystemParametersInfoW."""
    try:
        SPI_SETDESKWALLPAPER = 20
        # Needs full path with double backslashes
        path = image_path.replace('/', '\\')
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)
        print("Successfully set wallpaper on Windows.")
    except Exception as e:
        print(f"Error setting wallpaper on Windows: {e}")

def set_wallpaper_macos(image_path: str):
    """Sets the wallpaper on macOS systems via AppleScript."""
    try:
        script = f'tell application "Finder" to set desktop picture to POSIX file "{image_path}"'
        subprocess.run(["osascript", "-e", script], check=True)
        print("Successfully set wallpaper on macOS.")
    except Exception as e:
        print(f"Error setting wallpaper on macOS: {e}")
        
def set_wallpaper_linux(image_path: str):
    """Attempts to set the wallpaper on common Linux desktop environments."""
    desktop_environment = os.environ.get('XDG_CURRENT_DESKTOP', '').lower()
    
    try:
        if 'gnome' in desktop_environment or 'unity' in desktop_environment:
            subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{image_path}"], check=True)
        elif 'xfce' in desktop_environment:
            # XFCE uses a different utility
            subprocess.run(["xfconf-query", "-c", "xfce4-desktop", "-p", "/backdrop/screen0/monitor0/workspace0/last-image", "-s", image_path], check=True)
        else:
            print("Warning: Unknown Linux DE. Wallpaper set manually.")
            return

        print(f"Successfully set wallpaper on {desktop_environment.capitalize()}.")
        
    except Exception as e:
        print(f"Error setting wallpaper on Linux: {e}")

def set_wallpaper(image_path: str):
    """Sets the given image file as the desktop wallpaper based on OS."""
    os_name = platform.system()
    
    if os_name == "Windows":
        set_wallpaper_windows(image_path)
    elif os_name == "Darwin":
        set_wallpaper_macos(image_path)
    elif os_name == "Linux":
        set_wallpaper_linux(image_path)
    else:
        print(f"OS '{os_name}' not supported for automatic setting.")


if __name__ == "__main__":
    quote, author = fetch_random_quote()
    
    if not quote:
        sys.exit(1)
        
    img = fetch_background_image()
    image_path = generate_wallpaper(img, quote, author)
    set_wallpaper(image_path)
    
# End of main_setter.py (approx. 90 lines)