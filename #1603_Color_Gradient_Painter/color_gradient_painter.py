import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Gradient Painter")
clock = pygame.time.Clock()

def lerp(color1, color2, t):
    """Linear interpolation between two colors"""
    return tuple(int(c1 + (c2 - c1) * t) for c1, c2 in zip(color1, color2))

def random_color():
    """Generate a random RGB color"""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def horizontal_gradient(surf, color1, color2):
    """Create a smooth horizontal gradient"""
    for x in range(WIDTH):
        t = x / WIDTH
        color = lerp(color1, color2, t)
        pygame.draw.line(surf, color, (x, 0), (x, HEIGHT))

def radial_gradient(surf, center, color1, color2, max_radius):
    """Create a smooth radial gradient from center"""
    for radius in range(max_radius, 0, -2):
        t = 1 - (radius / max_radius)
        color = lerp(color1, color2, t)
        pygame.draw.circle(surf, color, center, radius)

# Main loop
running = True
color1 = random_color()
color2 = random_color()
mode = "horizontal"
last_switch = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Switch gradient mode and colors every 3 seconds
    current_time = pygame.time.get_ticks()
    if current_time - last_switch > 3000:
        color1 = random_color()
        color2 = random_color()
        mode = "radial" if mode == "horizontal" else "horizontal"
        last_switch = current_time
    
    # Draw gradient based on mode
    if mode == "horizontal":
        horizontal_gradient(screen, color1, color2)
    else:
        center = (WIDTH // 2, HEIGHT // 2)
        max_radius = int(math.sqrt((WIDTH // 2) ** 2 + (HEIGHT // 2) ** 2))
        radial_gradient(screen, center, color1, color2, max_radius)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
