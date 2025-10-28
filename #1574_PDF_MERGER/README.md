This project provides a simple command-line tool to **merge multiple PDF
files** from a specified folder into a single output file using Python
and `PyPDF2`.

------------------------------------------------------------------------

## Overview

The script (`pdf_merger.py`) scans a given folder, detects all valid PDF
files, and merges them in sorted order into one consolidated PDF file.

------------------------------------------------------------------------

## Folder Setup

1.  Create a folder named **`samples`** or any name you like.
2.  Place all the PDF files you want to merge inside the `samples`
    folder.
3.  Make sure all files have the `.pdf` extension and are not hidden or
    temporary.

------------------------------------------------------------------------

## Dependencies

Install required packages using pip:

``` bash
pip install PyPDF2
```

------------------------------------------------------------------------

## Note

-   Ignores temporary or hidden files (like `~$example.pdf`).
-   Overwrites existing output file if the same name is chosen.
-   Ensure PDFs are **not password-protected** before merging.

------------------------------------------------------------------------
