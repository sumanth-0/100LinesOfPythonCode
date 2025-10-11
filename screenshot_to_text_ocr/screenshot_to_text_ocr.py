#!/usr/bin/env python3
"""
Screenshot to Text (OCR) Converter
Extracts text from images using pytesseract and saves to a text file.
Requires: pytesseract, Pillow, tesseract-ocr installed on system
"""

import os
import sys
from PIL import Image
import pytesseract


def extract_text_from_image(image_path):
    """
    Extract text from an image using OCR.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Extracted text from the image
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        return text
    
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
        return None
    except Exception as e:
        print(f"Error processing image: {e}")
        return None


def save_text_to_file(text, output_path):
    """
    Save extracted text to a text file.
    
    Args:
        text (str): Text to save
        output_path (str): Path to the output text file
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Text successfully saved to '{output_path}'")
    
    except Exception as e:
        print(f"Error saving text to file: {e}")


def main():
    """
    Main function to handle command-line arguments and process the image.
    """
    if len(sys.argv) < 2:
        print("Usage: python screenshot_to_text_ocr.py <image_path> [output_path]")
        print("Example: python screenshot_to_text_ocr.py screenshot.png output.txt")
        sys.exit(1)
    
    # Get input image path
    image_path = sys.argv[1]
    
    # Get output path or create default one
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        # Create default output filename based on input filename
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        output_path = f"{base_name}_extracted_text.txt"
    
    print(f"Processing image: {image_path}")
    
    # Extract text from image
    extracted_text = extract_text_from_image(image_path)
    
    if extracted_text is not None:
        # Save to file
        save_text_to_file(extracted_text, output_path)
        print(f"\nExtracted text preview:")
        print("-" * 50)
        print(extracted_text[:200] if len(extracted_text) > 200 else extracted_text)
        if len(extracted_text) > 200:
            print("...")
        print("-" * 50)
    else:
        print("Failed to extract text from image.")
        sys.exit(1)


if __name__ == "__main__":
    main()
