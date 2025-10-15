import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import random
# Replace line plot with a polygon
from matplotlib.patches import Polygon
# Define theta
theta = np.linspace(0, 2 * np.pi, 1000)

# Define two functions
r1 = 2 * np.cos(theta)*np.sin(theta)
r2 = 2 * np.sin(theta)* np.cos(theta)
r3=2
r4=0.9
# Convert both to Cartesian
x1, y1 = r1 * np.cos(theta+np.full(1000,math.pi*0.25)), r1 *(np.full(1000,np.sin(theta+math.pi*0.25))) 
x2, y2 = r2 * np.cos(theta), r2 * np.sin(theta)
x3, y3 = r3 * np.cos(theta), r3 * np.sin(theta)
x4,y4 = r4 * np.cos(theta), r4 * np.sin(theta)

# Setup plot
fig, ax = plt.subplots()
# line1, = ax.plot([], [], color='green')
# line2, = ax.plot([], [], color='pink')
patch1 = Polygon(np.column_stack((x1, y1)), closed=True, color='green',zorder=3)
ax.add_patch(patch1)
patch2= Polygon(np.column_stack((x2, y2)), closed=True, color='pink',zorder=4)
ax.add_patch(patch2)
line1, = ax.plot([], [], color='blue')
line2, = ax.plot([], [], color='blue')
# Clean look
ax.set_aspect('equal')
ax.axis('off')
fig.set_facecolor('lightblue')
# Set axis limits considering shift
ax.set_xlim(-8, 8)
ax.set_ylim(-8, 8)

# Ping-pong shift values
shifts = np.linspace(-np.pi, np.pi, 100)
# shifts = np.concatenate((shifts, shifts[::-1]))  # back and forth

# Animation function
def update(frame):
    shift = shifts[frame % len(shifts)]
    # line1.set_data(x1 + shift, y1)  # Blue curve
    # line2.set_data(x2 + shift, y2)  # Red curve
    b_rad=5
    rnx,rny=0.08*np.random.rand(),0.08*np.random.rand()
    rnz=random.uniform(0.85,1.0)
    a1,a2=np.random.randint(0,11),np.random.randint(0,11)
    ar1,ar2 = np.radians(a1),np.radians(a2)
    x1, y1 = r1 * np.cos(theta+np.full(1000,math.pi*0.25)+np.full(1000,ar1)), r1 *(np.full(1000,np.sin(theta+math.pi*0.25+np.full(1000,ar2)))) 
    x2, y2 = r2 * np.cos(theta+np.full(1000,ar2)), r2 * np.sin(theta+np.full(1000,ar2))
    patch1.set_xy(np.column_stack((x1+b_rad*np.cos(shift)+rnx, y1+b_rad*np.sin(shift)+rny)))
    patch2.set_xy(np.column_stack((x2+b_rad*np.cos(shift)+rnx, y2+b_rad*np.sin(shift)+rny)))
    line1.set_data(rnz*x3+b_rad*np.cos(shift)+rnx, rnz*y3+b_rad*np.sin(shift)+rny)
    line2.set_data(rnz*x4+b_rad*np.cos(shift)+rnx, rnz*y4+b_rad*np.sin(shift)+rny)
    return patch1,patch2,line1,line2

# Create animation
ani = FuncAnimation(fig, update, frames=len(shifts), interval=30, blit=True)
plt.show()
