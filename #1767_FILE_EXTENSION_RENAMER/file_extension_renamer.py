import os


def change_file_extensions(folder_path, old_ext, new_ext):
    for filename in os.listdir(folder_path):
        if filename.endswith(old_ext):
            base = filename[: -len(old_ext)]
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, base + new_ext)
            os.rename(old_file, new_file)


# Example usage:
# change_file_extensions('path/to/folder', '.txt', '.md')
