# Tiny QR Code Generator

A lightweight Python script that generates QR codes from text or URLs using the `qrcode` library.

## Features

- Generate QR codes from any text or URL
- Command-line interface for easy use
- Customizable QR code size and border
- Save QR codes as PNG images
- Simple and intuitive error handling

## Requirements

- Python 3.6+
- `qrcode` library
- `pillow` library (dependency of qrcode)

## Installation

1. Install the required dependencies:

```bash
pip install qrcode[pil]
```

## Usage

### Basic Usage

Generate a QR code from text:

```bash
python tiny_qr_code_generator.py "Hello, World!"
```

Generate a QR code from a URL:

```bash
python tiny_qr_code_generator.py "https://github.com"
```

### Advanced Options

Specify output filename:

```bash
python tiny_qr_code_generator.py "https://github.com" -o github_qr.png
```

Customize QR code size (box size per pixel):

```bash
python tiny_qr_code_generator.py "Hello" -s 15
```

Customize border size:

```bash
python tiny_qr_code_generator.py "Hello" -b 2
```

Combine all options:

```bash
python tiny_qr_code_generator.py "Contact: +1234567890" -o contact.png -s 12 -b 3
```

### Command-Line Arguments

- `data` (required): Text or URL to encode in the QR code
- `-o, --output`: Output filename for the QR code image (default: `qr_code.png`)
- `-s, --size`: Box size for each QR code pixel (default: 10)
- `-b, --border`: Border size around the QR code (default: 4)

### Help

View all available options:

```bash
python tiny_qr_code_generator.py -h
```

## Examples

### Example 1: Simple Text QR Code

```bash
python tiny_qr_code_generator.py "Hello, World!"
```

Output: `qr_code.png` containing the encoded text

### Example 2: Website QR Code

```bash
python tiny_qr_code_generator.py "https://github.com/sumanth-0/100LinesOfPythonCode" -o repo_qr.png
```

Output: `repo_qr.png` containing a QR code that links to the repository

### Example 3: Contact Information

```bash
python tiny_qr_code_generator.py "Email: example@email.com" -o contact.png -s 15
```

Output: `contact.png` with larger QR code pixels

## How It Works

The script uses the `qrcode` library to:
1. Create a QR code instance with specified parameters
2. Add the input data to the QR code
3. Generate an image with black foreground and white background
4. Save the image to the specified output file

## Error Handling

The script includes error handling for:
- Invalid input data
- File writing issues
- Library import errors

All errors are reported to stderr with descriptive messages.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Created as part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) project.

## Related Issues

- Issue #666: Tiny QR Code Generator
