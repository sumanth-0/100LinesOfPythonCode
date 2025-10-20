import pygame, random, sys
pygame.init()

# Screen
CELL, COLS, ROWS = 30, 10, 20
WIDTH, HEIGHT = CELL*COLS, CELL*ROWS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")

# Colors
BLACK, COLORS = (0,0,0), [(0,255,255),(0,0,255),(255,165,0),(255,255,0),(0,255,0),(128,0,128),(255,0,0)]

# Shapes
SHAPES = [
    [[1,1,1,1]], [[1,1],[1,1]], [[0,1,0],[1,1,1]],
    [[0,1,1],[1,1,0]], [[1,1,0],[0,1,1]], [[1,0,0],[1,1,1]], [[0,0,1],[1,1,1]]
]

board = [[0]*COLS for _ in range(ROWS)]

def new_piece():
    shape = random.choice(SHAPES)
    return {'shape':shape, 'x':COLS//2-len(shape[0])//2, 'y':0, 'color':random.choice(COLORS)}

def draw_board():
    screen.fill(BLACK)
    for y,row in enumerate(board):
        for x,val in enumerate(row):
            if val: pygame.draw.rect(screen,val,(x*CELL,y*CELL,CELL,CELL))
    for y,row in enumerate(piece['shape']):
        for x,val in enumerate(row):
            if val: pygame.draw.rect(screen,piece['color'],((piece['x']+x)*CELL,(piece['y']+y)*CELL,CELL,CELL))
    pygame.display.flip()

def valid(pos=None):
    pos = pos or piece
    for y,row in enumerate(pos['shape']):
        for x,val in enumerate(row):
            if val:
                nx, ny = pos['x']+x, pos['y']+y
                if nx<0 or nx>=COLS or ny>=ROWS or board[ny][nx]: return False
    return True

def lock():
    for y,row in enumerate(piece['shape']):
        for x,val in enumerate(row):
            if val: board[piece['y']+y][piece['x']+x]=piece['color']
    clear_lines()

def clear_lines():
    global board
    board=[row for row in board if any(v==0 for v in row)]
    while len(board)<ROWS: board.insert(0,[0]*COLS)

def rotate(p):
    p['shape'] = [list(row) for row in zip(*p['shape'][::-1])]

piece = new_piece()
fall_time = 0
fall_speed = 0.5

while True:
    fall_time += clock.get_rawtime()/1000
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT: piece['x']-=1; valid() or piece.__setitem__('x',piece['x']+1)
            if event.key==pygame.K_RIGHT: piece['x']+=1; valid() or piece.__setitem__('x',piece['x']-1)
            if event.key==pygame.K_DOWN: piece['y']+=1; valid() or piece.__setitem__('y',piece['y']-1)
            if event.key==pygame.K_UP: rotate(piece); valid() or rotate(piece); rotate(piece); rotate(piece)
    if fall_time>fall_speed:
        piece['y']+=1
        if not valid():
            piece['y']-=1
            lock()
            piece = new_piece()
            if not valid(): print("Game Over"); sys.exit()
        fall_time=0
    draw_board()
