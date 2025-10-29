import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainfall Effect - Uniform Speed")

clock = pygame.time.Clock()

BG_COLOR = (3, 3, 99)
RAIN_COLOR = (255, 255, 255)
SPLASH_COLOR = (150, 150, 255)

RAIN_SPEED = 8
WIND_SPEED = 0.1

class Drop:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.length = random.randint(12, 20)
        self.thickness = random.uniform(1, 2)
        self.alpha = random.randint(140, 200)

    def update(self):
        self.x += WIND_SPEED
        self.y += RAIN_SPEED
        if self.y > HEIGHT - 5:
            splashes.append(Splash(self.x, HEIGHT - 5))
            self.reset()

    def draw(self, surface):
        color = (*RAIN_COLOR, self.alpha)
        end_x = self.x + WIND_SPEED * 8
        end_y = self.y + self.length
        pygame.draw.line(surface, color, (self.x, self.y), (end_x, end_y), int(self.thickness))

class Splash:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.uniform(1, 2)
        self.alpha = 255

    def update(self):
        self.radius += 0.4
        self.alpha -= 10

    def draw(self, surface):
        if self.alpha > 0:
            color = (*SPLASH_COLOR, int(self.alpha))
            s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            pygame.draw.circle(s, color, (int(self.x), int(self.y)), int(self.radius), 1)
            surface.blit(s, (0, 0))

drops = [Drop() for _ in range(250)]
splashes = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BG_COLOR)

    for drop in drops:
        drop.update()
        drop.draw(screen)

    for splash in splashes[:]:
        splash.update()
        splash.draw(screen)
        if splash.alpha <= 0:
            splashes.remove(splash)

    pygame.display.flip()
    clock.tick(60)