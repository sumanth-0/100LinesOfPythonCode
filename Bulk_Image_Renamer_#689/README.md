
# Image Renamer Script

> A lightweight Python utility to rename all images in a folder sequentially with a custom prefix.

---

## Features

* **Automatic renaming** of all image files in a folder
* **Custom prefix support** (e.g., `photo_1.jpg`, `photo_2.png`, etc.)
* **Preserves file extensions** correctly
* **Alphabetical renaming order** for predictable results
* **No external dependencies** — just pure Python
* Works on **Windows**, **macOS**, and **Linux**

---

## Example

### Before:

```
imgA.jpg
imgB.png
imgC.jpeg
```

### After running with prefix `photo`:

```
photo_1.jpg
photo_2.png
photo_3.jpeg
```

---

## 🧠 Usage

### 1. Clone or Download the Script

Download the file **`rename_images.py`** to your computer.

### 2. Run the Script

In your terminal or command prompt, navigate to the script’s folder and run:

```bash
python rename_images.py
```

### 3. Provide Input

You’ll be prompted to enter:

1. The **folder path** containing your images
2. The **prefix** for renamed files

Example session:

```
Enter the folder path containing images: /Users/deepak/Pictures/Vacation
Enter the prefix for renamed images: beach
```

Output:

```
Renamed: imgA.jpg → beach_1.jpg
Renamed: imgB.png → beach_2.png
Renamed: imgC.jpeg → beach_3.jpeg

Renaming completed successfully!
```

---

## Supported Image Formats

| Extension | Type                        |
| --------- | --------------------------- |
| `.jpg`    | JPEG image                  |
| `.jpeg`   | JPEG image                  |
| `.png`    | Portable Network Graphic    |
| `.gif`    | Graphics Interchange Format |
| `.bmp`    | Bitmap                      |
| `.tiff`   | Tagged Image File Format    |

---

## Notes & Tips

* The script **renames files in-place**, so make a **backup** if needed.
* Files are renamed **alphabetically** (not by creation date).
* Ensure you have **write permissions** in the target directory.
* Non-image files are **ignored** safely.

---

## Requirements

* **Python 3.6+**
* No third-party libraries required — uses the built-in `os` module.

---


