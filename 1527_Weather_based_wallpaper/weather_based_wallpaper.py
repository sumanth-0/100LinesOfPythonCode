import ctypes
import os
import sys

# --- (1) USER CONFIGURATION ---

# --- IMPORTANT ---
# You must create a folder and fill it with your own .jpg images.
# The image names *must* match the weather conditions.
#
# Examples: "Clear.jpg", "Clouds.jpg", "Rain.jpg", "Snow.jpg", "Fog.jpg"
#
# Use an absolute path (e.g., C:\...)
WALLPAPER_DIR = r"D:\wallpapers"

# --- (2) SCRIPT CONSTANTS ---

# Windows API constant for setting wallpaper
SPI_SETDESKWALLPAPER = 20

def set_windows_wallpaper(image_path):
    """
    Sets the desktop wallpaper for a Windows machine.
    """
    # Check if the file exists before trying to set it
    if not os.path.exists(image_path):
        print(f"\nOops! I couldn't find a wallpaper named:")
        print(f"{os.path.basename(image_path)}")
        print(f"Please check your wallpaper folder and try again.")
        return
        
    try:
        # Use ctypes to call the Windows API
        # The fix is here: it's "user32", not "user_32"
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER, 0, image_path, 3
        )
        print(f"\nSuccess! Wallpaper set to {os.path.basename(image_path)}")
    except Exception as e:
        print(f"Error setting wallpaper: {e}")

def main():
    

    # 1. Ask the user for the weather
    print("--- Weather Wallpaper ---")
    weather = input("What is the weather like? (e.g., Clear, Clouds, Rain, Snow): ")
    
    # 2. Clean up the input
    # .strip() removes whitespace, .capitalize() makes "clear" -> "Clear"
    weather_condition = weather.strip().capitalize()

    if not weather_condition:
        print("No input given. Exiting.")
        return
        
    # 3. Build the full path to the correct wallpaper
    # e.g., "C:\Users\YourUser\Pictures\WeatherWallpapers\Rain.jpg"
    wallpaper_path = os.path.join(WALLPAPER_DIR, f"{weather_condition}.jpg")
    
    # 4. Set the wallpaper
    set_windows_wallpaper(wallpaper_path)
    
    # Keep the console open for a moment so the user can see the result
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()