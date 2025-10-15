"""
Duplicate File Finder 🗂️
-------------------------
Identify duplicate image or other files in a directory by either filename or file content hash.

Usage:
    python duplicate_finder.py
"""

import os
import hashlib
from collections import defaultdict
from typing import Dict, List, Optional


def get_file_hash(file_path: str, algo: str = "md5", chunk_size: int = 4096) -> Optional[str]:
    """
    Return the hash of a file’s contents (binary-safe), or None if it can’t be read.
    Works for images, videos, and text files.
    """
    try:
        hasher = hashlib.new(algo)
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except (FileNotFoundError, PermissionError):
        return None


def find_duplicates(directory: str, mode: str = "hash") -> Dict[str, List[str]]:
    """
    Scan a directory recursively and return duplicates.
    mode: 'name' → match by filename
          'hash' → match by file content
    """
    duplicates = defaultdict(list)

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            key = file_name if mode == "name" else get_file_hash(file_path)
            if key:
                duplicates[key].append(file_path)

    # Keep only entries with more than one file
    return {k: v for k, v in duplicates.items() if len(v) > 1}


def print_duplicates(dupes: Dict[str, List[str]]) -> None:
    """Display duplicate file groups."""
    if not dupes:
        print("✅ No duplicate images/files found.")
        return

    print("🔍 Duplicate Files Found:")
    for key, paths in dupes.items():
        print(f"\n🔸 Key: {key}")
        for p in paths:
            print(f"   ➤ {p}")


def main() -> None:
    """Main entry point for the script."""
    directory = input("📁 Enter directory path to scan (default: current folder): ").strip() or "."
    mode = input("🔍 Find duplicates by 'name' or 'hash' (default: hash): ").strip().lower() or "hash"

    # Convert Windows backslashes for safety
    directory = os.path.normpath(directory)

    print(f"\nScanning '{directory}' for duplicates by {mode}...\n")
    duplicates = find_duplicates(directory, mode)
    print_duplicates(duplicates)

    if duplicates:
        print("\n✅ Scan complete. Duplicate files listed above.")
    else:
        print("\n✅ Scan complete. No duplicates found.")


if __name__ == "__main__":
    main()
