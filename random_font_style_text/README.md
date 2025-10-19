# Random Font Style Text Generator

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Description

A comprehensive Python tool that converts normal text into various Unicode styled text formats. This generator supports multiple font styles including bold, italic, script/cursive, monospace, and many special effects like circled, squared, inverted, and bubble text.

## Features

- **Multiple Unicode Font Styles:**
  - Bold (Mathematical Bold)
  - Italic (Mathematical Italic)
  - Bold Italic
  - Script/Cursive
  - Monospace
  - Sans-serif
  - Sans-serif Bold
  - Double-struck

- **Special Effects:**
  - Circled characters
  - Squared characters
  - Inverted/Flipped text
  - Bubble text
  - Small caps

- **Interactive CLI:**
  - Choose between random style or view all styles
  - Command-line argument support
  - Clean, formatted output

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/random_font_style_text
```

2. No external dependencies required - uses only Python standard library!

## Usage

### Basic Usage

Run the script and enter text when prompted:

```bash
python random_font_style_text.py
```

### Command Line Arguments

Provide text directly as command line arguments:

```bash
python random_font_style_text.py "Hello World"
```

### Interactive Options

When prompted, choose:
- `R` - Display text in a random style
- `A` - Display text in all available styles

## Example Output

```
============================================================
Random Font Style Text Generator
============================================================

Enter text to convert: Hello World

Original text: Hello World

------------------------------------------------------------

Show [A]ll styles or [R]andom style? (A/R): A

All available styles:

BOLD:
  𝐇𝐞𝐥𝐥𝐨 𝐖𝐨𝐫𝐥𝐝

ITALIC:
  𝐻𝑒𝑙𝑙𝑜 𝑊𝑜𝑟𝑙𝑑

SCRIPT:
  ℋℯ𝓁𝓁ℴ 𝒲ℴ𝓇𝓁𝒹

CIRCLED:
  ⒽⒺⓁⓁⓄ ⓌⓄⓇⓁⒹ

... and more!
============================================================
```

## Code Structure

The script is organized into a clean class-based structure:

```python
class FontStyleConverter:
    - __init__(): Initialize Unicode mappings
    - _create_mapping(): Create character mappings for styles
    - convert_text(): Convert text to Unicode style
    - circled_text(): Apply circled effect
    - squared_text(): Apply squared effect
    - inverted_text(): Flip text upside down
    - bubble_text(): Apply bubble effect
    - small_caps(): Convert to small capitals
    - apply_style(): Main method to apply any style
    - get_all_styles(): Return list of available styles
```

## How It Works

The generator uses Unicode character ranges to map regular ASCII characters to their styled equivalents:

- **Mathematical Alphanumeric Symbols** (U+1D400–U+1D7FF): Bold, italic, script, monospace, etc.
- **Enclosed Alphanumerics** (U+2460–U+24FF): Circled characters
- **Enclosed Alphanumeric Supplement** (U+1F100–U+1F1FF): Squared characters
- **Special Characters**: Custom mappings for inverted/flipped text

## Requirements

- Python 3.6 or higher
- No external dependencies

## Contributing

This project is part of the **100 Lines of Python Code** initiative. Contributions are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Related Issue

This implementation addresses issue [#770 - Random Font Style Text](https://github.com/sumanth-0/100LinesOfPythonCode/issues/770)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Thanks to the Unicode Consortium for the extensive character sets
- Part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) project
- Created for Hacktoberfest 2025

## Author

Created as a contribution to the 100LinesOfPythonCode project.

## Support

If you find this project helpful, please ⭐ star the repository!
