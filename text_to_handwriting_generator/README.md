# Text-to-Handwriting Generator

A Python script that converts input text to handwriting-style images using PIL (Python Imaging Library).

## Features

- Converts text to handwriting-style images
- Supports multiple handwriting-style fonts with automatic fallback
- Text wrapping to fit page width
- Customizable parameters:
  - Font size
  - Line spacing
  - Page margins
  - Background and text colors
- Interactive command-line interface
- Simple and easy to use

## Requirements

```bash
pip install Pillow
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/text_to_handwriting_generator
```

2. Install required dependencies:
```bash
pip install Pillow
```

## Usage

### Basic Usage

Run the script and follow the interactive prompts:

```bash
python text_to_handwriting_generator.py
```

The script will:
1. Prompt you to enter your text (press Ctrl+D on Unix/Mac or Ctrl+Z on Windows when done)
2. Ask for an output filename (default: handwriting.png)
3. Generate the handwriting-style image

### Programmatic Usage

You can also import and use the function directly in your Python code:

```python
from text_to_handwriting_generator import create_handwriting_image

text = "Hello, World!\nThis is handwritten text."
create_handwriting_image(
    text=text,
    output_path="my_handwriting.png",
    font_size=40,
    line_spacing=20,
    margin=50,
    page_width=800,
    bg_color=(255, 255, 255),
    text_color=(0, 0, 51)
)
```

## Parameters

- `text`: Input text to convert (supports multiple lines)
- `output_path`: Path to save the output image (default: "handwriting.png")
- `font_size`: Size of the font (default: 40)
- `line_spacing`: Spacing between lines in pixels (default: 20)
- `margin`: Margin around the text in pixels (default: 50)
- `page_width`: Width of the output image in pixels (default: 800)
- `bg_color`: Background color as RGB tuple (default: white)
- `text_color`: Text color as RGB tuple (default: dark blue)

## Example Output

The script will generate a PNG image with your text rendered in a handwriting-style font.

## Font Support

The script tries to use handwriting-style fonts in the following order:
1. Segoe Script
2. Bradley Hand
3. Comic Sans MS
4. Arial
5. Default PIL font (fallback)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is part of the 100LinesOfPythonCode repository.

## Issue Reference

This implementation addresses issue [#672](https://github.com/sumanth-0/100LinesOfPythonCode/issues/672) - Text-to-Handwriting Generator.
