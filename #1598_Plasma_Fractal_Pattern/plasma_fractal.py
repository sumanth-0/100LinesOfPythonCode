import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plasma Fractal Pattern")
clock = pygame.time.Clock()

def plasma(x, y, time):
    """Generate plasma value using multiple sine/cosine waves"""
    value = math.sin(x * 0.04 + time)
    value += math.sin(y * 0.03 + time * 1.3)
    value += math.sin((x + y) * 0.03 + time * 0.7)
    value += math.sin(math.sqrt(x * x + y * y) * 0.03 + time * 1.5)
    return value / 4.0  # Normalize to -1 to 1 range

def get_color(value):
    """Convert plasma value (-1 to 1) to RGB color"""
    # Shift and scale to 0-1 range
    t = (value + 1) / 2.0
    
    # Create smooth color transitions
    r = int(255 * abs(math.sin(t * math.pi * 2)))
    g = int(255 * abs(math.sin(t * math.pi * 2 + 2)))
    b = int(255 * abs(math.sin(t * math.pi * 2 + 4)))
    
    return (r, g, b)

def draw_plasma(surface, time):
    """Draw the plasma effect pixel by pixel"""
    pixel_array = pygame.PixelArray(surface)
    
    # Sample every 2 pixels for performance
    for y in range(0, HEIGHT, 2):
        for x in range(0, WIDTH, 2):
            value = plasma(x, y, time)
            color = get_color(value)
            # Draw 2x2 blocks for efficiency
            try:
                pixel_array[x:x+2, y:y+2] = color
            except:
                pass
    
    pixel_array.close()

# Main loop
running = True
time = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw plasma
    draw_plasma(screen, time)
    
    # Update display
    pygame.display.flip()
    
    # Increment time for animation
    time += 0.05
    
    clock.tick(FPS)

pygame.quit()
