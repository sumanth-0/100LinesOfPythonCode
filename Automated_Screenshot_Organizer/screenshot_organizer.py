#!/usr/bin/env python3
"""
Automated Screenshot Organizer
Scans directories for screenshots and organizes them by date, application, or category.
"""

import os
import shutil
from datetime import datetime
from pathlib import Path
import re

class ScreenshotOrganizer:
    def __init__(self, source_dir, dest_dir="organized_screenshots"):
        self.source_dir = Path(source_dir)
        self.dest_dir = Path(dest_dir)
        self.screenshot_patterns = [
            r'screenshot',
            r'screen shot',
            r'capture',
            r'snap',
            r'prtsc'
        ]
        
    def is_screenshot(self, filename):
        """Check if file is likely a screenshot based on naming patterns."""
        name_lower = filename.lower()
        return any(re.search(pattern, name_lower) for pattern in self.screenshot_patterns)
    
    def extract_date(self, filepath):
        """Extract date from file's modification time."""
        timestamp = filepath.stat().st_mtime
        return datetime.fromtimestamp(timestamp)
    
    def extract_app_name(self, filename):
        """Try to extract application name from screenshot filename."""
        patterns = [
            r'screenshot[_\s]+(\w+)',
            r'(\w+)[_\s]+screenshot',
        ]
        for pattern in patterns:
            match = re.search(pattern, filename.lower())
            if match:
                return match.group(1).capitalize()
        return "General"
    
    def organize_by_date(self):
        """Organize screenshots by year/month/day structure."""
        count = 0
        for file in self.source_dir.rglob('*'):
            if file.is_file() and self.is_screenshot(file.name):
                date = self.extract_date(file)
                dest_folder = self.dest_dir / "by_date" / str(date.year) / f"{date.month:02d}" / f"{date.day:02d}"
                dest_folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, dest_folder / file.name)
                count += 1
        return count
    
    def organize_by_app(self):
        """Organize screenshots by detected application name."""
        count = 0
        for file in self.source_dir.rglob('*'):
            if file.is_file() and self.is_screenshot(file.name):
                app_name = self.extract_app_name(file.name)
                dest_folder = self.dest_dir / "by_app" / app_name
                dest_folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, dest_folder / file.name)
                count += 1
        return count
    
    def organize_by_category(self):
        """Organize screenshots by file type/extension."""
        count = 0
        for file in self.source_dir.rglob('*'):
            if file.is_file() and self.is_screenshot(file.name):
                category = file.suffix.lower()[1:] or "no_extension"
                dest_folder = self.dest_dir / "by_category" / category
                dest_folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, dest_folder / file.name)
                count += 1
        return count

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Organize screenshots automatically")
    parser.add_argument("source", help="Source directory containing screenshots")
    parser.add_argument("-d", "--dest", default="organized_screenshots", help="Destination directory")
    parser.add_argument("-m", "--mode", choices=["date", "app", "category"], default="date", help="Organization mode")
    args = parser.parse_args()
    
    organizer = ScreenshotOrganizer(args.source, args.dest)
    if args.mode == "date":
        count = organizer.organize_by_date()
    elif args.mode == "app":
        count = organizer.organize_by_app()
    else:
        count = organizer.organize_by_category()
    print(f"Organized {count} screenshots successfully!")
