# Simple File Zipper

This is a command-line utility that gathers all `.txt` files in its directory and compresses them into a new `.zip` archive.

## Description

This script demonstrates the power of Python's built-in `zipfile` module. It's a practical tool for basic file backup and compression.

When run, the script will:
1.  Create two dummy `.txt` files (`file1_to_zip.txt`, `file2_to_zip.txt`) for demonstration.
2.  Ask the user for a name for the output zip file.
3.  Use the `glob` module to find all files ending in `.txt`.
4.  Create a new `.zip` archive and add all found text files to it.

## Features

* **File Compression:** Creates a standard `.zip` archive.
* **Pattern Matching:** Uses `glob` to find all `.txt` files.
* **Practical Utility:** A useful script for simple backups.
* **Error Handling:** Includes `try...except` blocks for file I/O operations.

## How to Run

1.  Ensure you have Python 3 installed.
2.  Run the script from your terminal:
    ```sh
    python simple_zipper.py
    ```
3.  Follow the prompt to name your zip file.
4.  A new `.zip` archive will appear in the directory.

## Modules Used

* **`zipfile`**: (Python's built-in module for reading/writing zip archives)
* **`os`**: (Built-in module for creating test files)
* **`glob`**: (Built-in module for finding files that match a pattern)