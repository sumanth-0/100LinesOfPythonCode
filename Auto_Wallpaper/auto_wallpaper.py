#!/usr/bin/env python3
"""
auto_wallpaper.py
Automatically change desktop wallpaper every few minutes from a local "wallpapers" folder.

Usage:
    python auto_wallpaper.py --interval 2 --random
    (By default, it will use ./wallpapers folder)

Arguments:
    --folder   Path to folder containing wallpapers (optional)
    --interval Interval in minutes between changes
    --random   Shuffle wallpapers each cycle (optional)

Works on:
    ✅ Windows (via ctypes)
    ✅ macOS (via osascript)
    ✅ Linux (GNOME, KDE supported via gsettings / feh)
"""

import os
import time
import random
import argparse
import platform
import subprocess
from pathlib import Path

# Detect OS
PLATFORM = platform.system().lower()

def set_wallpaper_windows(image_path):
    import ctypes
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def set_wallpaper_mac(image_path):
    script = f'''
    tell application "System Events"
        set desktopCount to count of desktops
        repeat with desktopNumber from 1 to desktopCount
            tell desktop desktopNumber
                set picture to POSIX file "{image_path}"
            end tell
        end repeat
    end tell
    '''
    subprocess.run(["osascript", "-e", script])

def set_wallpaper_linux(image_path):
    try:
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{image_path}"], check=True)
    except Exception:
        subprocess.run(["feh", "--bg-scale", image_path])

def set_wallpaper(image_path):
    if PLATFORM == "windows":
        set_wallpaper_windows(image_path)
    elif PLATFORM == "darwin":
        set_wallpaper_mac(image_path)
    elif PLATFORM == "linux":
        set_wallpaper_linux(image_path)
    else:
        raise NotImplementedError(f"Unsupported OS: {PLATFORM}")

def get_images(folder):
    exts = {".jpg", ".jpeg", ".png", ".bmp"}
    return [str(p) for p in Path(folder).glob("*") if p.suffix.lower() in exts]

def main():
    parser = argparse.ArgumentParser(description="Automatically change wallpaper every few minutes.")
    parser.add_argument("--folder", help="Path to the wallpaper folder (default: ./wallpapers)")
    parser.add_argument("--interval", type=int, default=5, help="Interval in minutes between changes")
    parser.add_argument("--random", action="store_true", help="Randomize wallpaper order")
    args = parser.parse_args()

    # Default to 'wallpapers' folder in same directory
    script_dir = Path(__file__).parent
    folder = Path(args.folder) if args.folder else script_dir / "wallpapers"

    if not folder.exists():
        print(f"⚠️ Folder not found: {folder}")
        return

    images = get_images(folder)
    if not images:
        print(f"⚠️ No images found in {folder}")
        return

    print(f"✅ Found {len(images)} wallpapers in {folder}")
    print(f"🕒 Changing every {args.interval} minute(s). Press Ctrl+C to stop.\n")

    try:
        while True:
            if args.random:
                random.shuffle(images)
            for img in images:
                print(f"🖼️ Setting wallpaper: {img}")
                set_wallpaper(img)
                time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\n🛑 Wallpaper changer stopped.")

if __name__ == "__main__":
    main()
