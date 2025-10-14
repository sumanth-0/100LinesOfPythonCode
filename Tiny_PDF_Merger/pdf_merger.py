# Tiny PDF Merger - Merge multiple PDF files into one
import os
import sys
from pypdf import PdfWriter, PdfReader

def list_pdf_files(directory="."):
    return sorted([f for f in os.listdir(directory) if f.lower().endswith('.pdf')])

def merge_pdfs_interactive():
    print("\n📚 PDF Merger - Interactive Mode\n" + "=" * 60)
    directory = "."
    while True:
        pdf_files = list_pdf_files(directory)
        if not pdf_files:
            print(f"❌ No PDF files found in {os.path.abspath(directory)}")
            change = input("Would you like to change directory? (y/n): ").strip().lower()
            if change == 'y':
                new_dir = input("Enter directory path: ").strip()
                if os.path.isdir(new_dir):
                    directory = new_dir
                    continue
                else:
                    print("❌ Invalid directory.")
            return
        break
    print(f"\n📄 Found {len(pdf_files)} PDF file(s) in {os.path.abspath(directory)}:")
    for idx, file in enumerate(pdf_files, 1):
        try:
            filepath = os.path.join(directory, file)
            reader = PdfReader(filepath)
            pages, size = len(reader.pages), os.path.getsize(filepath) / 1024
            print(f"  {idx}. {file} ({pages} pages, {size:.1f} KB)")
        except:
            print(f"  {idx}. {file} (Error reading)")
    print("\n📝 Enter file numbers to merge (e.g., 1,2,3 or 1-3 or 'all'):")
    selection = input("Selection: ").strip().lower()
    if selection == 'all':
        selected_files = [os.path.join(directory, f) for f in pdf_files]
    elif '-' in selection and selection.replace('-', '').isdigit():
        start, end = map(int, selection.split('-'))
        selected_files = [os.path.join(directory, f) for f in pdf_files[start-1:end]]
    else:
        indices = [int(x.strip()) - 1 for x in selection.split(',') if x.strip().isdigit()]
        selected_files = [os.path.join(directory, pdf_files[i]) for i in indices if 0 <= i < len(pdf_files)]
    if not selected_files:
        print("❌ No valid files selected.")
        return
    default_output = "merged_output.pdf"
    output_file = input(f"\n💾 Output filename (default: {default_output}): ").strip() or default_output
    if not output_file.lower().endswith('.pdf'):
        output_file += '.pdf'
    merge_pdfs(selected_files, output_file)

def merge_pdfs(input_files, output_file):
    print(f"\n🔄 Merging {len(input_files)} PDF file(s)...\n" + "-" * 60)
    merger = PdfWriter()
    total_pages = 0
    for idx, pdf_file in enumerate(input_files, 1):
        try:
            print(f"  [{idx}/{len(input_files)}] Adding: {pdf_file}")
            reader = PdfReader(pdf_file)
            pages = len(reader.pages)
            for page in reader.pages:
                merger.add_page(page)
            total_pages += pages
            print(f"      ✓ Added {pages} page(s)")
        except Exception as e:
            print(f"      ✗ Error: {str(e)}")
    try:
        with open(output_file, 'wb') as f:
            merger.write(f)
        size = os.path.getsize(output_file) / 1024
        print("\n" + "=" * 60)
        print(f"✅ Success! Merged PDF created:\n   📄 File: {output_file}")
        print(f"   📊 Total pages: {total_pages}\n   💾 File size: {size:.1f} KB")
    except Exception as e:
        print(f"\n❌ Error writing output file: {str(e)}")

def main():
    print("\n🔀 Tiny PDF Merger\n" + "=" * 60)
    if len(sys.argv) > 1:
        input_files = [f for f in sys.argv[1:] if f.lower().endswith('.pdf')]
        if not input_files:
            print("❌ No valid PDF files provided.\n\nUsage:")
            print("  Interactive: python pdf_merger.py")
            print("  CLI: python pdf_merger.py file1.pdf file2.pdf [output.pdf]")
            return
        if len(input_files) > 1 and not os.path.exists(input_files[-1]):
            output_file = input_files[-1]
            input_files = input_files[:-1]
        else:
            output_file = "merged_output.pdf"
        merge_pdfs(input_files, output_file)
    else:
        merge_pdfs_interactive()

if __name__ == "__main__":
    main()

