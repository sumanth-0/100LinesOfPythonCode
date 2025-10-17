#  Fractal Generator: Mandelbrot Set (Python & Pillow)

A simple, dependency-based Python script to generate a small, high-contrast image of the **Mandelbrot set** and save it as a PNG file using the Pillow library.

This project is excellent for beginners interested in **fractal mathematics** and **image processing** in Python.

---

##  Features

* **Mandelbrot Algorithm:** Implements the classic $z = z^2 + c$ iterative formula.
* **Image Generation:** Uses the powerful **Pillow** (PIL Fork) library for converting raw numerical data into a standard PNG image.
* **High Contrast:** Applies a square-root scaling function for better visualization of the fine details on the edge of the set.
* **Configurable:** Easily adjust the image dimensions and the zoom area of the complex plane.

---

##  Getting Started

### Prerequisites

You need **Python 3** installed, along with the **Pillow** and **NumPy** libraries.

```bash
pip install Pillow numpy
```
```
Usage
Save the Code: Save the provided Python code as a file named fractal_generator.py.
```
Run the Script: Execute the script from your terminal:
```
Bash

python fractal_generator.py
```
```
Output

The script will generate an image file named small_mandelbrot_fractal.png in the same directory and print a success message:
```
```
✅ Success! Fractal image saved as small_mandelbrot_fractal.png with size 256x256 pixels.