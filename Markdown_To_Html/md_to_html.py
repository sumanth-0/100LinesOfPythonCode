import sys
import os
from markdown import markdown  # optional but recommended

def convert_md_to_html(input_path, output_path=None):
    # Read the markdown file
    with open(input_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert markdown to HTML
    html_content = markdown(md_content)

    # Output path handling
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".html"

    # Write the HTML to a new file
    with open(output_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print(f"Conversion complete! HTML saved to {output_path}")

def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python md_to_html.py <input_markdown_file> [output_html_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    # Run the conversion
    convert_md_to_html(input_file, output_file)

if __name__ == "__main__":
    main()
