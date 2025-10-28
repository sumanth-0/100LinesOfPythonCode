import os

def main():
    print("Screenshot to PDF Converter")
    print("This tool combines all images from a folder into a single PDF file.")

    try:
        from PIL import Image
    except ImportError:
        print("\nError: The 'Pillow' library is not installed.")
        print("To install it, please run: pip install Pillow")
        return

    folder_path = input("\nEnter the path to the folder with your screenshots: ")

    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    all_files = os.listdir(folder_path)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not image_files:
        print(f"No image files found in '{folder_path}'.")
        return

    print(f"\nFound {len(image_files)} images. They will be added in alphabetical order.")
    for file in sorted(image_files):
        print(f"  - {file}")

    output_filename = input("\nEnter the name for the output PDF file (e.g., combined.pdf): ")

    if not output_filename:
        output_filename = "combined_screenshots.pdf(saved in directory where code is present)"
        print(f"No filename given. Using default: {output_filename}")

    if not output_filename.lower().endswith('.pdf'):
        output_filename = output_filename + '.pdf'

    print("\nProcessing images and creating PDF...")

    images_to_save = []
    try:
        for filename in sorted(image_files):
            full_path = os.path.join(folder_path, filename)
            img = Image.open(full_path)
            images_to_save.append(img)

        if images_to_save:
            images_to_save[0].save(
                output_filename,
                "PDF",
                resolution=100.0,
                save_all=True,
                append_images=images_to_save[1:]
            )
            print(f"\nSuccess! Your PDF has been saved as '{output_filename}'")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please make sure all files in the folder are valid, uncorrupted images.")

if __name__ == "__main__":
    main()