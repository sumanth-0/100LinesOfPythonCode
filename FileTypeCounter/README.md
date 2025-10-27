# 🧮 File Type Counter

A simple, elegant Python tool that counts how many `.png`, `.txt`, and `.pdf` files exist in a given folder — including all its subfolders.

Built with **under 100 lines of code**, this script demonstrates:
- Clean, modular design
- Practical use of Python’s `pathlib`
- A small touch of polish — dynamic pluralization for better CLI output

---

## 🚀 Features

- 🔍 Recursively scans subfolders
- 📁 Counts `.png`, `.txt`, and `.pdf` files
- 🧠 Uses dictionary comprehensions for compact, readable logic
- 🗣️ Smart pluralization (e.g., “1 file” vs “2 files”)
- ⚙️ Cross-platform (Windows, macOS, Linux)

---

## 📦 Installation

Clone the repository and navigate into it:

```bash
git clone https://github.com/yourusername/file-type-counter.git
cd file-type-counter

## 🧰 Usage

Run the script from your terminal:
```bash
python count_files.py [folder_path]

If no folder path is provided, it defaults to the current directory (.).

Example:
```bash
python count_files.py /home/user/Documents


Output:

```bash 
🔍 Scanning folder: /home/user/Documents

📊 File Type Counts:
-------------------------
• PNG: 12 files
• TXT: 4 files
• PDF: 9 files
