# Bulk PDF Splitter

## Description
A Python CLI tool to split multiple PDF files into individual pages in bulk. Perfect for processing large batches of multi-page PDFs quickly and efficiently.

## Features
- 📄 Split multiple PDFs at once from a directory
- 🔢 Zero-padded page numbers for proper sorting
- 📁 Custom output directory support
- 📊 Progress tracking with detailed summary
- ⚡ Fast batch processing
- 🛡️ Error handling for corrupted files

## Requirements
- Python 3.6+
- PyPDF2

## Installation

1. Clone this repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/#1007_Bulk_PDF_Splitter
```

2. Install dependencies:
```bash
pip install PyPDF2
```

## Usage

Basic usage (output goes to `input_folder/split_pdfs`):
```bash
python bulk_pdf_splitter.py <input_folder>
```

With custom output directory:
```bash
python bulk_pdf_splitter.py <input_folder> <output_folder>
```

### Examples

Split all PDFs in the `./documents` folder:
```bash
python bulk_pdf_splitter.py ./documents
```

Split PDFs and save to custom location:
```bash
python bulk_pdf_splitter.py ./documents ./output/split_pages
```

## Output Format
Pages are saved with the format: `{original_filename}_page_{page_number}.pdf`

Example:
- Input: `report.pdf` (5 pages)
- Output:
  - `report_page_001.pdf`
  - `report_page_002.pdf`
  - `report_page_003.pdf`
  - `report_page_004.pdf`
  - `report_page_005.pdf`

## Sample Output
```
Output directory: ./documents/split_pdfs
Found 3 PDF file(s) to process

Processing: report.pdf (5 pages)
  Created: report_page_001.pdf
  Created: report_page_002.pdf
  Created: report_page_003.pdf
  Created: report_page_004.pdf
  Created: report_page_005.pdf

Processing: presentation.pdf (10 pages)
  Created: presentation_page_001.pdf
  Created: presentation_page_002.pdf
  ...

==================================================
Summary: Processed 3/3 files
Total pages extracted: 25
Output saved to: ./documents/split_pdfs
```

## Error Handling
The tool includes error handling for:
- Invalid directory paths
- Corrupted PDF files
- Permission errors
- Missing dependencies

## License
This project is part of the 100 Lines of Python Code repository.

## Contributing
Contributions are welcome! Please check the [contributing guidelines](https://github.com/sumanth-0/100LinesOfPythonCode/blob/main/CONTRIBUTING.md).

## Related Issue
This tool was created to address [Issue #1007](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1007).
