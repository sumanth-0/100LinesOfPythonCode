import os
import shutil
import glob
from pathlib import Path

def is_temp_file(filepath):
    """Check if file is temporary."""
    ext = Path(filepath).suffix.lower()
    name = Path(filepath).name.lower()
    return ext in ['.tmp', '.temp', '~'] or name.startswith('~$') or name.endswith('~')

def organize_documents(directory, dry_run=True):
    """Organize documents into subfolders by type."""
    folder_map = {
        '.pdf': 'Documents/PDFs',
        '.doc': 'Documents/Word',
        '.docx': 'Documents/Word',
        '.txt': 'Documents/Text',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.mp4': 'Videos',
        '.avi': 'Videos',
        '.mp3': 'Audio',
        '.wav': 'Audio'
    }
    
    deleted = 0
    organized = 0
    
    for root, dirs, files in os.walk(directory):
        # Delete temp files
        for file in files:
            filepath = os.path.join(root, file)
            if is_temp_file(filepath):
                if dry_run:
                    print(f"Would delete: {filepath}")
                else:
                    os.remove(filepath)
                deleted += 1
        
        # Organize documents
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in folder_map:
                src = os.path.join(root, file)
                dest_folder = os.path.join(directory, folder_map[ext])
                os.makedirs(dest_folder, exist_ok=True)
                dest = os.path.join(dest_folder, file)
                
                # Avoid overwrite; rename if needed
                counter = 1
                while os.path.exists(dest):
                    name, e = os.path.splitext(file)
                    dest = os.path.join(dest_folder, f"{name}_{counter}{e}")
                    counter += 1
                
                if dry_run:
                    print(f"Would move: {src} -> {dest}")
                else:
                    shutil.move(src, dest)
                organized += 1
    
    return deleted, organized

def main():
    directory = input("Enter directory path (default: current): ").strip() or '.'
    if not os.path.exists(directory):
        print("Directory not found.")
        return
    
    dry_run = input("Dry run? (y/n, default y): ").strip().lower() != 'n'
    run = input("Run? (y/n): ").strip().lower() == 'y'
    
    if run:
        deleted, organized = organize_documents(directory, dry_run)
        print(f"\nSummary: Deleted {deleted} temp files, Organized {organized} documents.")
        if dry_run:
            print("(Dry run - no changes made)")
    else:
        print("Aborted.")

if __name__ == "__main__":
    main()
