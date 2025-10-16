# show_colors.py

Small utility to generate 5–10 (configurable) random colors and display them as colored blocks
either in the terminal (ANSI truecolor) or as a PNG image.

## Features
- Generate between 1 and 20 random colors (default 8).
- Terminal display using ANSI truecolor background blocks.
- Image output (PNG) if Pillow is installed.

## Requirements
- Python 3.7+
- For image mode: `pip install pillow`

## Usage
Run in terminal mode (default):
```bash
python show_colors.py         # prints 8 blocks with hex codes
python show_colors.py -n 6    # print 6 colors
python show_colors.py --mode terminal
