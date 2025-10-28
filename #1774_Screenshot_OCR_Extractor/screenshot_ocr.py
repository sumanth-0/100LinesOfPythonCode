import pytesseract
from PIL import ImageGrab, Image
import pyautogui
import sys

def take_screenshot():
    """Take a screenshot of the entire screen"""
    print("📸 Taking screenshot...")
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    print("✅ Screenshot saved as 'screenshot.png'")
    return screenshot

def extract_text_from_image(image):
    """Extract text from image using OCR"""
    print("🔍 Extracting text using OCR...")
    text = pytesseract.image_to_string(image)
    return text

def main():
    print("=" * 50)
    print("📷 SCREENSHOT OCR EXTRACTOR")
    print("=" * 50)
    
    # Take screenshot
    screenshot = take_screenshot()
    
    # Extract text
    extracted_text = extract_text_from_image(screenshot)
    
    # Display results
    print("\n" + "=" * 50)
    print("📝 EXTRACTED TEXT:")
    print("=" * 50)
    print(extracted_text)
    
    # Save to file
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
    
    print("\n✅ Text saved to 'extracted_text.txt'")

if __name__ == "__main__":
    main()