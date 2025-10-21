# Random Pixel Art Creator

A Python tool that generates random pixel art images using PIL (Pillow) library. Create beautiful, customizable pixel art with various patterns, color palettes, and symmetry options.

## Features

- 🎨 **Multiple Color Palettes**: Vibrant, pastel, monochrome, and random color schemes
- 🔄 **Symmetry Options**: Create symmetric patterns (vertical, horizontal, both) or asymmetric designs
- 📐 **Customizable Grid**: Set custom grid size and pixel dimensions
- 🖼️ **PNG Output**: Save your pixel art as high-quality PNG images
- 📝 **ASCII Representation**: Convert pixel art to ASCII characters
- 🎲 **Random Generation**: Each run creates unique artwork

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Install Required Dependencies

```bash
pip install Pillow
```

## Usage

### Basic Usage

Run the script to generate three example pixel art images:

```bash
python random_pixel_art_creator.py
```

This will create:
- `pixel_art_vibrant_symmetric.png` - 16x16 grid with vibrant colors and both-axis symmetry
- `pixel_art_pastel_asymmetric.png` - 24x24 grid with pastel colors and no symmetry
- `pixel_art_monochrome_vertical.png` - 20x20 grid with grayscale colors and vertical symmetry

### Custom Usage

Create your own pixel art programmatically:

```python
from random_pixel_art_creator import PixelArtGenerator

# Create a generator with custom grid size and pixel size
generator = PixelArtGenerator(grid_size=32, pixel_size=10)

# Generate a color palette
generator.generate_color_palette(num_colors=8, palette_type='vibrant')

# Create a pattern with symmetry
generator.create_random_pattern(symmetry='both', density=0.7)

# Save the image
generator.save('my_pixel_art.png')

# Print ASCII representation
print(generator.to_ascii())
```

## Configuration Options

### Grid Size

- **grid_size**: Number of pixels in each dimension (default: 16)
- **pixel_size**: Size of each pixel in the output image in pixels (default: 20)

### Color Palette Types

- **vibrant**: Bright, saturated colors (RGB values 50-255)
- **pastel**: Soft, light colors (RGB values 150-255)
- **monochrome**: Grayscale palette
- **random**: Completely random colors (RGB values 0-255)

### Symmetry Options

- **none**: No symmetry, completely random
- **vertical**: Mirror left-right
- **horizontal**: Mirror top-bottom
- **both**: Mirror both axes (creates quarter-pattern)

### Density

Controls how filled the pixel art is:
- **0.0**: Empty (no pixels)
- **0.5**: Half filled (recommended)
- **1.0**: Completely filled

## Examples

### Example 1: Character-like Sprite

```python
generator = PixelArtGenerator(grid_size=16, pixel_size=20)
generator.generate_color_palette(num_colors=5, palette_type='vibrant')
generator.create_random_pattern(symmetry='both', density=0.6)
generator.save('character_sprite.png')
```

### Example 2: Abstract Art

```python
generator = PixelArtGenerator(grid_size=32, pixel_size=15)
generator.generate_color_palette(num_colors=12, palette_type='pastel')
generator.create_random_pattern(symmetry='none', density=0.4)
generator.save('abstract_art.png')
```

### Example 3: Retro Icon

```python
generator = PixelArtGenerator(grid_size=24, pixel_size=18)
generator.generate_color_palette(num_colors=6, palette_type='monochrome')
generator.create_random_pattern(symmetry='vertical', density=0.55)
generator.save('retro_icon.png')
```

## ASCII Art Feature

The tool can convert pixel art to ASCII representation:

```python
print(generator.to_ascii())
```

Output example:
```
                
  @@@@    @@@@  
  @@@@    @@@@  
  ####    ####  
  ####    ####  
################
################
  ::::    ::::  
  ::::    ::::  
```

## Class Reference

### PixelArtGenerator

#### Methods

- **`__init__(grid_size=16, pixel_size=20)`**: Initialize the generator
- **`generate_color_palette(num_colors=5, palette_type='vibrant')`**: Generate a color palette
- **`create_random_pattern(symmetry='none', density=0.5)`**: Create a random pattern
- **`render_to_image(background_color=(255, 255, 255))`**: Render to PIL Image object
- **`to_ascii(chars=' .:-=+*#%@')`**: Convert to ASCII art string
- **`save(filename=None)`**: Save the pixel art to a PNG file

## Tips for Best Results

1. **For character-like sprites**: Use `symmetry='both'` with `grid_size=16` and `density=0.6`
2. **For abstract art**: Use `symmetry='none'` with larger grid sizes and lower density
3. **For icons**: Use `symmetry='vertical'` or `'horizontal'` with moderate density
4. **For more variety**: Increase the number of colors in your palette
5. **For cleaner look**: Use lower density values (0.3-0.5)

## Output Files

All output files are saved as PNG images with transparent or white backgrounds. File names include timestamps when auto-generated.

## Requirements

- Python 3.6+
- Pillow (PIL) library

## Contributing

This project is part of the 100 Lines of Python Code initiative. Contributions and improvements are welcome!

## Related Issue

This implementation addresses [Issue #840](https://github.com/sumanth-0/100LinesOfPythonCode/issues/840) - Random Pixel Art Creator.

## License

This project follows the license of the parent repository.

## Acknowledgments

- Built with [Pillow](https://python-pillow.org/) - Python Imaging Library
- Inspired by retro pixel art and sprite design

---

*Generate unique pixel art every time you run it! Perfect for game sprites, icons, avatars, and creative projects.*
