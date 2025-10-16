"""
Screenshot Renamer
Author: Diya Satish Kumar
Renames all screenshots in a folder with sequential names and timestamps.
"""

import os
from datetime import datetime

def rename_screenshots(folder_path):
    if not os.path.exists(folder_path):
        print("⚠️ Folder not found!")
        return

    files = [f for f in os.listdir(folder_path)
             if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if not files:
        print("📂 No screenshot files found in this folder.")
        return

    timestamp = datetime.now().strftime("%Y-%m-%d")
    files.sort()
    count = 1

    print(f"📸 Renaming {len(files)} screenshots in '{folder_path}'...\n")

    for old_name in files:
        ext = os.path.splitext(old_name)[1]
        new_name = f"screenshot_{timestamp}_{count:03d}{ext}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"✅ {old_name} → {new_name}")
        count += 1

    print("\n🎉 Renaming complete!")

if __name__ == "__main__":
    folder = input("Enter the folder path to rename screenshots: ").strip()
    rename_screenshots(folder)
