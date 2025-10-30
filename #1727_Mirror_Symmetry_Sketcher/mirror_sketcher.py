import pygame
import math

# --- Pygame Initialization & Constants ---
pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Symmetrical Drawing Tool")
CLOCK = pygame.time.Clock()
CENTER = pygame.Vector2(WIDTH // 2, HEIGHT // 2)

# --- Drawing Parameters ---
DRAW_COLOR = (255, 255, 255) # White strokes
BACKGROUND_COLOR = (0, 0, 0) # Black background
STROKE_THICKNESS = 3
NUM_AXES = 8 # Number of symmetry axes (e.g., 2, 4, 6, 8, 12)

# --- Global State for Drawing ---
drawing = False
last_pos = None

# --- Main Drawing Surface ---
# We draw everything onto a separate surface that gets blitted to the screen
# This allows continuous drawing without constant screen clearing.
ART_SURFACE = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
ART_SURFACE.fill(BACKGROUND_COLOR + (0,)) # Transparent background initially

# --- Main Loop ---
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        
        # Mouse Button Down: Start drawing
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = pygame.Vector2(event.pos)
        
        # Mouse Button Up: Stop drawing
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None

        # Mouse Motion: Draw if 'drawing' flag is true
        if event.type == pygame.MOUSEMOTION and drawing:
            current_pos = pygame.Vector2(event.pos)
            
            # Draw the original stroke and its reflections
            for i in range(NUM_AXES):
                angle = (2 * math.pi / NUM_AXES) * i
                
                # Transform points relative to center for rotation
                p1_relative = last_pos - CENTER
                p2_relative = current_pos - CENTER
                
                # Apply rotation matrix
                rotated_p1_x = p1_relative.x * math.cos(angle) - p1_relative.y * math.sin(angle)
                rotated_p1_y = p1_relative.x * math.sin(angle) + p1_relative.y * math.cos(angle)
                
                rotated_p2_x = p2_relative.x * math.cos(angle) - p2_relative.y * math.sin(angle)
                rotated_p2_y = p2_relative.x * math.sin(angle) + p2_relative.y * math.cos(angle)
                
                # Transform back to screen coordinates
                rotated_p1 = pygame.Vector2(rotated_p1_x, rotated_p1_y) + CENTER
                rotated_p2 = pygame.Vector2(rotated_p2_x, rotated_p2_y) + CENTER

                pygame.draw.line(ART_SURFACE, DRAW_COLOR, 
                                 (int(rotated_p1.x), int(rotated_p1.y)), 
                                 (int(rotated_p2.x), int(rotated_p2.y)), 
                                 STROKE_THICKNESS)
            
            last_pos = current_pos
        
        # Keyboard Event: Clear screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: # 'C' to clear
                ART_SURFACE.fill(BACKGROUND_COLOR + (0,)) # Clear with transparent
            # Change number of axes with keys
            if event.key == pygame.K_UP:
                NUM_AXES = min(12, NUM_AXES + 2) # Max 12
            if event.key == pygame.K_DOWN:
                NUM_AXES = max(2, NUM_AXES - 2) # Min 2
            pygame.display.set_caption(f"Symmetrical Drawing Tool - Axes: {NUM_AXES}")

    # Display the accumulated art and then update the screen
    SCREEN.fill(BACKGROUND_COLOR) # Clear screen with opaque background color
    SCREEN.blit(ART_SURFACE, (0, 0))
    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()