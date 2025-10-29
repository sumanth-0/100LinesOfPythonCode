import math, random, os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.lines import Line2D

# Lightning generation parameters
MAX_DEPTH = 6           # maximum recursion depth for branching
BRANCH_ANGLE = math.pi/4  # max deviation for child branches (radians)
BASE_LENGTH = 0.25       # base length of segments (as fraction of figure)
BRANCH_PROB = 0.35       # probability a segment branches
SEGMENTS_SCALE = 1.0     # scale multiplier for segment lengths

random.seed(42)
np.random.seed(42)

def generate_lightning(start=(0.5, 1.0), angle=-math.pi/2, depth=0, length=0.12):
    """
    Recursively generate a list of line segments representing lightning.
    Each segment is ((x1,y1), (x2,y2))
    """
    segments = []
    if depth > MAX_DEPTH:
        return segments

    # compute end point with some random length multiplier and angular jitter
    length = length * (0.7 + 0.6*random.random()) * SEGMENTS_SCALE
    angle_jitter = (random.random() - 0.5) * BRANCH_ANGLE * 0.6
    actual_angle = angle + angle_jitter
    dx = math.cos(actual_angle) * length
    dy = math.sin(actual_angle) * length
    x1, y1 = start
    x2, y2 = x1 + dx, y1 + dy

    segments.append(((x1, y1), (x2, y2)))

    # Continue the main branch downward
    if random.random() < 0.9:
        segments += generate_lightning((x2, y2), actual_angle, depth+1, length*0.95)

    # Possibly create a branching arm
    if depth < MAX_DEPTH and random.random() < BRANCH_PROB:
        branch_angle = actual_angle + (random.random() - 0.5) * BRANCH_ANGLE * 1.6
        segments += generate_lightning((x2, y2), branch_angle, depth+1, length*0.75)

    # Occasionally add a short side twig
    if depth < MAX_DEPTH and random.random() < 0.25:
        twig_angle = actual_angle + (random.random() - 0.5) * BRANCH_ANGLE * 2.2
        midx = x1 + (x2-x1)*0.5
        midy = y1 + (y2-y1)*0.5
        segments += generate_lightning((midx, midy), twig_angle, depth+1, length*0.5)
    return segments

# Generate and pick one lightning bolt
bolts = [generate_lightning() for _ in range(6)]
bolt = max(bolts, key=len)

# Convert to arrays for animation
lines = [np.array([[x1, y1], [x2, y2]]) for ((x1, y1), (x2, y2)) in bolt]

# Plot setup
fig, ax = plt.subplots(figsize=(5, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor("black")  # dark background
ax.set_title("⚡ Lightning Strike Animation ⚡", color="white")
ax.set_frame_on(False)

# Add lightning lines
artists = []
for seg in lines:
    ln = Line2D(seg[:, 0], seg[:, 1], linewidth=2.5, color="cyan", alpha=1.0)
    ax.add_line(ln)
    artists.append(ln)

# Animation
TOTAL_FRAMES = 40

def update(frame):
    reveal_fraction = min(1.0, (frame+1) / (TOTAL_FRAMES * 0.5))
    num_revealed = int(reveal_fraction * len(artists))
    for i, ln in enumerate(artists):
        if i < num_revealed:
            jitter = (np.random.rand(2, 2) - 0.5) * 0.007 * (1.0 - frame/TOTAL_FRAMES)
            x = ln.get_xdata() + jitter[:, 0]
            y = ln.get_ydata() + jitter[:, 1]
            ln.set_data(x, y)
            base_alpha = 0.9
            flicker = 0.2 * (np.random.rand() - 0.5)
            ln.set_alpha(max(0.0, min(1.0, base_alpha + flicker - 0.4*(frame/TOTAL_FRAMES))))
        else:
            ln.set_alpha(0.0)
    return artists

anim = FuncAnimation(fig, update, frames=TOTAL_FRAMES, blit=False, interval=40)

# Save as GIF
gif_path = "lightning.gif"
anim.save(gif_path, writer=PillowWriter(fps=20))
print(f"Animation saved as {gif_path}")

plt.show()
