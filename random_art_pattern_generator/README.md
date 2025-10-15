# Random Art Pattern Generator

## Description
A Python script that generates stunning random art patterns using turtle graphics. The program creates various artistic patterns including spirals, concentric circles, stars, fractal trees, and random polygons with vibrant, randomly generated colors.

## Features
- **Multiple Pattern Types**: Choose from 5 different pattern styles:
  - Spiral patterns with adjustable angles
  - Concentric circular patterns
  - Star patterns with varying points
  - Fractal tree patterns
  - Random polygon compositions
- **Dynamic Colors**: Uses HSV color space to generate vibrant, aesthetically pleasing random colors
- **Interactive Display**: Click-to-close interface for easy viewing
- **Randomized Generation**: Each run creates a unique artwork

## Requirements
- Python 3.x
- turtle (built-in Python library)
- random (built-in Python library)
- colorsys (built-in Python library)

## Usage
```python
python random_art_pattern_generator.py
```

The script will randomly select one of the five pattern types and generate a unique artwork. Click anywhere on the canvas to close the window.

## How It Works
1. Sets up a black canvas (800x800 pixels)
2. Randomly selects one of five pattern types
3. Generates the pattern using random colors from HSV color space
4. Displays the artwork until the user clicks to exit

## Example Patterns
- **Spiral**: Creates expanding spiral patterns with changing colors
- **Circular**: Draws concentric circles with decreasing radii
- **Star**: Generates multiple star shapes with random sizes and point counts
- **Fractal**: Produces recursive tree-like structures
- **Polygons**: Scatters random polygons across the canvas

## Customization
You can modify the pattern generation parameters in the `main()` function:
- Adjust size parameters for different pattern scales
- Change the number of iterations for more/less detail
- Modify color ranges in `get_random_color()` for different color schemes

## Author
Created as part of the 100 Lines of Python Code project

## License
This project is open source and available for educational purposes.
