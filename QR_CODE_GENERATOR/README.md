# QR Code Generator

A powerful yet simple Python QR code generator within 100 lines of code! Generate QR codes for any URL or text input with customization options.

## 📦 Files Included

1. **`qr_code_generator.py`** (75 lines) - Full-featured interactive generator with customization
2. **`simple_qr_generator.py`** (71 lines) - Quick and simple generator without customization  
3. **`demo_example.py`** - Shows programmatic usage examples

## ✨ Features

- ✅ Generate QR codes for any URL or text
- ✅ Multiple error correction levels (7% to 30% recovery)
- ✅ Customizable styles: Square, Rounded, or Circle modules
- ✅ Custom foreground and background colors
- ✅ Auto-save with timestamps
- ✅ Interactive command-line interface
- ✅ Clean, organized output folder

## 🚀 Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 📖 Usage

### Option 1: Full-Featured Generator (Recommended)

Run the main generator with all customization options:

```bash
python qr_code_generator.py
```

**Interactive prompts:**
1. Enter your text or URL
2. Choose error correction level (1-4)
3. Select QR code style (Square/Rounded/Circle)
4. Customize colors (hex format)
5. QR code generated and saved automatically!

### Option 2: Simple Generator

For quick QR code generation without customization:

```bash
python simple_qr_generator.py
```

### Option 3: Programmatic Usage

Use in your own Python scripts:

```python
from simple_qr_generator import generate_simple_qr

# Generate QR code
filepath = generate_simple_qr("https://github.com")
print(f"Saved to: {filepath}")
```

## 💡 Examples

### Generate a Website QR Code
```
Input: https://github.com
Error Correction: Medium (15%)
Style: Rounded
Colors: Black (#000000) on White (#FFFFFF)
```

### Generate a WiFi QR Code
```
Input: WIFI:T:WPA;S:MyNetwork;P:MyPassword;;
Style: Circle
```

### Generate Contact Info
```
Input: BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:+1-234-567-8900
EMAIL:john@example.com
END:VCARD
```

### Generate Plain Text
```
Input: Hello, World! Scan me to see this message.
```

## 📁 Output

All generated QR codes are saved in the `generated_qr_codes` folder:
- **Format**: `qr_code_YYYYMMDD_HHMMSS.png`
- **Type**: High-quality PNG images
- **Usage**: Ready to print, share, or embed

## 🎯 Error Correction Levels

| Level | Recovery | Best For |
|-------|----------|----------|
| Low (1) | 7% | Clean, controlled environments |
| Medium (2) | 15% | General use (Default) |
| Quartile (3) | 25% | Potential minor damage |
| High (4) | 30% | High-damage environments |

## 🎨 Style Options

- **Square**: Classic QR code appearance (Default)
- **Rounded**: Modern rounded corners
- **Circle**: Circular dots for unique look

## 📊 Code Stats

✅ **Main Script**: 75 lines (including comments)  
✅ **Simple Script**: 71 lines  
✅ Clean, readable, well-documented  
✅ Error handling included  
✅ Cross-platform compatible (Windows/Mac/Linux)

## 🔧 Requirements

- Python 3.6+
- qrcode[pil] library
- Pillow (PIL) library

## 💻 Advanced Usage

Generate QR codes from command line (demo):

```bash
python demo_example.py
```

This creates sample QR codes for:
- GitHub
- YouTube  
- Contact information
- Email
- Plain text

## 🎓 QR Code Use Cases

- **Websites**: Share URLs easily
- **WiFi**: Quick network access
- **Contact Cards**: vCard format
- **Payments**: Payment links or crypto addresses
- **App Downloads**: App store links
- **Event Registration**: Ticketing systems
- **Product Info**: Product details and manuals
- **Social Media**: Profile links

## 🐛 Troubleshooting

**Import errors**: Make sure you've installed requirements:
```bash
pip install -r requirements.txt
```

**Permission errors**: Ensure write access to current directory

**Invalid hex color**: Use format `#RRGGBB` (e.g., `#FF5733`)

## 📝 License

Free to use and modify for personal and commercial projects!

## 🤝 Contributing

Feel free to fork, modify, and improve! This is part of the 100 Lines of Python Code collection.

---

**Made with ❤️ in Python | Under 100 lines | Simple & Powerful**
