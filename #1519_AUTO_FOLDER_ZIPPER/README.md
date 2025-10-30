# 🗜️ Auto Folder Zipper (Python)

A simple Python script that automatically zips all files in a given folder — preserving structure and saving the `.zip` file in the **same directory** as the original folder.

---

## 🚀 Features
- Recursively zips all files and subfolders  
- Keeps folder structure intact  
- Option to specify a custom zip filename  
- Saves output zip in the same folder’s location  
- Lightweight and dependency-free  

---

## 🧩 Installation

Ensure you have Python 3 installed.  
No external dependencies are required — only built-in libraries (`os`, `zipfile`).

```bash
git clone https://github.com/yourusername/auto-folder-zipper.git
cd auto-folder-zipper
```

## 🧪 Tests Performed

| Test Case | Input | Expected Output | Result |
|------------|--------|----------------|---------|
| **1. Default behavior** | Entered folder path only (no name) | Creates `archive.zip` in same directory | ✅ Passed |
| **2. File name without extension** | Entered `backup` as name | Creates `backup.zip` in same directory | ✅ Passed |
| **3. File name with `.zip` extension** | Entered `data_archive.zip` as name | Creates `data_archive.zip` correctly | ✅ Passed |
| **4. File name with a random `.xlx` extension** | Entered `data_archive.xlx` as name | Creates `data_archive.xlx.zip` correctly | ✅ Passed |
