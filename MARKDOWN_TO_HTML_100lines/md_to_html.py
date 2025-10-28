import re
import sys

sys.argv = ["md_to_html.py", "input.md", "output.html"]

def markdown_to_html(md):
    """Convert Markdown text to HTML."""
    html = md
    for i in range(6, 0, -1):
        html = re.sub(f"^{'#' * i}\s+(.+)$", f'<h{i}>\\1</h{i}>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.+?)\*\*|__(.+?)__', r'<strong>\1\2</strong>', html)
    html = re.sub(r'\*(.+?)\*|_(.+?)_', r'<em>\1\2</em>', html)
    html = re.sub(r'~~(.+?)~~', r'<del>\1</del>', html)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', html)
    html = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)', r'<img src="\2" alt="\1">', html)
    html = re.sub(r'```([^`]+)```', r'<pre><code>\1</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'^(---|\\*\\*\\*)$', r'<hr>', html, flags=re.MULTILINE)
    lines = html.split('\n')
    result = []
    in_blockquote = in_ul = in_ol = False
    for line in lines:
        if line.startswith('> '):
            if not in_blockquote:
                result.append('<blockquote>')
                in_blockquote = True
            result.append(line[2:])
            continue
        elif in_blockquote:
            result.append('</blockquote>')
            in_blockquote = False
        ul_match = re.match(r'^[\*\-\+]\s+(.+)$', line)
        if ul_match:
            if not in_ul:
                result.append('<ul>')
                in_ul = True
            result.append(f'<li>{ul_match.group(1)}</li>')
            continue
        elif in_ul:
            result.append('</ul>')
            in_ul = False
        ol_match = re.match(r'^\d+\.\s+(.+)$', line)
        if ol_match:
            if not in_ol:
                result.append('<ol>')
                in_ol = True
            result.append(f'<li>{ol_match.group(1)}</li>')
            continue
        elif in_ol:
            result.append('</ol>')
            in_ol = False
        if line.strip() and not re.match(r'^\s*<', line):
            result.append(f'<p>{line}</p>')
        else:
            result.append(line)
    if in_blockquote:
        result.append('</blockquote>')
    if in_ul:
        result.append('</ul>')
    if in_ol:
        result.append('</ol>')
    return '\n'.join(result)
def convert_file(input_file, output_file=None):
    """Convert a Markdown file to HTML."""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        
        html_content = markdown_to_html(markdown_text)
        full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted from Markdown</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; padding: 0 20px; color: #333; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
        blockquote {{ border-left: 4px solid #ddd; margin: 0; padding-left: 20px; color: #666; }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_html)
            print(f"Converted {input_file} to {output_file}")
        else:
            print(full_html)
        return full_html
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markdown_converter.py <input.md> [output.html]")
        sys.exit(1)
    convert_file("MARKDOWN_TO_HTML_100lines/input.md", "MARKDOWN_TO_HTML_100lines/output.html" if len(sys.argv) > 2 else None)