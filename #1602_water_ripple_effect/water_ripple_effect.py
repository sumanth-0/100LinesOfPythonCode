import pygame
import sys
import math

# ----------------------------
# Settings
# ----------------------------
WIDTH, HEIGHT = 600, 400
BG_COLOR = (10, 10, 30)
DROP_COLOR = (0, 150, 255)
MAX_RADIUS = 100
GROWTH_SPEED = 2

# ----------------------------
# Initialize Pygame
# ----------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Water Ripple Effect")
clock = pygame.time.Clock()

# List to store active ripples
ripples = []

# ----------------------------
# Ripple class
# ----------------------------
class Ripple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 0
        self.alpha = 255

    def update(self):
        self.radius += GROWTH_SPEED
        self.alpha = max(255 - int(self.radius * 2.5), 0)

    def draw(self, surface):
        if self.alpha > 0:
            ripple_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(ripple_surface, (DROP_COLOR[0], DROP_COLOR[1], DROP_COLOR[2], self.alpha), (self.x, self.y), self.radius, 2)
            surface.blit(ripple_surface, (0, 0))

# ----------------------------
# Main loop
# ----------------------------
while True:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Add ripple on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            ripples.append(Ripple(x, y))

    # Update and draw ripples
    for ripple in ripples[:]:
        ripple.update()
        ripple.draw(screen)
        if ripple.alpha <= 0:
            ripples.remove(ripple)

    pygame.display.flip()
    clock.tick(60)
