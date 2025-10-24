# File Duplicates Remover

A simple Python script to automatically find and remove duplicate files in a specified directory. The program uses SHA-256 hashing to detect duplicates based on file content, not just file names.

---

## Features

- Scans a directory (and its subdirectories) for duplicate files.
- Compares files using SHA-256 hash for reliable detection.
- Automatically deletes duplicate files, keeping only one copy.
- Prints the path of each removed duplicate file.
- Lightweight and runs entirely in the terminal.

---

## How It Works

1. The user specifies a directory path as a command-line argument.
2. The script walks through all files in the directory and subdirectories.
3. For each file, it calculates a SHA-256 hash of its contents.
4. If a file's hash matches a previously seen hash, it is considered a duplicate and is deleted.
5. The script prints the path of each removed duplicate file.

---

## Usage

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the program with the directory you want to scan:
   ```bash
   python file_duplicates_remover.py <directory_path>
   ```
   Replace `<directory_path>` with the path to the folder you want to scan for duplicates.

---