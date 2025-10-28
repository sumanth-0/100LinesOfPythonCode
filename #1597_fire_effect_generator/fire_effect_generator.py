import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fire resolution
width, height = 200, 150

# Create the figure
fig, ax = plt.subplots()
plt.axis('off')

# Initialize fire intensity array
fire = np.zeros((height, width))

# Custom colormap (black → red → orange → yellow → white)
from matplotlib.colors import LinearSegmentedColormap
colors = [(0, 0, 0), (0.6, 0, 0), (1, 0.3, 0), (1, 0.8, 0), (1, 1, 1)]
fire_cmap = LinearSegmentedColormap.from_list("fire", colors, N=256)

# Display initial frame
img = ax.imshow(fire, cmap=fire_cmap, interpolation="bilinear", vmin=0, vmax=1)

# Fire update function
def update(frame_num):
    global fire

    # Add random noise at the bottom to simulate new flames
    fire[-1, :] = np.random.random(width) * 0.9 + 0.1

    # Propagate flames upward with diffusion
    fire[:-1, :] = (fire[1:, :] +
                    np.roll(fire[1:, :], 1, axis=1) +
                    np.roll(fire[1:, :], -1, axis=1)) / 3.05

    # Slight decay for realism
    fire = np.clip(fire * 1.02 - 0.01, 0, 1)

    img.set_array(fire)
    return [img]

# Create animation
ani = animation.FuncAnimation(fig, update, interval=30, blit=True, cache_frame_data=False)

plt.show()
