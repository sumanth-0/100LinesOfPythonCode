import pygame
import random
import math

# --- Pygame Initialization & Constants ---
pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recursive Circle Packer")
CLOCK = pygame.time.Clock()
BACKGROUND_COLOR = (20, 20, 30)
MAX_ATTEMPTS = 5000 # Max attempts to find an open spot
MAX_CIRCLES = 500

# --- Data Structure for Circles ---
circles = []

def check_overlap(x, y, r):
    """Checks if a potential circle overlaps any existing circle or screen edge."""
    # 1. Check screen boundaries
    if not (r < x < WIDTH - r and r < y < HEIGHT - r):
        return True 

    # 2. Check overlap with existing circles
    for circle in circles:
        dx = x - circle['x']
        dy = y - circle['y']
        distance_sq = dx*dx + dy*dy
        min_dist_sq = (r + circle['r'])**2
        
        if distance_sq < min_dist_sq:
            return True
    return False

def pack_circles():
    """Iteratively attempts to place non-overlapping circles."""
    circles.clear()
    
    attempts = 0
    while attempts < MAX_ATTEMPTS and len(circles) < MAX_CIRCLES:
        attempts += 1
        
        # 1. Choose random position
        x = random.uniform(0, WIDTH)
        y = random.uniform(0, HEIGHT)
        
        # 2. Start with a tiny circle
        r = 2
        
        # Optimization: quickly check if the initial small circle overlaps
        if check_overlap(x, y, r):
            continue

        # 3. Grow the circle until it hits something
        while not check_overlap(x, y, r + 1):
            r += 1

        # 4. If the circle grew to a reasonable size, save it
        if r >= 5:
            # Use Pygame's Color object for quick HSL->RGB conversion
            color = pygame.Color(0)
            color.hsla = (random.uniform(0, 360), 90, 60, 100)
            
            circles.append({
                'x': x,
                'y': y,
                'r': r,
                'color': color
            })
            
            # Reset attempts counter to prioritize filling space with successful circles
            attempts = 0

def draw_circles():
    """Draws all packed circles."""
    SCREEN.fill(BACKGROUND_COLOR)
    for circle in circles:
        pygame.draw.circle(SCREEN, circle['color'], 
                           (int(circle['x']), int(circle['y'])), 
                           int(circle['r']))

# --- Main Loop ---
pack_circles() # Generate the initial pattern

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # Press SPACE to regenerate
                pack_circles()

    draw_circles()
    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()