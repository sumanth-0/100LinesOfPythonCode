# Screenshot to Text (OCR)

A Python script that extracts text from images using Optical Character Recognition (OCR) and saves the extracted text to a text file.

## Description

This tool uses pytesseract (Python wrapper for Tesseract OCR) and Pillow (Python Imaging Library) to read text from images such as screenshots, photos, or scanned documents.

## Requirements

- Python 3.x
- pytesseract
- Pillow (PIL)
- Tesseract OCR (system installation required)

## Installation

1. Install Tesseract OCR on your system:

   **Windows:**
   - Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
   - Add Tesseract to your PATH

   **macOS:**
   ```bash
   brew install tesseract
   ```

   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt-get install tesseract-ocr
   ```

2. Install Python dependencies:
   ```bash
   pip install pytesseract Pillow
   ```

## Usage

Basic usage with automatic output filename:
```bash
python screenshot_to_text_ocr.py <image_path>
```

Specify custom output filename:
```bash
python screenshot_to_text_ocr.py <image_path> <output_path>
```

### Examples

```bash
# Extract text from screenshot.png (creates screenshot_extracted_text.txt)
python screenshot_to_text_ocr.py screenshot.png

# Extract text and save to custom file
python screenshot_to_text_ocr.py image.jpg output.txt

# Works with various image formats
python screenshot_to_text_ocr.py document.jpeg extracted_text.txt
```

## Features

- Supports multiple image formats (PNG, JPEG, JPG, BMP, etc.)
- Automatic output filename generation based on input file
- UTF-8 encoding support for international characters
- Error handling for missing files and processing errors
- Preview of extracted text in console
- Command-line interface for easy integration

## Output

The script will:
1. Process the input image
2. Extract all readable text using OCR
3. Save the text to a .txt file with UTF-8 encoding
4. Display a preview of the extracted text in the console

## Notes

- OCR accuracy depends on image quality and text clarity
- Better results with high-resolution, clear images
- Works best with printed text rather than handwritten text
- Supports multiple languages (if configured in Tesseract)

## Issue Reference

Solves issue #687: Screenshot to Text (OCR) feature request
