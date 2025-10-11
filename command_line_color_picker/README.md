# Command Line Color Picker

A simple command-line tool to convert colors between different formats (hex, RGB, color names) and display them in the terminal.

## Features

- **Multiple Input Formats**: Accepts colors as:
  - Hex codes (e.g., `#FF0000`, `#F00`)
  - RGB values (e.g., `rgb(255, 0, 0)`, `255,0,0`, `255 0 0`)
  - Color names (e.g., `red`, `blue`, `green`)

- **Color Display**: Shows a colored block in the terminal using ANSI escape codes

- **Format Conversion**: Outputs the color in all supported formats:
  - Hex format
  - RGB format
  - Individual R, G, B values
  - Color name (if it matches a known color)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/command_line_color_picker
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Basic Usage

```bash
python command_line_color_picker.py <color>
```

### Examples

**Using color names:**
```bash
python command_line_color_picker.py red
```

**Using hex codes:**
```bash
python command_line_color_picker.py "#FF0000"
python command_line_color_picker.py "#F00"
```

**Using RGB values:**
```bash
python command_line_color_picker.py "rgb(255, 0, 0)"
python command_line_color_picker.py "255,0,0"
python command_line_color_picker.py "255 0 0"
```

### Output Example

For the command `python command_line_color_picker.py red`:

```
[Colored block displayed in terminal]

Color Formats:
  HEX: #FF0000
  RGB: rgb(255, 0, 0)
  R: 255, G: 0, B: 0
  Name: Red
```

## Supported Color Names

The tool recognizes the following color names:
- red, green, blue
- white, black, gray
- yellow, cyan, magenta
- orange, purple, pink
- brown, lime, navy, teal

## Technical Details

- **Lines of Code**: ≤100 (as per project requirements)
- **Python Version**: Python 3.x
- **Dependencies**: None (standard library only)

## How It Works

1. **Parse Input**: The tool identifies the input format (hex, RGB, or color name)
2. **Convert to RGB**: All formats are normalized to RGB values
3. **Display Color**: Uses ANSI escape codes to show a colored block in the terminal
4. **Output Formats**: Converts and displays all format variations

## Contributing

Contributions are welcome! Feel free to:
- Add more color names
- Improve the display format
- Add new features (while staying under 100 lines)

## License

This project is part of the 100LinesOfPythonCode collection. See the main repository for license details.

## Issue Reference

This solution addresses issue #656 from the 100LinesOfPythonCode repository.
