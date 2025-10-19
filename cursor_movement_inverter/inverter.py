import pyautogui
from pynput import mouse

# Get screen size
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
CENTER_X, CENTER_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

def invert_position(x, y):
    """
    Calculate the inverted cursor position relative to screen center.
    """
    dx = x - CENTER_X
    dy = y - CENTER_Y
    inverted_x = CENTER_X - dx
    inverted_y = CENTER_Y - dy
    # Clamp to screen bounds
    inverted_x = max(0, min(SCREEN_WIDTH - 1, inverted_x))
    inverted_y = max(0, min(SCREEN_HEIGHT - 1, inverted_y))
    return inverted_x, inverted_y

def on_move(x, y):
    """
    Moves the cursor to the inverted position relative to screen center.
    """
    inv_x, inv_y = invert_position(x, y)
    pyautogui.moveTo(inv_x, inv_y, duration=0)

def main():
    print("Cursor Inverter Active!")
    print("Move your mouse — it will move in the opposite direction.")
    print("Press Ctrl+C in the terminal to stop.")
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()

if __name__ == "__main__":
    main()
