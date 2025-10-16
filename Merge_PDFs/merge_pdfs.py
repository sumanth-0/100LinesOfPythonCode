#!/usr/bin/env python3
"""
Merge PDFs by order or list using PyPDF2.

Usage:
    python merge_pdfs.py folder_path
    python merge_pdfs.py output.pdf folder_path
    python merge_pdfs.py output.pdf file1.pdf file2.pdf ...
"""

import os
import sys
from PyPDF2 import PdfMerger

def get_digit_prefix(filename: str):
    """Return the first digit found in the filename, or 9999 if none."""
    for ch in filename:
        if ch.isdigit():
            return int(ch)
    return 9999

def merge_from_folder(folder_path: str, output_path: str):
    """Merge all PDFs from a folder based on the first digit in their name."""
    pdfs = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ]
    pdfs.sort(key=lambda x: get_digit_prefix(os.path.basename(x)))
    merge_pdfs(pdfs, output_path)

def merge_pdfs(pdf_list, output_path):
    """Merge a list of PDFs in the given order."""
    merger = PdfMerger()
    for pdf in pdf_list:
        print(f"→ Adding: {pdf}")
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"✅ Merged PDF saved as: {output_path}")

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    # Case 1: only folder provided → create merged_output.pdf in that folder
    if len(args) == 1 and os.path.isdir(args[0]):
        folder = args[0]
        output = os.path.join(os.path.dirname(folder), "merged_output.pdf")
        merge_from_folder(folder, output)
        return

    # Case 2: output + folder
    if len(args) == 2 and os.path.isdir(args[1]):
        output, folder = args
        merge_from_folder(folder, output)
        return

    # Case 3: output + list of PDFs
    if len(args) >= 2:
        output = args[0]
        pdfs = args[1:]
        merge_pdfs(pdfs, output)
        return

    print(__doc__)

if __name__ == "__main__":
    main()
