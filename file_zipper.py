"""
Simple File Zipper
------------------
A utility script that creates a ZIP archive from one or more files/directories
using Python's built-in zipfile module.

Usage:
    python file_zipper.py <output_zip_name> <path1> <path2> ...

Example:
    python file_zipper.py archive.zip file1.txt folder1
"""

import sys
import os
import zipfile


def zip_paths(output_zip, paths):
    """Create a ZIP archive from the provided file and directory paths."""
    try:
        with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
            for path in paths:
                if os.path.isfile(path):
                    # Add single file
                    zipf.write(path, arcname=os.path.basename(path))
                    print(f"Added file: {path}")

                elif os.path.isdir(path):
                    # Add entire directory
                    for root, _, files in os.walk(path):
                        for file in files:
                            full_path = os.path.join(root, file)
                            relative_path = os.path.relpath(full_path, path)
                            zipf.write(full_path, arcname=os.path.join(os.path.basename(path), relative_path))
                            print(f"Added file: {full_path}")

                else:
                    print(f"⚠️ Skipped (not found): {path}")

        print(f"\n✅ ZIP file created successfully: {output_zip}")

    except Exception as e:
        print(f"❌ Error while creating ZIP: {e}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python file_zipper.py <output_zip_name> <path1> <path2> ...")
        sys.exit(1)

    output_zip = sys.argv[1]
    paths = sys.argv[2:]

    zip_paths(output_zip, paths)


if __name__ == "__main__":
    main()
