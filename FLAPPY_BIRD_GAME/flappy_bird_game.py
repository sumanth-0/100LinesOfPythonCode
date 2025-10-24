import curses
import time
import random

FPS = 20
GRAVITY = 0.5 / FPS
FLAP = -6.0 / FPS
PIPE_SPACING = 30
PIPE_GAP = 12
PIPE_CHAR = '#'

class Pipe:
    def __init__(self, x, gap_y):
        self.x = x
        self.gap_y = gap_y
        self.passed = False

    def move(self, dx):
        self.x += dx

    def collides(self, bird_x, bird_y):
        if bird_x < int(self.x) or bird_x > int(self.x) + 1:
            return False
        if bird_y >= self.gap_y and bird_y < self.gap_y + PIPE_GAP:
            return False
        return True

def draw_bird(stdscr, y, x):
    try: stdscr.addstr(int(round(y)), x, 'O')
    except: pass

def draw_pipe(stdscr, pipe, max_y):
    x = int(round(pipe.x))
    for col in range(2):
        px = x + col
        for row in range(0, pipe.gap_y):
            try: stdscr.addstr(row, px, PIPE_CHAR)
            except: pass
        for row in range(pipe.gap_y + PIPE_GAP, max_y - 1):
            try: stdscr.addstr(row, px, PIPE_CHAR)
            except: pass

def game_loop(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(0)
    max_y, max_x = stdscr.getmaxyx()
    playable_h = max_y - 1
    bird_y = playable_h // 2
    bird_v = 0
    pipes = []
    score = 0
    gap_y = random.randint(3, playable_h - PIPE_GAP - 3)
    pipes.append(Pipe(max_x + 10, gap_y))
    while True:
        time.sleep(1 / FPS)
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key in (ord(' '), ord('w')):
            bird_v = FLAP
        bird_v += GRAVITY
        bird_y += bird_v
        bird_y = max(0, min(bird_y, playable_h - 1))
        for p in pipes:
            p.move(-1)
        if pipes and pipes[-1].x < max_x - PIPE_SPACING:
            gap_y = random.randint(3, playable_h - PIPE_GAP - 3)
            pipes.append(Pipe(max_x, gap_y))
        if pipes[0].x + 2 < 0:
            pipes.pop(0)
        for p in pipes:
            if not p.passed and p.x + 1 < 5:
                p.passed = True
                score += 1
        collided = bird_y >= playable_h - 1 or bird_y <= 0
        if not collided:
            for p in pipes:
                if p.collides(5, bird_y):
                    collided = True
                    break
        stdscr.erase()
        stdscr.addstr(0, 2, f"Score: {score}  Q to quit")
        draw_bird(stdscr, bird_y, 5)
        for p in pipes:
            draw_pipe(stdscr, p, playable_h)
        stdscr.refresh()
        if collided:
            stdscr.addstr(playable_h // 2, max_x // 2 - 5, "Game Over")
            stdscr.refresh()
            time.sleep(2)
            break

def main():
    curses.wrapper(game_loop)

if __name__ == "__main__":
    main()