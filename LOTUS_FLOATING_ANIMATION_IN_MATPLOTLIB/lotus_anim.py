import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon
import math, random

# --- Setup polar angle and radial functions ---
theta = np.linspace(0, 2 * np.pi, 1000)

# Base petal forms (two mirrored lobes)
r1 = 2 * np.cos(theta) * np.sin(theta)
r2 = 2 * np.sin(theta) * np.cos(theta)

# Outer & inner ripple radii
r3, r4 = 2, 0.9

# Convert polar forms to Cartesian (initial positions)
x1, y1 = r1 * np.cos(theta + math.pi/4), r1 * np.sin(theta + math.pi/4)
x2, y2 = r2 * np.cos(theta), r2 * np.sin(theta)
x3, y3 = r3 * np.cos(theta), r3 * np.sin(theta)
x4, y4 = r4 * np.cos(theta), r4 * np.sin(theta)

# --- Plot initialization ---
fig, ax = plt.subplots()
fig.set_facecolor('lightblue')
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)

# Lotus petals (center polygons)
patch1 = Polygon(np.column_stack((x1, y1)), closed=True, color='green', zorder=3)
patch2 = Polygon(np.column_stack((x2, y2)), closed=True, color='pink', zorder=4)
ax.add_patch(patch1)
ax.add_patch(patch2)

# Blue ripple outlines
line1, = ax.plot([], [], color='blue')
line2, = ax.plot([], [], color='blue')

# --- Frame control for rotation and ripple ---
shifts = np.linspace(-np.pi, np.pi, 100)

# --- Animation update function ---
def update(frm):
    # Circular rotation offset
    sh = shifts[frm % len(shifts)]
    b_rad = 5  # orbit radius of lotus center

    # Small vibration in x, y, and ripple scaling
    rnx, rny = 0.08*np.random.rand(), 0.08*np.random.rand()
    rnz = random.uniform(0.85, 1.0)

    # Slight random angular offset for petals
    a1, a2 = np.radians(np.random.randint(0, 11)), np.radians(np.random.randint(0, 11))

    # Rotated lotus petals
    x1n = r1 * np.cos(theta + math.pi/4 + a1)
    y1n = r1 * np.sin(theta + math.pi/4 + a2)
    x2n = r2 * np.cos(theta + a2)
    y2n = r2 * np.sin(theta + a2)

    # Update petal positions (rotating + vibrating)
    patch1.set_xy(np.column_stack((x1n + b_rad*np.cos(sh) + rnx,
                                   y1n + b_rad*np.sin(sh) + rny)))
    patch2.set_xy(np.column_stack((x2n + b_rad*np.cos(sh) + rnx,
                                   y2n + b_rad*np.sin(sh) + rny)))

    # Update ripple circles (expanding/contracting)
    line1.set_data(rnz*x3 + b_rad*np.cos(sh) + rnx,
                   rnz*y3 + b_rad*np.sin(sh) + rny)
    line2.set_data(rnz*x4 + b_rad*np.cos(sh) + rnx,
                   rnz*y4 + b_rad*np.sin(sh) + rny)

    return patch1, patch2, line1, line2

# --- Create and display animation ---
ani = FuncAnimation(fig, update, frames=len(shifts), interval=30, blit=True)
plt.show()
