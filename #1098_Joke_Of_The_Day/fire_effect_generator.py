# ...existing code...
import random
import time
import os

def fire_effect():
    chars = ['.', ':', ';', '!', '^']
    try:
        while True:
            # clear screen (Windows uses 'nt', not 'int')
            os.system('cls' if os.name == 'nt' else 'clear')
            line = "".join(random.choice(chars) for _ in range(50))
            print(line)
            time.sleep(0.1)
    except KeyboardInterrupt:
        # allow graceful exit with Ctrl+C
        pass

if __name__ == "__main__":
    fire_effect()
# ...existing code...
