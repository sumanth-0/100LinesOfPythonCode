import time
import os

# ASCII digits for 0-9 and colon
ASCII_DIGITS = {
    "0": [" 000 ", "0   0", "0   0", "0   0", " 000 "],
    "1": ["  1  ", " 11  ", "  1  ", "  1  ", "11111"],
    "2": [" 222 ", "2   2", "   2 ", "  2  ", "22222"],
    "3": [" 333 ", "    3", "  33 ", "    3", " 333 "],
    "4": ["   4 ", "  44 ", " 4 4 ", "44444", "   4 "],
    "5": ["55555", "5    ", "5555 ", "    5", "5555 "],
    "6": [" 666 ", "6    ", "6666 ", "6   6", " 666 "],
    "7": ["77777", "    7", "   7 ", "  7  ", " 7   "],
    "8": [" 888 ", "8   8", " 888 ", "8   8", " 888 "],
    "9": [" 999 ", "9   9", " 9999", "    9", " 999 "],
    ":": ["     ", "  :  ", "     ", "  :  ", "     "]
}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display_time():
    try:
        while True:
            now = time.strftime("%H:%M:%S")
            lines = [""] * 5
            frame_width = len(now) * 7 + 4
            print("╔" + "═" * frame_width + "╗")
            for ch in now:
                for i in range(5):
                    lines[i] += ASCII_DIGITS[ch][i] + "  "
            for line in lines:
                print("║ " + line + "║")
            print("╚" + "═" * frame_width + "╝")
            time.sleep(1)
            clear()
    except KeyboardInterrupt:
        clear()
        print("Clock stopped. Have a nice day! ⏰")

if __name__ == "__main__":
    display_time()
