# 📷 Screenshot OCR Extractor

Extract text from screenshots using Optical Character Recognition (OCR).

## 🚀 Features
- Takes full screen screenshot
- Extracts text using Tesseract OCR
- Saves screenshot and extracted text to files

## 📦 Installation
```bash
pip install pytesseract pillow pyautogui
```

**Note:** You also need to install Tesseract OCR:
- **Windows:** Download from https://github.com/UB-Mannheim/tesseract/wiki
- **Mac:** `brew install tesseract`
- **Linux:** `sudo apt install tesseract-ocr`

## 💻 Usage
```bash
python screenshot_ocr.py
```

## 📝 Output
- `screenshot.png` - The captured screenshot
- `extracted_text.txt` - The extracted text

## 🔧 Requirements
- Python 3.x
- pytesseract
- Pillow
- pyautogui