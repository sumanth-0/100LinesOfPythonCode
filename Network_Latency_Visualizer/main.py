import time
import threading
import argparse
import sys
from ping3 import ping
import matplotlib.pyplot as plt
from collections import deque

# ----------------------------------------
# Command-line arguments
# ----------------------------------------
# Allows the user to specify a host to ping and an optional duration
parser = argparse.ArgumentParser(description="Ping a host and plot latency in real-time.")
parser.add_argument(
    "host",
    nargs="?",
    default="8.8.8.8",
    help="Host or IP to ping (default: 8.8.8.8)"
)
parser.add_argument(
    "-d", "--duration",
    type=int,
    default=0,
    help="Duration in seconds to run the pings (default: infinite)"
)
args = parser.parse_args()

# Host to ping and how long to ping (0 means infinite)
HOST = args.host
DURATION = args.duration
INTERVAL = 1       # Seconds between pings
MAX_POINTS = 100   # Maximum number of points to display on the plot

print(f"Pinging host: {HOST}")
if DURATION > 0:
    print(f"Duration: {DURATION} seconds")
else:
    print("Duration: infinite")

# ----------------------------------------
# Data buffers for storing ping results
# ----------------------------------------
# Using deque for efficient FIFO buffer with max length
latencies = deque(maxlen=MAX_POINTS)   # Store ping times in ms
timestamps = deque(maxlen=MAX_POINTS)  # Store corresponding timestamps

# ----------------------------------------
# Function to continuously ping the host
# ----------------------------------------
def ping_server():
    start_time = time.time()
    while True:
        # Stop if duration is set and exceeded
        if DURATION > 0 and time.time() - start_time >= DURATION:
            break

        # Send a ping and handle timeout
        latency = ping(HOST, timeout=2)  # Returns seconds or None if timeout
        if latency is None:
            latency = 0  # Use 0 ms for timeouts

        # Convert latency to milliseconds and store in buffers
        latencies.append(latency * 1000)
        timestamps.append(time.time())

        # Wait before sending the next ping
        time.sleep(INTERVAL)

# ----------------------------------------
# Start pinging in a background thread
# ----------------------------------------
threading.Thread(target=ping_server, daemon=True).start()

# ----------------------------------------
# Setup live matplotlib plot
# ----------------------------------------
plt.ion()  # Interactive mode on for live updates
fig, ax = plt.subplots()
line, = ax.plot([], [], 'g-', label='Latency (ms)')
ax.set_xlabel('Time')
ax.set_ylabel('Latency (ms)')
ax.set_title(f'Ping Latency to {HOST}')
ax.legend()
ax.grid(True)

# ----------------------------------------
# Live plot update loop
# ----------------------------------------
try:
    start_time = time.time()
    while True:
        if len(timestamps) > 1:
            # Update plot axes
            ax.set_xlim(timestamps[0], timestamps[-1])
            ax.set_ylim(0, max(latencies) + 50)
            
            # Update line data
            line.set_data(timestamps, latencies)
            plt.pause(0.1)  # Small pause to update plot

        # Check if duration exceeded
        if DURATION > 0 and time.time() - start_time >= DURATION:
            print("Finished duration.")
            sys.exit(0)

# ----------------------------------------
# Handle manual interruption (Ctrl+C)
# ----------------------------------------
except KeyboardInterrupt:
    print("\nPing interrupted by user.")
    sys.exit(1)
