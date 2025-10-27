#!/usr/bin/env python3
"""
count_files.py
----------------
Counts how many files of specific types (.png, .txt, .pdf)
exist in a given folder (including subfolders).

✅ Under 100 lines
✅ Uses pathlib for elegance
✅ Well-commented & easy to follow
✅ Includes a neat pluralization trick for output
"""

from pathlib import Path

def count_files_by_extension(folder: str, extensions=('png', 'txt', 'pdf')) -> dict:
    """
    Count files in `folder` (recursively) that match given extensions.
    Returns a dictionary: {extension: count}.
    """
    folder_path = Path(folder)
    if not folder_path.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    # Dictionary comprehension for elegance and brevity
    return {
        ext: sum(1 for _ in folder_path.rglob(f'*.{ext}'))
        for ext in extensions
    }

def display_results(results: dict) -> None:
    """
    Print results in a clean, readable format.
    Includes pluralization (e.g., '1 file' vs '2 files').
    """
    print("\n📊 File Type Counts:")
    print("-" * 25)
    for ext, count in results.items():
        suffix = "file" if count == 1 else "files"
        print(f"• {ext.upper()}: {count} {suffix}")

def main():
    import sys
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"🔍 Scanning folder: {folder}\n")

    try:
        results = count_files_by_extension(folder)
        display_results(results)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
