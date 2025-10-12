# Random Flag Creator

A Python script that generates random flag patterns using PIL (Pillow). This tool creates unique flags with various design patterns including horizontal stripes, vertical stripes, quadrants, and borders.

## Features

- **Multiple Flag Patterns:**
  - Horizontal stripes (2-5 colors)
  - Vertical stripes (2-5 colors)
  - Four-quadrant flags
  - Border flags with customizable border size

- **Customizable Options:**
  - Flag dimensions (width and height)
  - Output filename
  - Generate multiple flags at once

- **Random Colors:** Each flag uses randomly generated RGB colors

## Requirements

```bash
pip install Pillow
```

## Usage

### Basic Usage

Generate a single random flag with default settings:

```bash
python random_flag_creator.py
```

This creates a 600x400 pixel flag saved as `random_flag.png`.

### Custom Dimensions

```bash
python random_flag_creator.py --width 800 --height 600
```

### Custom Output Filename

```bash
python random_flag_creator.py --output my_flag.png
```

### Generate Multiple Flags

```bash
python random_flag_creator.py --number 5 --output flag.png
```

This generates 5 flags: `flag_1.png`, `flag_2.png`, etc.

### All Options Combined

```bash
python random_flag_creator.py -w 1000 -H 700 -o custom_flag.png -n 3
```

## Command-Line Arguments

- `-w, --width`: Flag width in pixels (default: 600)
- `-H, --height`: Flag height in pixels (default: 400)
- `-o, --output`: Output filename (default: random_flag.png)
- `-n, --number`: Number of flags to generate (default: 1)

## Examples

The script randomly selects from four flag designs:

1. **Horizontal Stripes**: 2-5 horizontal bands of random colors
2. **Vertical Stripes**: 2-5 vertical bands of random colors
3. **Quadrants**: Four equal sections, each with a random color
4. **Border**: A border with one color surrounding a center of another color

## Contributing

This project is part of [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode). Contributions are welcome!

## License

Open source - feel free to use and modify.
