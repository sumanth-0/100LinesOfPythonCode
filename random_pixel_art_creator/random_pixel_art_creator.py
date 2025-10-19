"""Random Pixel Art Creator

Generates random pixel art images using PIL (Pillow).
Can create both colorful pixel art and ASCII representations.

Features:
- Random color palette generation
- Symmetric patterns for more artistic results
- ASCII art output
- Customizable grid size and pixel size
- Save to PNG format
"""

import random
from PIL import Image, ImageDraw
import os
from datetime import datetime


class PixelArtGenerator:
    """Generate random pixel art with various patterns and color schemes."""
    
    def __init__(self, grid_size=16, pixel_size=20):
        """
        Initialize the pixel art generator.
        
        Args:
            grid_size: Number of pixels in each dimension (default: 16x16)
            pixel_size: Size of each pixel in the output image (default: 20)
        """
        self.grid_size = grid_size
        self.pixel_size = pixel_size
        self.image_size = grid_size * pixel_size
        self.grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.palette = []
        
    def generate_color_palette(self, num_colors=5, palette_type='vibrant'):
        """
        Generate a random color palette.
        
        Args:
            num_colors: Number of colors in the palette
            palette_type: Type of palette ('vibrant', 'pastel', 'monochrome', 'random')
        """
        self.palette = []
        
        if palette_type == 'vibrant':
            # Vibrant, saturated colors
            for _ in range(num_colors):
                r = random.randint(50, 255)
                g = random.randint(50, 255)
                b = random.randint(50, 255)
                self.palette.append((r, g, b))
                
        elif palette_type == 'pastel':
            # Soft, pastel colors
            for _ in range(num_colors):
                r = random.randint(150, 255)
                g = random.randint(150, 255)
                b = random.randint(150, 255)
                self.palette.append((r, g, b))
                
        elif palette_type == 'monochrome':
            # Grayscale palette
            for _ in range(num_colors):
                value = random.randint(50, 230)
                self.palette.append((value, value, value))
                
        else:  # random
            for _ in range(num_colors):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                self.palette.append((r, g, b))
    
    def create_random_pattern(self, symmetry='none', density=0.5):
        """
        Create a random pattern in the grid.
        
        Args:
            symmetry: Type of symmetry ('none', 'vertical', 'horizontal', 'both')
            density: Probability of filling a pixel (0.0 to 1.0)
        """
        if symmetry == 'vertical':
            # Create half and mirror vertically
            for y in range(self.grid_size):
                for x in range(self.grid_size // 2 + 1):
                    if random.random() < density:
                        color = random.choice(self.palette)
                        self.grid[y][x] = color
                        self.grid[y][self.grid_size - 1 - x] = color
                        
        elif symmetry == 'horizontal':
            # Create half and mirror horizontally
            for y in range(self.grid_size // 2 + 1):
                for x in range(self.grid_size):
                    if random.random() < density:
                        color = random.choice(self.palette)
                        self.grid[y][x] = color
                        self.grid[self.grid_size - 1 - y][x] = color
                        
        elif symmetry == 'both':
            # Create quarter and mirror both ways
            for y in range(self.grid_size // 2 + 1):
                for x in range(self.grid_size // 2 + 1):
                    if random.random() < density:
                        color = random.choice(self.palette)
                        self.grid[y][x] = color
                        self.grid[y][self.grid_size - 1 - x] = color
                        self.grid[self.grid_size - 1 - y][x] = color
                        self.grid[self.grid_size - 1 - y][self.grid_size - 1 - x] = color
                        
        else:  # no symmetry
            for y in range(self.grid_size):
                for x in range(self.grid_size):
                    if random.random() < density:
                        self.grid[y][x] = random.choice(self.palette)
    
    def render_to_image(self, background_color=(255, 255, 255)):
        """
        Render the grid to a PIL Image.
        
        Args:
            background_color: RGB tuple for background color
            
        Returns:
            PIL Image object
        """
        image = Image.new('RGB', (self.image_size, self.image_size), background_color)
        draw = ImageDraw.Draw(image)
        
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                if self.grid[y][x] is not None:
                    x_pos = x * self.pixel_size
                    y_pos = y * self.pixel_size
                    draw.rectangle(
                        [x_pos, y_pos, x_pos + self.pixel_size - 1, y_pos + self.pixel_size - 1],
                        fill=self.grid[y][x]
                    )
        
        return image
    
    def to_ascii(self, chars=' .:-=+*#%@'):
        """
        Convert the pixel art to ASCII representation.
        
        Args:
            chars: String of characters to use (from darkest to lightest)
            
        Returns:
            String containing ASCII art
        """
        ascii_art = []
        
        for y in range(self.grid_size):
            row = []
            for x in range(self.grid_size):
                if self.grid[y][x] is None:
                    row.append(' ')
                else:
                    # Calculate brightness from RGB
                    r, g, b = self.grid[y][x]
                    brightness = (r + g + b) / (3 * 255)
                    char_index = int(brightness * (len(chars) - 1))
                    row.append(chars[char_index])
            ascii_art.append(''.join(row))
        
        return '\n'.join(ascii_art)
    
    def save(self, filename=None):
        """
        Save the pixel art to a file.
        
        Args:
            filename: Output filename (default: auto-generated with timestamp)
        """
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f'pixel_art_{timestamp}.png'
        
        image = self.render_to_image()
        image.save(filename)
        print(f"Pixel art saved to {filename}")
        return filename


def main():
    """Main function to demonstrate the pixel art generator."""
    print("Random Pixel Art Creator")
    print("=" * 40)
    
    # Example 1: Vibrant symmetric pixel art
    print("\nGenerating vibrant symmetric pixel art...")
    generator1 = PixelArtGenerator(grid_size=16, pixel_size=20)
    generator1.generate_color_palette(num_colors=6, palette_type='vibrant')
    generator1.create_random_pattern(symmetry='both', density=0.6)
    filename1 = generator1.save('pixel_art_vibrant_symmetric.png')
    
    # Show ASCII representation
    print("\nASCII representation:")
    print(generator1.to_ascii())
    
    # Example 2: Pastel asymmetric pixel art
    print("\nGenerating pastel asymmetric pixel art...")
    generator2 = PixelArtGenerator(grid_size=24, pixel_size=15)
    generator2.generate_color_palette(num_colors=8, palette_type='pastel')
    generator2.create_random_pattern(symmetry='none', density=0.4)
    filename2 = generator2.save('pixel_art_pastel_asymmetric.png')
    
    # Example 3: Monochrome vertical symmetry
    print("\nGenerating monochrome vertical symmetric pixel art...")
    generator3 = PixelArtGenerator(grid_size=20, pixel_size=18)
    generator3.generate_color_palette(num_colors=5, palette_type='monochrome')
    generator3.create_random_pattern(symmetry='vertical', density=0.5)
    filename3 = generator3.save('pixel_art_monochrome_vertical.png')
    
    print("\n" + "=" * 40)
    print("All pixel art images generated successfully!")
    print(f"Files created: {filename1}, {filename2}, {filename3}")


if __name__ == '__main__':
    main()
