
# Automatic Downloads Organizer

> A Python utility that automatically organizes your **Downloads** folder by moving files into categorized subfolders based on their type.

---

## Features

* Automatically detects and categorizes files by extension
* Creates folders for each category (e.g., *Images*, *Documents*, *Videos*, *Music*, etc.)
* Moves files into their respective folders
* Works across **Windows**, **macOS**, and **Linux**
* No external libraries required — uses Python’s built-in modules

---

## 🧩 Categories and File Types

| Category         | File Extensions                                                           |
| ---------------- | ------------------------------------------------------------------------- |
| **Images**       | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`                  |
| **Documents**    | `.pdf`, `.doc`, `.docx`, `.txt`, `.ppt`, `.pptx`, `.xls`, `.xlsx`, `.csv` |
| **Videos**       | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`                            |
| **Music**        | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`                           |
| **Archives**     | `.zip`, `.rar`, `.tar`, `.gz`, `.7z`                                      |
| **Applications** | `.exe`, `.msi`, `.dmg`, `.pkg`, `.app`                                    |
| **Others**       | Any unsupported or unknown file type                                      |

---

## Example

### Before:

```
photo.jpg
report.pdf
song.mp3
video.mp4
installer.exe
randomfile.xyz
```

### After running the script:

```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Music/
│   └── song.mp3
├── Videos/
│   └── video.mp4
├── Applications/
│   └── installer.exe
└── Others/
    └── randomfile.xyz
```

---

## How It Works

1. Scans your **Downloads** folder for all files.
2. Determines each file’s type based on its extension.
3. Automatically creates category folders (if missing).
4. Moves files into their appropriate folders.
5. Displays a summary of all moved files in the terminal.

---

## Usage

### 1. Clone or Download the Script

Download or copy `organize_downloads.py` to your computer.

### 2. Run the Script

Open a terminal or command prompt and run:

```bash
python organize_downloads.py
```

### 3. Output Example

```
Automatic Downloads Organizer
Target folder: /Users/Downloads

Moved: photo.jpg → Images/
Moved: resume.pdf → Documents/
Moved: song.mp3 → Music/
Moved: installer.exe → Applications/

Downloads folder organized successfully!
```

---

## Requirements

* **Python 3.6+**
* Works on **Windows**, **macOS**, and **Linux**
* Uses built-in modules: `os`, `shutil`, and `pathlib` — no installation needed

---

## Notes

* Files are **moved**, not copied — back up if necessary.
* Only organizes files directly in the **Downloads** folder (not subfolders).
* Skips already-organized files inside existing category folders.
* Make sure the script has permission to modify the Downloads folder.

---
