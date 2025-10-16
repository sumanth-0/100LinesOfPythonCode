# 📚 Tiny PDF Merger

A simple and command-line tool to merge multiple PDF files into one.

## ✨ Features

- **Interactive Mode**: Easy-to-use menu for selecting PDFs
- **Directory Selection**: Change directories to find PDFs anywhere on your system
- **Command-Line Mode**: Quick merging via command line
- **Smart Selection**: Select files by numbers, ranges, or "all"
- **File Preview**: Shows page count and file size before merging
- **Progress Tracking**: Real-time feedback during merge process
- **Error Handling**: Graceful handling of corrupted or invalid PDFs
- **Flexible Output**: Custom output filename support

## 🚀 Installation

Install the required dependency:

```bash
pip install pypdf
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

## 📖 Usage

### Interactive Mode

Simply run the script without arguments:

```bash
python pdf_merger.py
```

You'll see a menu like this:

```
📚 PDF Merger - Interactive Mode
============================================================

📄 Found 3 PDF file(s) in C:\Users\Documents\PDFs:
  1. document1.pdf (5 pages, 234.5 KB)
  2. document2.pdf (3 pages, 156.2 KB)
  3. document3.pdf (8 pages, 445.1 KB)

📝 Enter file numbers to merge (e.g., 1,2,3 or 1-3 or 'all'):
Selection: all

💾 Output filename (default: merged_output.pdf): combined.pdf

🔄 Merging 3 PDF file(s)...
------------------------------------------------------------
  [1/3] Adding: document1.pdf
      ✓ Added 5 page(s)
  [2/3] Adding: document2.pdf
      ✓ Added 3 page(s)
  [3/3] Adding: document3.pdf
      ✓ Added 8 page(s)

============================================================
✅ Success! Merged PDF created:
   📄 File: combined.pdf
   📊 Total pages: 16
   💾 File size: 835.8 KB
```

**If no PDFs are found:**

```
📚 PDF Merger - Interactive Mode
============================================================

❌ No PDF files found in C:\Desktop\LMU\practice\100LinesOfPythonCode
Would you like to change directory? (y/n): y
Enter directory path: C:\Users\Documents\PDFs

📄 Found 3 PDF file(s) in C:\Users\Documents\PDFs:
  1. document1.pdf (5 pages, 234.5 KB)
  2. document2.pdf (3 pages, 156.2 KB)
  3. document3.pdf (8 pages, 445.1 KB)
...
```


## 🛠️ Requirements

- Python 3.6 or higher
- pypdf library (replaces PyPDF2)



