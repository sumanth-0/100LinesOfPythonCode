import pygame
import random
import time

# --- Pygame Initialization & Constants ---
pygame.init()
FONT_SIZE = 16
W, H = 800, 600
SCREEN = pygame.display.set_mode((W, H))
pygame.display.set_caption("Digital Waterfall")
CLOCK = pygame.time.Clock()
BG_COLOR = (0, 0, 0) # Black background
STREAM_COLOR = (0, 255, 0) # Green stream
HEAD_COLOR = (200, 255, 200) # Bright head

# --- Grid and Character Setup ---
COLS = W // FONT_SIZE
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
FONT = pygame.font.SysFont('Consolas', FONT_SIZE, bold=True)
FALL_SPEED = 0.5 # Pixels/frame
SPAWN_CHANCE = 0.05 # Chance a stream starts in a column each frame

# Columns store [y_pos, length, speed, char_list]
streams = [None] * COLS

def get_char_surface(char, is_head):
    """Generates a text surface for drawing."""
    color = HEAD_COLOR if is_head else STREAM_COLOR
    return FONT.render(char, True, color)

# --- Main Animation Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Update/Draw streams
    SCREEN.fill(BG_COLOR)
    
    for x in range(COLS):
        stream = streams[x]
        
        # Spawn new stream
        if stream is None and random.random() < SPAWN_CHANCE:
            length = random.randint(10, 20)
            streams[x] = [0, length, random.uniform(2, 4), [random.choice(CHARS) for _ in range(length)]]
            continue # Skip update this frame
            
        if stream:
            y_pos, length, speed, chars = stream
            y_pos += speed # Move stream down
            
            # Draw stream characters
            for i in range(length):
                char = chars[i]
                current_y = int(y_pos - (i * FONT_SIZE))
                
                # Check if char is on screen
                if current_y >= 0 and current_y < H:
                    surface = get_char_surface(char, i == 0) # i=0 is the head
                    SCREEN.blit(surface, (x * FONT_SIZE, current_y))

                # Cycle characters to simulate change
                if random.random() < 0.05:
                    chars[i] = random.choice(CHARS)
            
            # Check if stream is fully off screen
            if y_pos - (length * FONT_SIZE) > H:
                streams[x] = None # Kill stream
            else:
                streams[x][0] = y_pos # Update position

    pygame.display.flip()
    CLOCK.tick(30) # 30 FPS

pygame.quit()
