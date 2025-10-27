import os
import time
import msvcrt

def main():
    print("--- ASCII Art Drawing ---")
    print("Use arrow keys to move, SPACE to draw, 'c' to clear, 'q' to quit.")
    print("Press any other key to change the drawing character.")
    input("Press Enter to start drawing...")
    
    if os.name != 'nt':
        print("This script is designed for Windows terminals.")
        return

    WIDTH, HEIGHT = 60, 20
    cursor_x, cursor_y = WIDTH // 2, HEIGHT // 2
    draw_char = '#'
    
    canvas = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if key == b'\xe0' or key == b'\x00':
                key = msvcrt.getch()
                if key == b'H':
                    cursor_y = max(0, cursor_y - 1)
                elif key == b'P':
                    cursor_y = min(HEIGHT - 1, cursor_y + 1)
                elif key == b'K':
                    cursor_x = max(0, cursor_x - 1)
                elif key == b'M':
                    cursor_x = min(WIDTH - 1, cursor_x + 1)
            else:
                char = key.decode('utf-8').lower()
                if char == 'q':
                    break
                elif char == 'c':
                    canvas = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
                elif char == ' ':
                    canvas[cursor_y][cursor_x] = draw_char
                else:
                    draw_char = char

        os.system('cls')
        
        screen_lines = []
        for y in range(HEIGHT):
            row_str = "".join(canvas[y])
            if y == cursor_y:
                row_list = list(row_str)
                row_list[cursor_x] = draw_char
                row_str = "".join(row_list)
            screen_lines.append(row_str)
        
        print("\n".join(screen_lines))
        
        print(f"--- Controls: Arrows=Move, Space=Draw, c=Clear, q=Quit ---")
        print(f"Current Character: '{draw_char}' | Position: ({cursor_x}, {cursor_y})")
        
        time.sleep(0.05)

    print("\nThanks for drawing!")

if __name__ == "__main__":
    main()