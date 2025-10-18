import curses
import random
from collections import deque

def main(stdscr):
    # Initialize
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    
    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    
    # Initialize snake in the middle of screen
    snake = deque([(sh//2, sw//4), (sh//2, sw//4-1), (sh//2, sw//4-2)])
    
    # Initial food position
    food = None
    while food is None:
        nf = (random.randint(1, sh-2), random.randint(1, sw-2))
        food = nf if nf not in snake else None
    
    w.addch(food[0], food[1], curses.ACS_PI)
    
    # Initial direction
    key = curses.KEY_RIGHT
    
    # Score
    score = 0
    
    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key
        
        # Check if snake hits wall or itself
        head = snake[0]
        
        if key == curses.KEY_DOWN:
            new_head = (head[0] + 1, head[1])
        elif key == curses.KEY_UP:
            new_head = (head[0] - 1, head[1])
        elif key == curses.KEY_LEFT:
            new_head = (head[0], head[1] - 1)
        elif key == curses.KEY_RIGHT:
            new_head = (head[0], head[1] + 1)
        else:
            continue
        
        # Check wall collision
        if (new_head[0] in [0, sh-1] or 
            new_head[1] in [0, sw-1] or 
            new_head in snake):
            msg = f"Game Over! Score: {score} Press any key to exit"
            w.addstr(sh//2, sw//2 - len(msg)//2, msg)
            w.nodelay(0)
            w.getch()
            break
        
        snake.appendleft(new_head)
        
        # Check if snake got food
        if new_head == food:
            score += 1
            food = None
            while food is None:
                nf = (random.randint(1, sh-2), random.randint(1, sw-2))
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')
        
        w.addch(new_head[0], new_head[1], curses.ACS_CKBOARD)
        
        # Draw border
        w.border(0)
        
        # Display score
        score_text = f"Score: {score}"
        w.addstr(0, 2, score_text)
        
        w.refresh()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    print("Thanks for playing!")
