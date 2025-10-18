#!/usr/bin/env python3
"""
Bulk PDF Splitter - Split multiple PDFs into individual pages

Usage:
    python bulk_pdf_splitter.py <input_folder> [output_folder]

Example:
    python bulk_pdf_splitter.py ./pdfs ./split_pdfs
"""

import sys
import os
from pathlib import Path
try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("Error: PyPDF2 is required. Install it with: pip install PyPDF2")
    sys.exit(1)

def split_pdf(pdf_path, output_dir):
    """Split a single PDF into individual pages."""
    try:
        reader = PdfReader(pdf_path)
        pdf_name = Path(pdf_path).stem
        total_pages = len(reader.pages)
        
        print(f"\nProcessing: {pdf_name}.pdf ({total_pages} pages)")
        
        for page_num in range(total_pages):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            
            # Create output filename with zero-padded page numbers
            output_filename = f"{pdf_name}_page_{page_num + 1:03d}.pdf"
            output_path = output_dir / output_filename
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            print(f"  Created: {output_filename}")
        
        return total_pages
    except Exception as e:
        print(f"  Error processing {pdf_path}: {e}")
        return 0

def bulk_split_pdfs(input_folder, output_folder=None):
    """Split all PDFs in the input folder."""
    input_path = Path(input_folder)
    
    if not input_path.exists() or not input_path.is_dir():
        print(f"Error: '{input_folder}' is not a valid directory")
        return
    
    # Set output folder
    if output_folder:
        output_path = Path(output_folder)
    else:
        output_path = input_path / "split_pdfs"
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_path}")
    
    # Find all PDF files
    pdf_files = list(input_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in '{input_folder}'")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to process")
    
    total_pages = 0
    successful = 0
    
    for pdf_file in pdf_files:
        pages = split_pdf(pdf_file, output_path)
        if pages > 0:
            total_pages += pages
            successful += 1
    
    print(f"\n{'='*50}")
    print(f"Summary: Processed {successful}/{len(pdf_files)} files")
    print(f"Total pages extracted: {total_pages}")
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bulk_pdf_splitter.py <input_folder> [output_folder]")
        print("\nExample: python bulk_pdf_splitter.py ./pdfs ./split_pdfs")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2] if len(sys.argv) > 2 else None
    
    bulk_split_pdfs(input_folder, output_folder)
