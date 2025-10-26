import random
import time
import os

def terminal_rain():
    """Creates a falling rain effect in the terminal."""
    
    # Get terminal dimensions
    try:
        width, height = os.get_terminal_size()
    except OSError:
        width, height = 80, 24  # Default values if size can't be fetched

    # A list to store all our drops. Each drop is a dictionary.
    drops = []

    # Characters to use for rain
    rain_chars = ['|', '¦', '.', "'", ':', ',']

    try:
        while True:
            # 1. ADD NEW DROPS
            # Add a 30% chance of a new drop appearing at the top
            if random.random() < 0.3:
                # Add a small cluster of new drops
                for _ in range(random.randint(1, 3)):
                    new_drop = {
                        'x': random.randint(0, width - 1),
                        'y': 0,
                        'char': random.choice(rain_chars)
                    }
                    drops.append(new_drop)

            # 2. CLEAR SCREEN & CREATE BUFFER
            # Clear the terminal screen (cross-platform)
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Create a 2D list (buffer) filled with spaces
            screen = [[' ' for _ in range(width)] for _ in range(height)]

            # 3. UPDATE & DRAW DROPS
            # We create a new list for drops that are still on-screen
            remaining_drops = []
            
            for drop in drops:
                # Place the drop character in our screen buffer
                # Check bounds to prevent errors
                if 0 <= drop['y'] < height and 0 <= drop['x'] < width:
                    screen[drop['y']][drop['x']] = drop['char']
                
                # Move the drop down for the next frame
                drop['y'] += 1
                
                # If the drop is still on screen, add it to the 'remaining' list
                if drop['y'] < height:
                    remaining_drops.append(drop)
            
            # Update our main drops list
            drops = remaining_drops

            # 4. PRINT BUFFER
            # Join all characters in each row, then join all rows with newlines
            print('\n'.join([''.join(row) for row in screen]))

            # 5. PAUSE
            # Control the speed of the animation
            time.sleep(0.09)

    except KeyboardInterrupt:
        # Clean up the terminal 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Rain stopped. ☔")

if __name__ == "__main__":
    terminal_rain()