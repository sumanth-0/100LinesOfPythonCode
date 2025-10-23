# 🐶 Random Dog Image Viewer

A simple Python script that fetches and displays a **random dog image** from the public API [random.dog](https://random.dog).
The API occasionally returns `.mp4` video files, which this script automatically filters out to display only valid image formats.

---

## 📋 Features

* Fetches random dog images from the internet.
* Automatically avoids non-image (e.g., `.mp4`) responses.
* Opens the image directly in your system’s default image viewer.

---

## 🧠 How It Works

1. Requests a random file URL from `https://random.dog/woof.json`.
2. If the returned file ends with `.mp4`, it retries until an image URL is received.
3. Downloads the image bytes and displays it using **Pillow (PIL)**.

---

## 🧩 Requirements

Install dependencies using pip:

```bash
pip install requests pillow
```

---

## ▶️ Usage

Run the script:

```bash
python random_dog_images.py
```


## 💡 Notes

* The `random.dog` API is free and open; no authentication is required.


