
# 🎨 Gradient Image Generator

This project provides two simple Python scripts to **generate colorful gradient images** either **linear** or **radial** using **NumPy** and **Pillow (PIL)**.

---

## 🧩 Features

* ✅ Generate **linear gradients** (vertical or horizontal)
* ✅ Generate **radial gradients** (with adjustable radius)
* ✅ Fully **interactive**: you can enter parameters like orientation or radius
* ✅ Automatically saves generated images to an `images/` folder next to the script

---

## 🖥️ Requirements

Make sure you have Python 3.8+ installed.
Then, install dependencies:

```bash
pip install numpy pillow
```

---

## 🧱 Project Structure

```
gradient_generator/
│
├── generate_linear_gradient.py
├── generate_radial_gradient.py
└── images/
    ├── linear_gradient.png
    └── radial_gradient.png
```

---

## 🌈 Linear Gradient

The **linear gradient script** creates an image that transitions smoothly from a start color to an end color, either **vertically** or **horizontally**.

### ▶️ Run

```bash
python generate_linear_gradient.py
```

### 🧭 Example Interaction

```
Enter the orientation of the gradient (horizontal/vertical) :  horizontal
```

The generated image will be saved as:

```
/images/linear_gradient.png
```

### ⚙️ Default Settings

* Image size: `500 x 300`
* Start color: **Red** `(255, 0, 0)`
* End color: **Blue** `(0, 0, 255)`
* Default orientation: **Vertical**

---

## ☀️ Radial Gradient

The **radial gradient script** generates a gradient that spreads outward from the center of the image, fading from a start color to an end color.
You can control how fast the gradient spreads using the **radius**.

### ▶️ Run

```bash
python generate_radial_gradient.py
```

### 🧭 Example Interaction

```
Please enter the radius for the radial gradient(0-1) : 0.5
```

The generated image will be saved as:

```
/images/radial_gradient.png
```

### ⚙️ Default Settings

* Image size: `500 x 500`
* Start color: **Yellow** `(255, 255, 0)`
* End color: **Black** `(0, 0, 0)`
* Default radius: **250**

---

## 💾 Output

Both scripts create an `images/` folder automatically if it doesn’t exist and store the generated images inside.

---

## 🧠 Notes

* You can freely modify the **width**, **height**, **colors**, and **radius** in each script.
* Perfect for generating backgrounds, art assets, or UI design placeholders.

---

## 📜 License

MIT License © 2025 — Created for educational and creative purposes.

---


