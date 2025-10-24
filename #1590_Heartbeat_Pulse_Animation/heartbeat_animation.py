import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.axis('off')

# Parametric equations for a heart shape
t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

# Create a line object for the heart
heart, = ax.plot([], [], color='red', lw=2)

# Set the plot limits
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

# Animation function to update the plot
def update(frame):
    """Updates the plot for each frame of the animation."""
    # Use a sine function to create a pulsing effect
    scale = 1 + 0.2 * np.sin(frame * 0.1)
    heart.set_data(x * scale, y * scale)
    return heart,

# Create the animation
# The FuncAnimation function creates the animation
# The update function is called for each frame
# The frames argument specifies the number of frames in the animation
# The interval argument specifies the delay between frames in milliseconds
# The blit argument tells the animation to only redraw the parts of the plot that have changed
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the plot
plt.show()
