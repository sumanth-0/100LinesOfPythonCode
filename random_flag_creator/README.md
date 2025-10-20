# Random Flag Creator

A Python tool that generates random flags with ASCII/colors or PNG images using PIL/Pillow.

## Description

The Random Flag Creator is a fun and creative Python script that generates random flags in two formats:
1. **ASCII Art with ANSI Colors** - Displays colorful flags directly in your terminal
2. **PNG Images** - Creates high-quality flag images using PIL/Pillow

## Features

- 🎨 Multiple flag patterns:
  - Horizontal stripes
  - Vertical stripes
  - Cross pattern
  - And more!
- 🌈 Random color generation
- 🖥️ Terminal-based ASCII art with ANSI colors
- 🖼️ PNG image generation (requires PIL/Pillow)
- ⚙️ Customizable dimensions and stripe counts
- 📦 No external dependencies for ASCII mode

## Requirements

### Basic ASCII Mode
- Python 3.6+
- No external dependencies required!

### PNG Generation Mode
- Python 3.6+
- Pillow (PIL)

## Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/random_flag_creator
```

2. (Optional) Install Pillow for PNG generation:
```bash
pip install Pillow
```

## Usage

### Basic Usage

Run the script directly to generate random flags:

```bash
python random_flag_creator.py
```

This will:
- Display 3 ASCII flags in your terminal (horizontal, vertical, and cross patterns)
- Generate 3 PNG files (if PIL is installed): `flag_horizontal.png`, `flag_vertical.png`, `flag_cross.png`

### Example Output

#### ASCII Flags in Terminal
```
==================================================
Random Flag Creator
==================================================

1. Horizontal Striped Flag (ASCII):
████████████████████████████████████████
████████████████████████████████████████
████████████████████████████████████████
████████████████████████████████████████
...

2. Vertical Striped Flag (ASCII):
██████████████████████████████████████
██████████████████████████████████████
...

3. Cross Pattern Flag (ASCII):
████████████████████████████████████████
████████████████████████████████████████
...
```

#### PNG Files
The script generates three PNG flag files in the current directory.

## Customization

You can modify the `main()` function to customize:

- **Flag dimensions**: Change `width` and `height` parameters
- **Number of stripes**: Adjust the `stripes` parameter
- **Output filenames**: Modify the `filename` parameter

### Example Custom Usage

```python
from random_flag_creator import generate_png_horizontal_flag

# Generate a custom horizontal flag
generate_png_horizontal_flag(
    width=600, 
    height=400, 
    stripes=5, 
    filename='my_custom_flag.png'
)
```

## Functions

### ASCII Functions
- `generate_ascii_horizontal_flag(width, height, stripes)` - Creates horizontal striped ASCII flag
- `generate_ascii_vertical_flag(width, height, stripes)` - Creates vertical striped ASCII flag
- `generate_ascii_cross_flag(width, height)` - Creates cross pattern ASCII flag

### PNG Functions
- `generate_png_horizontal_flag(width, height, stripes, filename)` - Creates horizontal striped PNG
- `generate_png_vertical_flag(width, height, stripes, filename)` - Creates vertical striped PNG
- `generate_png_cross_flag(width, height, filename)` - Creates cross pattern PNG

### Utility Functions
- `random_color_rgb()` - Generates random RGB color tuple
- `random_ansi_color()` - Returns random ANSI color code

## Technical Details

- Uses ANSI escape codes for terminal colors
- Unicode block character (█) for ASCII art
- PIL/Pillow ImageDraw for PNG generation
- Predefined color palette with 10+ colors
- Graceful degradation if PIL is not available

## Contributing

This is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) project. Contributions are welcome!

## Issue Reference

Implemented for issue [#766 - Random Flag Creator](https://github.com/sumanth-0/100LinesOfPythonCode/issues/766)

## License

This project follows the license of the parent repository.

## Author

Created as part of Hacktoberfest 2025 contributions.

## Acknowledgments

- Thanks to the 100LinesOfPythonCode project maintainers
- Inspired by vexillology (the study of flags)

---

**Note**: The actual line count may exceed 100 lines to provide comprehensive functionality and proper documentation.
