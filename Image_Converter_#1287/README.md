
# Image Format Converter (PNG ⇆ JPEG)

A simple yet powerful **Python script** that converts all **PNG files to JPEG** or **JPEG files to PNG** in a specified folder using the [Pillow](https://pypi.org/project/Pillow/) library.

---

## Features

- Converts all images in a folder between **PNG** and **JPEG** formats  
- Automatically skips invalid image files  
- Saves converted images in a `converted/` subfolder (originals remain safe)  
- Simple CLI-based input for folder path and target format  
- Clear console messages for every step  

---

## How It Works

1. The program scans the specified folder for image files (`.png`, `.jpg`, `.jpeg`).
2. Based on the user’s chosen output format:
   - Converts all **PNG → JPEG**, or  
   - Converts all **JPEG → PNG**.
3. Converted images are saved into a new `converted/` subfolder.

---

## Requirements

Make sure you have **Python 3.7+** installed, then install the Pillow library:

```bash
pip install pillow
````

---

## ▶️ Usage

Run the script using:

```bash
python convert_images.py
```

When prompted:

* Enter the folder path where your images are stored
* Enter the desired target format (`jpeg` or `png`)

**Example:**

```
Enter the folder path containing images: ./photos
Enter target format ('jpeg' or 'png'): jpeg
Converted: sample1.png → sample1.jpeg
Converted: flower.png → flower.jpeg
Conversion complete! 2 files saved to './photos/converted'
```

---

## Example Folder Structure

```
photos/
 ├── flower.png
 ├── sky.png
 └── convert_images.py
```

After conversion:

```
photos/
 ├── flower.png
 ├── sky.png
 ├── convert_images.py
 └── converted/
      ├── flower.jpeg
      └── sky.jpeg
```

---

## Notes

* The script does **not overwrite** original images.
* Only `.png`, `.jpg`, and `.jpeg` formats are supported.
* Large image folders may take longer to process.

---
```
