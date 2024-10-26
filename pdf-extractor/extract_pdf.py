import pytesseract
from pdf2image import convert_from_path
import os

# Configure the path to the Tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)
    
    # Initialize an empty string to store text
    extracted_text = ""
    
    # Loop through each image
    for i, image in enumerate(images):
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)
        extracted_text += f"--- Page {i + 1} ---\n{text}\n\n"
    
    return extracted_text

# Path to your PDF file
pdf_file_path = 'path/to/your/file.pdf'

# Extract text from the PDF
text = extract_text_from_pdf(pdf_file_path)

# Display the extracted text
print(text)

# Optionally save to a text file
with open('extracted_text.txt', 'w', encoding='utf-8') as f:
    f.write(text)
