import os
from PyPDF2 import PdfMerger

def getpdf(folder_path):
    #Return a sorted list of unique,valid pdf files 
    pdf_files=[]
    seen=set()
    
    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf") and not file.startswith("~$"): #to avoid hidden
            full_path = os.path.join(folder_path, file)
            if full_path not in seen:
                pdf_files.append(full_path)
                seen.add(full_path)
    
    return sorted(pdf_files)

def merge_pdfs(pdf_files, output_path):
    if not pdf_files:
        raise ValueError("No PDF files found to merge.")
    try:
        with PdfMerger() as merger:
            for pdf in pdf_files:
                print(f"Adding: {os.path.basename(pdf)}")
                merger.append(pdf)
            merger.write(output_path)
        print(f"\nSuccessfully created merged PDF: {output_path}")
    except Exception as e:
        print(f"Error merging PDFs:{e}")

def main():
    folder_path=input("Enter folder path containing PDF files: ").strip()
    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return
    pdf_files=getpdf(folder_path)
    if not pdf_files:
        print("No pdf files found in the folder.")
        return
    print("\nFound the following pdf files to merge:")
    for i, f in enumerate(pdf_files, start=1):
        print(f"{i}.{os.path.basename(f)}")
    output_name=input("\nEnter name for merged PDF: ").strip()
    output_path=os.path.join(folder_path, output_name + ".pdf")
    if os.path.exists(output_path):
        try:
            os.remove(output_path)
        except Exception as e:
            print(f"Cannot remove existing output PDF: {e}")
            return
    merge_pdfs(pdf_files, output_path)
if __name__ == "__main__":
    main()