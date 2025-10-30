import os
import zipfile

def zip_folder(folder_path, output_name="archive.zip"):
    # Create a ZipFile object in write mode
    if output_name.split('.')[-1] != "zip":
        output_name+=".zip"
    
    with zipfile.ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Store relative path inside zip (preserves folder structure)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)
    print(f"✅ Folder '{folder_path}' zipped successfully as '{output_name}'")

# Example usage
if __name__ == "__main__":
    folder_to_zip = input("Enter folder path to zip: ").strip()
    zip_name = input("Enter output zip name (default: archive.zip): ").strip() or "archive.zip"
    zip_folder(folder_to_zip, zip_name)
