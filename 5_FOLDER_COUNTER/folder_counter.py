
import os

class FolderCounter:
    def __init__(self, directory):
        self.directory = directory
        self.file_count = 0
        self.folder_count = 0

    def count_items(self):
        for root, dirs, files in os.walk(self.directory):
            self.folder_count += len(dirs)
            self.file_count += len(files)
        print(f"Mission Complete! 🚀 You've uncovered {self.folder_count} folders and {self.file_count} files in '{self.directory}'.")

if __name__ == "__main__":
    # Insert your chosen directory path below
    directory_path = input("Enter the directory to scan: ")
    counter = FolderCounter(directory_path)
    counter.count_items()
