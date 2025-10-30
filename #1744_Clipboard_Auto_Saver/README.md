# 📋 Clipboard Monitor Logger

A lightweight **Python clipboard history tracker** that monitors copied text and saves it automatically to a file (`data.txt`).  
Useful for saving snippets, research notes, or preventing accidental clipboard loss.

---

## 🚀 Features

- ✅ Monitors your clipboard in real-time  
- ✅ Logs **only new and unique** clipboard entries  
- ✅ Automatically timestamps each entry  
- ✅ Cross-platform (Windows, macOS, Linux)  
- ✅ Simple and unobtrusive — runs in the terminal  

---

## 🧠 How It Works

The script continuously checks your clipboard every few seconds (default: **2 seconds**).  
If it detects new text, it appends it to a file named **`data.txt`** with a timestamp.

---

## ⚙️ Configuration

You can modify the following constants at the top of the script:

| Variable | Default | Description |
|-----------|----------|-------------|
| `OUTPUT_FILENAME` | `"data.txt"` | File where clipboard entries are saved |
| `CHECK_INTERVAL` | `2` | Time (in seconds) between clipboard checks |

---