# Interactive 2D Ray Reflection Simulator

This Python program provides an **interactive 2D ray reflection simulator** using `matplotlib` and `numpy`. Users can place mirrors and shoot rays to visualize reflections in real time.

## Features

- **Interactive Mirror Placement:** Click two points to define a mirror segment.
- **Ray Shooting:** Click to define the start and direction of a ray.
- **Real-Time Reflection:** Rays reflect off mirrors using accurate vector mathematics.
- **Multiple Reflections:** Each ray can bounce up to 10 times across multiple mirrors.
- **Clear & Reset:** Easily clear all mirrors and rays to start a new simulation.
- **Simple Controls:** Switch between mirror placement and ray shooting modes via keyboard.

## Controls

- `m` — Switch to **Mirror Mode** (click two points to place a mirror)  
- `l` — Switch to **Ray Mode** (click two points to define a ray direction)  
- `c` — **Clear** all mirrors and rays from the canvas  

## How It Works

1. **Mirror Representation:** Each mirror is a line segment defined by two points.  
2. **Ray Propagation:** Rays are represented by a starting point and direction vector.  
3. **Reflection Calculation:** When a ray hits a mirror, its direction is reflected according to the mirror's normal vector.  
4. **Intersection Detection:** The simulation computes ray-segment intersections to determine the next reflection point.  
5. **Visualization:** `matplotlib` plots the mirrors in black, rays in red, and ray origins in blue.

## Requirements

- Python 3.6 or higher  
- `matplotlib` (`pip install matplotlib`)  
- `numpy` (`pip install numpy`)  

## Use Cases

- Educational tool for learning **geometrical optics** and **reflection laws**  
- Interactive demonstrations of ray tracing and mirror interactions  
- Simple visual experiments in **2D physics simulations**  

This project is lightweight and designed for experimentation and learning. Simply run the script to start placing mirrors and shooting rays in an interactive plotting window.
