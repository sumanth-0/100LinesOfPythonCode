import pygame
import math
import random

# --- Pygame Initialization & Constants ---
pygame.init()
W, H = 800, 400
SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dancing Sine Wave")
CLOCK = pygame.time.Clock()

# --- Colors and Wave Parameters ---
BG_COLOR = (20, 20, 40) # Dark background
DOT_COLOR = (150, 200, 255) # Light blue dots
AMPLITUDE = 80 # Height of the wave
FREQUENCY = 0.02 # How many waves fit on screen (lower = more waves)
SPEED = 0.05 # How fast the wave moves horizontally
NUM_DOTS = 50 # Number of dots on the wave
DOT_RADIUS = 5

# --- Global Wave Offset ---
wave_offset = 0.0

# --- Main Animation Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill(BG_COLOR)
    
    # Update wave offset for movement
    wave_offset += SPEED
    
    # Calculate and draw dots
    for i in range(NUM_DOTS):
        # Evenly distribute dots across the screen width
        x = i * (W / (NUM_DOTS - 1))
        
        # Calculate y-position based on sine wave
        # Add wave_offset to x to make the wave appear to move
        y_wave = math.sin(x * FREQUENCY + wave_offset) 
        
        # Scale to amplitude and center vertically
        y = H / 2 + (y_wave * AMPLITUDE)
        
        # Add a subtle "dance" (random vertical offset) to each dot
        dance_offset = random.uniform(-5, 5) # Smaller range for subtle effect
        
        pygame.draw.circle(SCREEN, DOT_COLOR, (int(x), int(y + dance_offset)), DOT_RADIUS)
        
    pygame.display.flip()
    CLOCK.tick(60) # Smooth animation at 60 FPS

pygame.quit()
