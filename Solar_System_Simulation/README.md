# Solar System Simulation

A simple and beautiful simulation of our solar system with colored circles representing planets orbiting around the sun.

## Features

- **8 Planets**: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune
- **Realistic Colors**: Each planet has its characteristic color
- **Orbital Motion**: Planets orbit at different speeds (relative to their actual orbital periods)
- **Orbit Paths**: Visible circular paths showing each planet's orbit
- **Labels**: Each celestial body is labeled for easy identification

## Requirements

- Python 3.x
- Pygame

## Installation

1. Install the required package:
```bash
pip install pygame
```

## Usage

Run the simulation:
```bash
python solar_system.py
```

## Controls

- **ESC** or **Close Window**: Exit the simulation

## Planet Details

| Planet   | Color      | Relative Speed |
|----------|------------|----------------|
| Mercury  | Gray       | Fastest        |
| Venus    | Orange     | Very Fast      |
| Earth    | Blue       | Fast           |
| Mars     | Red        | Medium         |
| Jupiter  | Brown      | Slow           |
| Saturn   | Gold       | Very Slow      |
| Uranus   | Cyan       | Extremely Slow |
| Neptune  | Dark Blue  | Slowest        |

## How It Works

The simulation uses Pygame to create a visual representation of the solar system. Each planet:
- Orbits in a circular path around the sun
- Has a unique color for easy identification
- Moves at a speed proportional to its actual orbital period
- Displays its name below the planet

The sun is positioned at the center of the screen, and planets orbit around it in concentric circles.

## Customization

You can modify the following parameters in the code:
- Planet colors
- Orbital distances
- Planet sizes
- Orbital speeds
- Screen dimensions

Enjoy exploring our solar system! 🌍🪐✨
