import os
import random
import time
import ctypes

def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def get_wallpaper_images(folder_path):
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png', '.bmp'))]

def main():
    folder_path = input("Enter the folder path containing wallpapers: ")
    wallpaper_images = get_wallpaper_images(folder_path)

    if not wallpaper_images:
        print("No wallpapers found in the specified folder.")
        return

    print("Changing wallpaper every 2 hours...")
    while True:
        image = random.choice(wallpaper_images)
        change_wallpaper(image)
        print(f"Wallpaper changed to: {image}")
        time.sleep(7200)  # Sleep for 2 hours

if __name__ == "__main__":
    main()
