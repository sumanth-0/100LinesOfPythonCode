"""Smart File Deduplicator - Finds duplicate files by MD5 hash"""
import os, hashlib, sys
from pathlib import Path
from collections import defaultdict

def calculate_md5(filepath: Path) -> str:
    """Calculate MD5 hash"""
    md5 = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                md5.update(chunk)
        return md5.hexdigest()
    except: return None

def find_duplicates(directory: str):
    """Find duplicate files"""
    hash_map = defaultdict(list)
    print(f"🔍 Scanning: {directory}\n")
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = Path(root) / filename
            if filepath.is_file() and filepath.stat().st_size > 0:
                if hash_val := calculate_md5(filepath):
                    hash_map[hash_val].append(filepath)
    duplicates = {h: f for h, f in hash_map.items() if len(f) > 1}
    print(f"📊 Found {len(duplicates)} duplicate groups\n")
    return duplicates

def format_size(bytes_size: int) -> str:
    """Format bytes to readable size"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024: return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} TB"

def display_duplicates(duplicates):
    """Display duplicate files"""
    total_wasted = total_dups = 0
    for idx, (_, files) in enumerate(duplicates.items(), 1):
        size = files[0].stat().st_size
        wasted = size * (len(files) - 1)
        total_wasted += wasted
        total_dups += len(files) - 1
        print(f"📁 Group {idx} ({len(files)} copies) - {format_size(size)}:")
        for i, fp in enumerate(files, 1):
            print(f"  {'✓' if i == 1 else '🗑️ '} [{i}] {fp}")
        print(f"  💾 Wasted: {format_size(wasted)}\n")
    return total_dups, total_wasted

def delete_duplicates(duplicates):
    """Delete duplicate files (keeping first)"""
    deleted = 0
    for files in duplicates.values():
        for filepath in files[1:]:
            try:
                if input(f"Delete {filepath}? (y/n): ").lower() == 'y':
                    filepath.unlink()
                    deleted += 1
                    print(f"🗑️  Deleted: {filepath}")
            except Exception as e:
                print(f"❌ Error: {e}")
    return deleted

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: python file_deduplicator.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    if not Path(directory).is_dir():
        print(f"❌ Invalid directory: {directory}")
        sys.exit(1)
    duplicates = find_duplicates(directory)
    if not duplicates:
        print("✅ No duplicates found!")
        return
    dup_count, wasted = display_duplicates(duplicates)
    print(f"📈 Summary: {dup_count} duplicates, {format_size(wasted)} wasted")
    if input("\n🗑️  Delete all duplicates? (y/n): ").lower() == 'y':
        deleted = delete_duplicates(duplicates)
        print(f"\n✅ Deleted {deleted} files!")

if __name__ == "__main__":
    main()
