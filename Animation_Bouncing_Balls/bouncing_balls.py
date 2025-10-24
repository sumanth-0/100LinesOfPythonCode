#!/usr/bin/env python3
"""
Simple bouncing balls animation using tkinter.

Run: python3 animations/bouncing_balls.py --count 10

Features:
- Multiple balls with random positions, velocities and colors
- Simple physics: position integration, gravity, and wall collisions with elasticity
- Small CLI to tweak count, gravity and elasticity
"""
import argparse
import random
import sys
try:
    import tkinter as tk
except Exception as e:
    print("tkinter is required to run this script. On some systems you may need to install python3-tk.")
    raise

class Ball:
    def __init__(self, canvas, x, y, vx, vy, r=15, color="#ff0000"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.color = color
        self.id = self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill=self.color, outline="")

    def update(self, dt, gravity, width, height, elasticity):
        # integrate velocity
        self.vy += gravity * dt

        # integrate position
        self.x += self.vx * dt
        self.y += self.vy * dt

        # collision with left wall
        if self.x - self.r < 0:
            self.x = self.r
            self.vx = -self.vx * elasticity

        # collision with right wall
        if self.x + self.r > width:
            self.x = width - self.r
            self.vx = -self.vx * elasticity

        # collision with top
        if self.y - self.r < 0:
            self.y = self.r
            self.vy = -self.vy * elasticity

        # collision with bottom
        if self.y + self.r > height:
            self.y = height - self.r
            self.vy = -self.vy * elasticity

        # update canvas coords
        self.canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

def mk_color():
    return "#%02x%02x%02x" % (random.randint(40, 255), random.randint(40, 255), random.randint(40, 255))

def run(count=8, width=800, height=600, gravity=400.0, elasticity=0.9):
    root = tk.Tk()
    root.title("Bouncing Balls")
    canvas = tk.Canvas(root, width=width, height=height, bg="#111111")
    canvas.pack()

    balls = []
    for _ in range(count):
        r = random.randint(8, 30)
        x = random.uniform(r, width - r)
        y = random.uniform(r, height - r)
        vx = random.uniform(-300, 300)
        vy = random.uniform(-100, 100)
        balls.append(Ball(canvas, x, y, vx, vy, r=r, color=mk_color()))
    fps = 60
    dt = 1.0 / fps
    def tick():
        for b in balls:
            b.update(dt, gravity, width, height, elasticity)
        root.after(int(1000 / fps), tick)
    tick()
    root.mainloop()

def parse_args(argv):
    p = argparse.ArgumentParser(description="Bouncing balls animation")
    p.add_argument("--count", "-n", type=int, default=8, help="Number of balls")
    p.add_argument("--width", type=int, default=800, help="Window width")
    p.add_argument("--height", type=int, default=600, help="Window height")
    p.add_argument("--gravity", type=float, default=400.0, help="Gravity (pixels/s^2)")
    p.add_argument("--elasticity", type=float, default=0.9, help="Elasticity on collisions 0..1")
    return p.parse_args(argv)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    run(count=args.count, width=args.width, height=args.height, gravity=args.gravity, elasticity=args.elasticity)