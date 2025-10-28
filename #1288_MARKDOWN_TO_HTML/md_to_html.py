import markdown
import sys
import os

def convert_markdown_to_html(input_file, output_file=None, title=None):
    """
    Convert a Markdown file to a simple HTML page.
    
    Args:
        input_file: Path to the input Markdown file
        output_file: Path to the output HTML file (optional)
        title: Title for the HTML page (optional)
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    html_body = markdown.markdown(md_content, extensions=['extra', 'codehilite'])
    
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.html'
    
    if title is None:
        title = os.path.splitext(os.path.basename(input_file))[0]
    
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }}
        h1 {{
            font-size: 2em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }}
        h2 {{
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
        }}
        code {{
            background-color: #f6f8fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 85%;
        }}
        pre {{
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}
        blockquote {{
            border-left: 4px solid #dfe2e5;
            padding-left: 16px;
            color: #6a737d;
            margin-left: 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
        }}
        th, td {{
            border: 1px solid #dfe2e5;
            padding: 8px 12px;
        }}
        th {{
            background-color: #f6f8fa;
            font-weight: 600;
        }}
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
    </style>
</head>
<body>
{html_body}
</body>
</html>"""
    
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_template)
        print(f"Successfully converted '{input_file}' to '{output_file}'")
    except Exception as e:
        print(f"Error writing output file: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python md_to_html.py <input.md> [output.html] [title]")
        print("Example: python md_to_html.py README.md index.html 'My Page'")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    title = sys.argv[3] if len(sys.argv) > 3 else None
    
    convert_markdown_to_html(input_file, output_file, title)

if __name__ == "__main__":
    main()