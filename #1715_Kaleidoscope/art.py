import pygame
import sys
import math

# --- Constants (PEP 8) ---
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
BACKGROUND_COLOR = (10, 10, 20)  # A very dark blue
LINE_WIDTH = 2
SYMMETRY = 6  # Number of kaleidoscope wedges
ANGLE_STEP = 360 / SYMMETRY

def rotate_point(point, angle_rad):
    """Rotates a point (x, y) around the origin (0, 0)."""
    x, y = point
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    new_x = x * cos_a - y * sin_a
    new_y = x * sin_a + y * cos_a
    return new_x, new_y

def main():
    """Main function to run the kaleidoscope app."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Kaleidoscope (Press 'c' to clear)")
    # We draw onto this persistent surface to accumulate the drawing
    canvas = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    canvas.fill(BACKGROUND_COLOR)
    screen.blit(canvas, (0, 0))
    pygame.display.flip()
    drawing = False
    prev_pos = None
    running = True
    color_hue = 0  # For cycling colors
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_c:
                    canvas.fill(BACKGROUND_COLOR)  # Clear canvas
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    drawing = True
                    prev_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing = False
                    prev_pos = None
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    current_pos = event.pos
                    if prev_pos:
                        # Get a nice cycling color using HSL
                        color = pygame.Color(0, 0, 0)
                        color.hsla = (color_hue % 360, 100, 50, 100)
                        color_hue += 0.5
                        # Get coordinates relative to the center
                        p1_rel = (prev_pos[0] - CENTER[0], prev_pos[1] - CENTER[1])
                        p2_rel = (current_pos[0] - CENTER[0],
                                  current_pos[1] - CENTER[1])
                        # Get mirrored coordinates (reflection across x-axis)
                        p1_rel_m = (p1_rel[0], -p1_rel[1])
                        p2_rel_m = (p2_rel[0], -p2_rel[1])
                        for i in range(SYMMETRY):
                            angle_rad = math.radians(i * ANGLE_STEP)
                            # Rotate original and mirrored points
                            rp1 = rotate_point(p1_rel, angle_rad)
                            rp2 = rotate_point(p2_rel, angle_rad)
                            rp1_m = rotate_point(p1_rel_m, angle_rad)
                            rp2_m = rotate_point(p2_rel_m, angle_rad)
                            # Convert back to screen coordinates and draw
                            sp1 = (rp1[0] + CENTER[0], rp1[1] + CENTER[1])
                            sp2 = (rp2[0] + CENTER[0], rp2[1] + CENTER[1])
                            sp1_m = (rp1_m[0] + CENTER[0], rp1_m[1] + CENTER[1])
                            sp2_m = (rp2_m[0] + CENTER[0], rp2_m[1] + CENTER[1])
                            pygame.draw.line(canvas, color, sp1, sp2, LINE_WIDTH)
                            pygame.draw.line(canvas, color, sp1_m, sp2_m,
                                             LINE_WIDTH)
                    prev_pos = current_pos
        # Update the screen by copying the canvas to it
        screen.blit(canvas, (0, 0))
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()