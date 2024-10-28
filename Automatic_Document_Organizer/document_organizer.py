import os
import shutil

class DocumentOrganizer:
    """Class to organize documents based on file type or keywords."""
    
    def __init__(self, download_folder):
        self.download_folder = download_folder
        self.folders = {
            'Documents': ['.pdf', '.docx', '.txt'],
            'Images': ['.jpg', '.jpeg', '.png'],
            'Videos': ['.mp4', '.avi'],
            'Music': ['.mp3', '.wav'],
            'Archives': ['.zip', '.tar', '.rar']
        }

    def organize_files(self):
        """Organize files in the download folder."""
        for filename in os.listdir(self.download_folder):
            file_path = os.path.join(self.download_folder, filename)
            if os.path.isfile(file_path):
                self.move_file(filename, file_path)

    def move_file(self, filename, file_path):
        """Move file to the appropriate folder based on its type."""
        for folder, extensions in self.folders.items():
            if any(filename.endswith(ext) for ext in extensions):
                target_folder = os.path.join(self.download_folder, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} to {target_folder}")
                return
        print(f"No matching folder for: {filename}")

def main():
    """Main function to organize downloaded documents."""
    download_folder = input("Enter the path to your download folder: ")
    organizer = DocumentOrganizer(download_folder)
    organizer.organize_files()

if __name__ == "__main__":
    main()
