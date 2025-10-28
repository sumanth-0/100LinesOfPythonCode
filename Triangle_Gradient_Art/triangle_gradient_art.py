# Triangle Gradient Art

import cv2 as cv
from google.colab.patches import cv2_imshow   # for colab
import numpy as np
import random

canvas = np.zeros((800, 800, 3), dtype=np.uint8)

def draw_trangle(canvas, pts, color, alpha=0.1):
  copy_canvas = canvas.copy()
  pts = np.array([pts], dtype=np.int32)
  cv.fillPoly(canvas, pts, color)
  cv.addWeighted(copy_canvas, alpha, canvas, 1 - alpha, 0, canvas)

for _ in range(random.randint(100, 200)) :
  pts = [(random.randint(0, 800), random.randint(0, 800)), (random.randint(0, 800), random.randint(0, 800)), (random.randint(0, 800), random.randint(0, 800))]
  color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  alpha = random.uniform(0.2, 0.8)
  
  draw_trangle(canvas, pts, color, alpha)

cv2_imshow(canvas)   # for colab
cv.waitKey(0)
cv.destroyAllWindows()