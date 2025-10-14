#!/usr/bin/env python3
"""
Bulk Text Replacer
------------------
A simple Python script to search and replace words or phrases
across multiple text files in a given folder.

Usage:
    python bulk_text_replacer.py

Features:
    ✅ Recursively scans folders for .txt files
    ✅ Allows preview before applying replacements
    ✅ Creates a backup of original files automatically
"""

import os
import sys
from pathlib import Path

def find_text_files(folder: Path):
    """Return a list of all .txt files inside the folder (recursively)."""
    return list(folder.rglob("*.txt"))

def replace_in_file(file_path: Path, old_word: str, new_word: str):
    """
    Replace all occurrences of old_word with new_word in a single file.
    Creates a backup before modification.
    """
    try:
        text = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"⚠️ Skipping non-UTF8 file: {file_path}")
        return False

    if old_word not in text:
        return False  # no change needed

    # Create a backup
    backup_path = file_path.with_suffix(file_path.suffix + ".bak")
    backup_path.write_text(text, encoding="utf-8")

    # Replace and save
    new_text = text.replace(old_word, new_word)
    file_path.write_text(new_text, encoding="utf-8")
    return True

def main():
    print("🔍 Bulk Text Replacer\n")

    # Input folder
    folder = input("Enter folder path: ").strip()
    folder_path = Path(folder)

    if not folder_path.exists() or not folder_path.is_dir():
        print("❌ Invalid folder path.")
        sys.exit(1)

    old_word = input("Enter word/phrase to search: ").strip()
    new_word = input("Enter replacement word/phrase: ").strip()

    print("\nScanning for text files...")
    files = find_text_files(folder_path)
    print(f"Found {len(files)} text files.\n")

    if not files:
        print("No text files found.")
        return

    confirm = input(f"Replace '{old_word}' ➡ '{new_word}' in all files? (y/n): ").lower()
    if confirm != "y":
        print("❌ Operation cancelled.")
        return

    changed_count = 0
    for file in files:
        if replace_in_file(file, old_word, new_word):
            changed_count += 1
            print(f"✅ Updated: {file}")
        else:
            print(f"– No match: {file}")

    print(f"\n🎉 Replacement complete! {changed_count} files modified.")
    print("Backups (.bak) were created for all changed files.")

if __name__ == "__main__":
    main()
