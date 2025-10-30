"""
This script creates a flickering fire animation using Pygame.
It generates a grid of pixels with randomly varying colors that 
simulate rising flames using a smooth color gradient (red → orange → yellow → black).

The animation gives the illusion of fire flickering and moving upward.

Dependencies:
    - pygame (install via pip)
        pip install pygame
"""

import pygame
import random
import sys

def generate_fire_palette() -> list:
    """
    Generate a list of RGB color tuples representing the fire color gradient.
    The palette transitions from black to red, orange, yellow, and white.

    Returns:
        list: A list of (R, G, B) tuples for the fire color palette.
    """
    palette = []

    # Dark colors (bottom of the fire)
    for i in range(64):
        palette.append((i // 2, 0, 0))  # Dark reds

    # Red to orange transition
    for i in range(64, 128):
        palette.append((i, i // 4, 0))  # Bright red → orange

    # Orange to yellow transition
    for i in range(128, 192):
        palette.append((i, i // 2, 0))  # Orange → yellow

    # Bright yellow to white at the hottest parts
    for i in range(192, 256):
        palette.append((255, 255, i - 128))  # Yellow → white

    return palette


def create_fire_surface(width: int, height: int, palette: list) -> pygame.Surface:
    """
    Create and animate the fire effect using a pixel buffer.

    Args:
        width (int): Width of the fire area.
        height (int): Height of the fire area.
        palette (list): List of color tuples for the fire gradient.

    Returns:
        pygame.Surface: A surface containing the animated fire pixels.
    """
    # Initialize a 2D array for pixel intensities
    fire_pixels = [0] * (width * height)

    # Create a surface to draw the fire
    surface = pygame.Surface((width, height))

    def draw_fire():
        """Update the fire pixels and draw them on the surface."""
        nonlocal fire_pixels

        # Randomize the bottom row (fire source)
        for x in range(width):
            fire_pixels[(height - 1) * width + x] = random.randint(128, 255)

        # Propagate fire upward by averaging pixels below
        for y in range(height - 1):
            for x in range(width):
                # Get intensity below current pixel
                below = (y + 1) * width + x
                decay = random.randint(0, 3)  # Flicker randomness
                new_intensity = fire_pixels[below] - decay
                if new_intensity < 0:
                    new_intensity = 0

                # Slight horizontal movement for more natural flicker
                if x > 0 and random.random() < 0.5:
                    fire_pixels[y * width + x - 1] = new_intensity
                else:
                    fire_pixels[y * width + x] = new_intensity

        # Draw pixels onto surface
        pixel_array = pygame.PixelArray(surface)
        for y in range(height):
            for x in range(width):
                color_index = fire_pixels[y * width + x]
                pixel_array[x, y] = surface.map_rgb(palette[color_index])
        del pixel_array  # Unlock surface

    return surface, draw_fire


def run_fire_animation():
    """
    Initialize the Pygame window and run the flickering fire animation loop.

    Returns:
        None
    """
    pygame.init()

    # Screen dimensions
    screen_width = 640
    screen_height = 480

    # Create Pygame window
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flickering Fire Animation")

    # Generate fire color palette
    fire_palette = generate_fire_palette()

    # Fire area (smaller than screen for black borders)
    fire_width = 160
    fire_height = 120
    fire_surface, draw_fire = create_fire_surface(fire_width, fire_height, fire_palette)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update fire animation
        draw_fire()

        # Scale fire to fill the screen smoothly
        scaled_fire = pygame.transform.scale(fire_surface, (screen_width, screen_height))

        # Draw fire onto the screen
        screen.blit(scaled_fire, (0, 0))
        pygame.display.flip()

        # Control frame rate
        clock.tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    print("Starting flickering fire animation...")
    print("Press [ESC] or close the window to exit.\n")
    run_fire_animation()
