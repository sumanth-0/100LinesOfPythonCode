import os
import zipfile
import glob

print("--- Simple File Zipper ---")
print("This script will find all .txt files and add them to a new .zip archive.")

# --- 1. Create dummy files to zip ---
# This makes the script easy to test immediately.
try:
    with open("file1_to_zip.txt", "w") as f:
        f.write("This is the first test file.")
    with open("file2_to_zip.txt", "w") as f:
        f.write("This is the second test file.")
    print("Created 'file1_to_zip.txt' and 'file2_to_zip.txt' for testing.")
except IOError as e:
    print(f"Error creating test files: {e}")
    exit() # Exit if we can't even write files

# --- 2. Get the desired archive name ---
zip_name = input("Enter the name for your new zip file (e.g., 'archive.zip'): ")
if not zip_name.endswith(".zip"):
    zip_name += ".zip" # Ensure it has the .zip extension

# --- 3. Find all .txt files in the current directory ---
# glob.glob is a simple way to find files matching a pattern
txt_files = glob.glob("*.txt")

if not txt_files:
    print("No .txt files were found in this directory to zip.")
else:
    print(f"\nFound {len(txt_files)} .txt file(s):")
    for f in txt_files:
        print(f"  - {f}")
        
    # --- 4. Create the zip file and add files ---
    try:
        # 'w' mode means write a new zip file (will overwrite if it exists)
        with zipfile.ZipFile(zip_name, 'w') as zf:
            for file_path in txt_files:
                # Add the file to the zip archive
                zf.write(file_path)
                # Optional: Remove the original file after zipping
                # os.remove(file_path) 
        
        print(f"\nSuccessfully created '{zip_name}' containing {len(txt_files)} file(s).")
        
    except Exception as e:
        print(f"\nAn error occurred while creating the zip file: {e}")