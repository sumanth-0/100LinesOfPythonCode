# Firefly Synchronization Simulation

import cv2 as cv
import numpy as np
import random
import time

canvas = np.zeros((800, 800, 3), dtype=np.uint8)

class particle():
  def __init__(self):
    self.reset()

  def reset(self):
    self.color = (random.randint(0, 1), random.randint(200, 255), random.randint(200, 255))
    self.x = random.randint(0, 800)
    self.y = random.randint(0, 800)
    self.radius = random.randint(0, 3)
    self.alpha = random.uniform(0.3, 1)
    self.speed_x = random.uniform(-0.5, 2)
    self.speed_y = random.uniform(-0.5, 2)

  def move(self):
    self.y += self.speed_y
    self.x += self.speed_x
    self.alpha -= 0.05
    if (self.alpha < 0 or self.x < 0 or self.y < 0):
      self.reset()

particles = [particle() for _ in range(random.randint(100, 200))]

while True:
  canvas[:] = 0

  for p in particles:
    canvas_copy = canvas.copy()
    cv.circle(canvas_copy, (int(p.x), int(p.y)), p.radius, p.color, -1)
    cv.addWeighted(canvas_copy, p.alpha, canvas, 1 - p.alpha, 0, canvas)
    p.move()

  cv.imshow("Fireflies", canvas)
  if cv.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
    break