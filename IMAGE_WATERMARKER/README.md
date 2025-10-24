# Simple Image Watermarker
A Python GUI tool that lets you add a centered, semi-transparent text watermark to an image using **Tkinter** and **Pillow**.

## Features
- Add custom text watermark to an image.
- Choose watermark color (Black or White).
- Automatically centers the watermark.
- Semi-transparent (50%) text.
- Saves and previews the watermarked image instantly.

## Usage
1. Run `main.py`.
2. Click **Select** to choose an image (`.jpg`, `.jpeg`, or `.png`).
3. Enter the watermark text.
4. Choose watermark color (Black/White).
5. Click **Insert Watermark** to generate the image.
6. The new image (`watermarked_image.jpg`) is saved in the same folder and automatically opened.

## Requirements
This project requires the **Pillow** library. Install it using pip:

```bash
pip install pillow
```

## Example

Original Image:  
![Original](images/image.jpg)

Watermarked Image:  
![Watermarked](images/watermarked_image.jpg)
