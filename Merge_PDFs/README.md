# PDF Merger — PyPDF2 Utility

This simple script merges multiple PDF files using [PyPDF2](https://pypi.org/project/PyPDF2/).

It can take either:
- a **folder** of PDF files (sorted by the **first digit** in each filename), or  
- a **list of specific PDF files** to merge in the given order.

---

## Features

- Merge several PDFs into one single file  
- Automatic sorting by the **first digit** in filenames (e.g. `1_intro.pdf`, `2_chapter.pdf`)  
- Works with both **folders** and **explicit file lists**  

---

## ⚙️ Installation

Make sure you have Python 3.8+ installed, then run:

```bash
pip install PyPDF2
```
or
```bash
pip install -r Merge_PDFs/requirements.txt
```

## Examples

```bash
# Merge all PDFs from the defined folder
python merge_pdfs.py /path/to/folder

# Merge PDFs from a folder and save output to a custom file
python merge_pdfs.py merged_document.pdf ./reports

# Merge specific PDFs listed manually
python merge_pdfs.py combined.pdf chapter1.pdf chapter3.pdf chapter2.pdf

```