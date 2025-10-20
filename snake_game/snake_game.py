import pygame, random, sys
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK, GREEN, RED = (0,0,0), (0,255,0), (255,0,0)

# Snake and food
snake = [(100,100)]
dx, dy = CELL, 0
food = (random.randrange(0, WIDTH, CELL), random.randrange(0, HEIGHT, CELL))
score = 0
font = pygame.font.SysFont(None, 35)

def draw_snake():
    for x,y in snake:
        pygame.draw.rect(screen, GREEN, (x,y,CELL,CELL))

def draw_food():
    pygame.draw.rect(screen, RED, (*food,CELL,CELL))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dy==0: dx,dy=0,-CELL
            if e.key == pygame.K_DOWN and dy==0: dx,dy=0,CELL
            if e.key == pygame.K_LEFT and dx==0: dx,dy=-CELL,0
            if e.key == pygame.K_RIGHT and dx==0: dx,dy=CELL,0

    # Move snake
    x,y = snake[0]
    new_head = (x+dx, y+dy)
    if (new_head in snake or
        new_head[0]<0 or new_head[0]>=WIDTH or
        new_head[1]<0 or new_head[1]>=HEIGHT):
        print("Game Over! Score:", score); sys.exit()

    snake.insert(0,new_head)
    if new_head==food:
        score+=1
        food=(random.randrange(0, WIDTH, CELL),
              random.randrange(0, HEIGHT, CELL))
    else:
        snake.pop()

    screen.fill(BLACK)
    draw_snake(); draw_food()
    score_text=font.render(f"Score: {score}",True,(200,200,200))
    screen.blit(score_text,(10,10))
    pygame.display.flip()
    clock.tick(10)
