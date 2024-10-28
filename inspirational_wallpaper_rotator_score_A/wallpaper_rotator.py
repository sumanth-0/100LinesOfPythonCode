import os
import time
import random
import ctypes

class WallpaperRotator:
    def __init__(self, wallpaper_folder, interval):
        self.wallpaper_folder = wallpaper_folder
        self.interval = interval

    def get_wallpapers(self):
        """Get a list of wallpaper files from the specified folder."""
        return [os.path.join(self.wallpaper_folder, file) for file in os.listdir(self.wallpaper_folder) if file.endswith(('.jpg', '.png'))]

    def set_wallpaper(self, wallpaper_path):
        """Set the wallpaper using the Windows API."""
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)

    def start_rotating(self):
        """Start rotating wallpapers at the specified interval."""
        wallpapers = self.get_wallpapers()
        while True:
            wallpaper = random.choice(wallpapers)
            self.set_wallpaper(wallpaper)
            print(f"Wallpaper set to: {wallpaper}")
            time.sleep(self.interval)

def main():
    """Main function to run the wallpaper rotator."""
    wallpaper_folder = input("Enter the folder path with wallpapers: ")
    interval = int(input("Enter the interval in seconds to change the wallpaper: "))
    
    rotator = WallpaperRotator(wallpaper_folder, interval)
    rotator.start_rotating()

if __name__ == "__main__":
    main()
