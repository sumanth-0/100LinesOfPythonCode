\# Floating Lights ✨



This project creates colorful, glowing particles that rise and fade, simulating fireflies or floating dust. Each run produces a dynamic, abstract animation.



\## Features



* Randomly moving particles with varied colors and sizes
* Semi-transparent glow for smooth blending
* Particles reset when they fade out or leave the canvas
* Works in Google Colab and local Python environments with OpenCV



\## Requirements



* Python 3.x
* OpenCV (opencv-python)
* NumPy
* Google Colab (optional, for automatic display)



* Install dependencies:
  pip install opencv-python numpy



\### How to Run



* Copy the code into a .py file or a Colab notebook.
* Run the script. A live animation of glowing particles will appear.



In Colab, the image updates automatically using cv2\_imshow.



\### How It Works



* A pixel canvas is created using NumPy.



* Each particle is initialized with:
  Random position, color, radius, and transparency (alpha)
  Random speed in X and Y directions



* On each frame:
  The canvas is cleared
  Particles are drawn with semi-transparency using cv.addWeighted()
  Particle positions and alpha values are updated
  Particles reset if they fade out or move off-screen



* The loop runs indefinitely, simulating a swarm of floating lights.



\### Customization



* Canvas size → Change canvas = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
* Particle count → Adjust particles = \[particle() for \_ in range(N)]
* Alpha fade speed → Modify self.alpha -= 0.05
* Particle speed range → Adjust self.speed\_x and self.speed\_y
