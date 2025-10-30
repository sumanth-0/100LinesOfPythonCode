import time
from pynput import keyboard
from collections import deque

# --- Configuration ---
# Calculate KPM based on key presses in the last 10 seconds
TIME_WINDOW_SECONDS = 10 

# --- Global variable to store timestamps ---
# We use a deque because it's thread-safe for appends/pops
# and very fast for removing old items.
key_timestamps = deque()

def on_press(key):
    """
    This function is called by the listener every time a key is pressed.
    It runs in a separate thread.
    """
    # Append the current time to our list
    key_timestamps.append(time.time())

def main():
    """
    Main loop to calculate and display KPM.
    """
    print("--- Live Keystrokes Per Minute (KPM) Tracker ---")
    print(f"Calculating KPM based on a {TIME_WINDOW_SECONDS}-second rolling window.")
    print("Start typing to see your speed. Press Ctrl+C to stop.")

    # Start the keyboard listener in a non-blocking background thread
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
        while True:
            # --- Calculate KPM ---
            
            # 1. Get the current time
            now = time.time()
            
            # 2. Define the cutoff time
            cutoff_time = now - TIME_WINDOW_SECONDS
            
            # 3. Clean the deque: remove all timestamps older than the cutoff
            #    This is fast because we only check from the left.
            while key_timestamps and key_timestamps[0] < cutoff_time:
                key_timestamps.popleft()
                
            # 4. Count the remaining keys (all within the time window)
            keys_in_window = len(key_timestamps)
            
            # 5. Calculate KPM (extrapolate from our window)
            # (Keys / Seconds) * 60 = Keys per Minute
            if keys_in_window > 0:
                kpm = (keys_in_window / TIME_WINDOW_SECONDS) * 60
            else:
                kpm = 0
            
            # --- Display the result ---
            # '\r' moves the cursor to the start of the line.
            # 'end=""' prevents it from printing a new line.
            # We add spaces at the end to clear any previous, longer text.
            print(f"\rKPM: {kpm:5.0f}   ", end="")
            
            # Wait a short time before recalculating
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        # User pressed Ctrl+C
        print("\nStopping listener...")
        listener.stop()
        print("Exiting.")

if __name__ == "__main__":
    main()