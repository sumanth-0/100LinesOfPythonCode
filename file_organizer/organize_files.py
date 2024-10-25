import os
import shutil

def organize_files(directory):
    # folder definition
    folders = {
        'Images': ['.png', '.jpg', '.jpeg', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.tar', '.rar']
    }

    # Creation of folders, if they don't exist 
    for folder in folders.keys():
        os.makedirs(os.path.join(directory, folder), exist_ok=True)

    # Move files to the appropriate folder
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # Check if it is a file
            moved = False
            for folder, extensions in folders.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    print(f'Moved: {filename} to {folder}')
                    break
            if not moved:
                print(f'No folder found for: {filename}')

if __name__ == "__main__":
    # Prompt user for the directory to organize
    directory_to_organize = input("Enter the directory to organize: ")
    organize_files(directory_to_organize)
