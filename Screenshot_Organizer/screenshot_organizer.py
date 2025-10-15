#!/usr/bin/env python3
"""
Screenshot Organizer - Automatically organize screenshots from Downloads to Screenshots folder
Issue #752: Move all screenshots from your downloads folder into a 'Screenshots' directory automatically.
"""

import os
import shutil
import time
from pathlib import Path
from datetime import datetime
import re


class ScreenshotOrganizer:
    """Organizes screenshots from Downloads folder to a dedicated Screenshots directory."""
    
    def __init__(self):
        """Initialize the Screenshot Organizer with default paths."""
        self.home = Path.home()
        self.downloads_folder = self.home / "Downloads"
        self.screenshots_folder = self.home / "Pictures" / "Screenshots"
        
        # Common screenshot filename patterns
        self.screenshot_patterns = [
            r'^Screenshot.*\.(png|jpg|jpeg)$',
            r'^Screen Shot.*\.(png|jpg|jpeg)$',
            r'^Capture.*\.(png|jpg|jpeg)$',
            r'^screenshot.*\.(png|jpg|jpeg)$',
            r'^.*screenshot.*\.(png|jpg|jpeg)$',
        ]
        
    def create_screenshots_directory(self):
        """Create the Screenshots directory if it doesn't exist."""
        if not self.screenshots_folder.exists():
            self.screenshots_folder.mkdir(parents=True, exist_ok=True)
            print(f"Created Screenshots directory at: {self.screenshots_folder}")
        else:
            print(f"Screenshots directory exists at: {self.screenshots_folder}")
    
    def is_screenshot(self, filename):
        """Check if a file matches screenshot naming patterns."""
        for pattern in self.screenshot_patterns:
            if re.match(pattern, filename, re.IGNORECASE):
                return True
        return False
    
    def get_screenshots_from_downloads(self):
        """Find all screenshot files in the Downloads folder."""
        screenshots = []
        
        if not self.downloads_folder.exists():
            print(f"Downloads folder not found: {self.downloads_folder}")
            return screenshots
        
        for file in self.downloads_folder.iterdir():
            if file.is_file() and self.is_screenshot(file.name):
                screenshots.append(file)
        
        return screenshots
    
    def organize_screenshot(self, screenshot_path):
        """Move a single screenshot to the Screenshots folder."""
        try:
            destination = self.screenshots_folder / screenshot_path.name
            
            # Handle duplicate filenames
            if destination.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                name_parts = screenshot_path.stem
                extension = screenshot_path.suffix
                new_name = f"{name_parts}_{timestamp}{extension}"
                destination = self.screenshots_folder / new_name
            
            shutil.move(str(screenshot_path), str(destination))
            print(f"Moved: {screenshot_path.name} -> {destination}")
            return True
            
        except Exception as e:
            print(f"Error moving {screenshot_path.name}: {e}")
            return False
    
    def organize_all_screenshots(self):
        """Organize all screenshots from Downloads to Screenshots folder."""
        print("\n=== Screenshot Organizer ===")
        print(f"Source: {self.downloads_folder}")
        print(f"Destination: {self.screenshots_folder}\n")
        
        # Create Screenshots directory
        self.create_screenshots_directory()
        
        # Get all screenshots
        screenshots = self.get_screenshots_from_downloads()
        
        if not screenshots:
            print("No screenshots found in Downloads folder.")
            return
        
        print(f"Found {len(screenshots)} screenshot(s) to organize:\n")
        
        # Move each screenshot
        success_count = 0
        for screenshot in screenshots:
            if self.organize_screenshot(screenshot):
                success_count += 1
        
        print(f"\nSuccessfully organized {success_count}/{len(screenshots)} screenshot(s).")


def main():
    """Main function to run the Screenshot Organizer."""
    organizer = ScreenshotOrganizer()
    organizer.organize_all_screenshots()


if __name__ == "__main__":
    main()
