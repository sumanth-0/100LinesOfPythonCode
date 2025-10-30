"""
random_art_collage.py

A Python program that automatically generates random abstract art
by drawing random shapes, colors, and text onto a canvas.

Each run produces a unique collage-like pattern with:
- Random circles, rectangles, and lines
- Random colors and transparencies
- Random text placements and sizes
"""

import pygame, random, sys

# --- Configuration ---
WIDTH, HEIGHT = 900, 600
SHAPE_COUNT = 100     # total number of random shapes
TEXT_COUNT = 8        # random text phrases count
BG_COLOR = (20, 20, 30)
FONT_NAMES = ["arial", "verdana", "timesnewroman", "couriernew"]

# Some random text phrases for artistic feel
WORDS = [
    "dream", "code", "flow", "energy", "pulse",
    "random", "vibe", "create", "art", "infinity"
]

def random_color(alpha=False):
    """Generate a random RGB or RGBA color."""
    color = [random.randint(0, 255) for _ in range(3)]
    if alpha:
        color.append(random.randint(50, 255))  # transparency
    return tuple(color)

def draw_random_shape(surface):
    """Draw a random shape (circle, rectangle, or line)."""
    shape_type = random.choice(["circle", "rect", "line"])
    color = random_color()
    if shape_type == "circle":
        pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        radius = random.randint(10, 100)
        pygame.draw.circle(surface, color, pos, radius, random.randint(1, 8))
    elif shape_type == "rect":
        rect = pygame.Rect(
            random.randint(0, WIDTH),
            random.randint(0, HEIGHT),
            random.randint(30, 200),
            random.randint(30, 200),
        )
        pygame.draw.rect(surface, color, rect, random.randint(0, 5))
    else:  # line
        start = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        end = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        pygame.draw.line(surface, color, start, end, random.randint(1, 6))

def draw_random_text(surface):
    """Draw random text at a random position and size."""
    text = random.choice(WORDS)
    font_name = random.choice(FONT_NAMES)
    size = random.randint(20, 100)
    font = pygame.font.SysFont(font_name, size, bold=random.choice([True, False]))
    color = random_color()
    rendered = font.render(text, True, color)
    x = random.randint(0, WIDTH - rendered.get_width())
    y = random.randint(0, HEIGHT - rendered.get_height())
    surface.blit(rendered, (x, y))

def generate_random_art():
    """Generate the abstract art collage and display it."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Random Art Collage Generator")
    clock = pygame.time.Clock()

    # Create a semi-transparent surface for layered look
    surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    surface.fill(BG_COLOR)

    # Draw random shapes
    for _ in range(SHAPE_COUNT):
        draw_random_shape(surface)

    # Draw random text
    for _ in range(TEXT_COUNT):
        draw_random_text(surface)

    # Display final art
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    print("Random art generated! Press any key or close window to exit.")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False
        clock.tick(30)

    # Optionally save the artwork
    filename = f"random_art_{random.randint(1000,9999)}.png"
    pygame.image.save(screen, filename)
    print(f"Artwork saved as {filename}")

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    generate_random_art()
