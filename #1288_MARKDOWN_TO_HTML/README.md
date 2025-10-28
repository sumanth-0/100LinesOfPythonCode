# Markdown to HTML Converter

A Python utility that converts Markdown files into beautifully styled HTML pages. Perfect for generating documentation, README displays, blog posts, and more.

## Features

- 📝 Convert Markdown to clean, responsive HTML
- 🎨 GitHub-inspired styling out of the box
- 🔧 Support for extended Markdown features (tables, code blocks, footnotes)
- 💻 Syntax highlighting for code blocks
- 📱 Mobile-responsive design
- ⚡ Simple command-line interface
- 🎯 Customizable page titles
- 📦 Self-contained HTML output (CSS included)

## Requirements

- Python 3.6+
- `markdown` library

## Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install markdown
```

## Usage

### Basic Usage

Convert a Markdown file to HTML:
```bash
python md_to_html.py input.md
```

This creates `input.html` in the same directory.

### Specify Output File

```bash
python md_to_html.py README.md index.html
```

### Custom Page Title

```bash
python md_to_html.py document.md output.html "My Documentation"
```

### As a Python Module

You can also use it programmatically in your Python code:

```python
from md_to_html import convert_markdown_to_html

# Basic conversion
convert_markdown_to_html('input.md')

# With custom output and title
convert_markdown_to_html('input.md', 'output.html', 'My Custom Title')
```

## Command-Line Options

```
python md_to_html.py <input.md> [output.html] [title]
```

| Argument | Description | Required | Default |
|----------|-------------|----------|---------|
| `input.md` | Input Markdown file | Yes | - |
| `output.html` | Output HTML file | No | Same name as input with .html extension |
| `title` | HTML page title | No | Input filename without extension |

## Supported Markdown Features

### Basic Formatting
- **Bold** and *italic* text
- Headers (H1-H6)
- Links and images
- Ordered and unordered lists
- Blockquotes
- Horizontal rules

### Extended Features
- Tables with proper styling
- Fenced code blocks with language specification
- Inline code formatting
- Footnotes
- Definition lists
- Automatic link detection

### Code Highlighting

The converter supports syntax highlighting for code blocks:

````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

Supported languages include Python, JavaScript, Java, C, C++, HTML, CSS, and many more.

## Output

### HTML Structure

The generated HTML includes:
- Proper HTML5 doctype and structure
- UTF-8 character encoding
- Responsive viewport meta tag
- Embedded CSS styling
- Clean, semantic HTML markup

### Styling

The default styling includes:
- **Maximum width**: 800px for optimal readability
- **Typography**: System font stack for native look
- **Code blocks**: Syntax highlighting with GitHub-style background
- **Tables**: Bordered cells with hover effects
- **Links**: Styled with hover effects
- **Headers**: Proper hierarchy with bottom borders
- **Blockquotes**: Left border accent
- **Responsive**: Mobile-friendly design

## Example

### Input Markdown (`example.md`):

```markdown
# My Project

This is a **great** project that does amazing things.

## Features

- Fast performance
- Easy to use
- Well documented

## Code Example

```python
print("Hello, World!")
```

## Installation

Run this command:

```bash
pip install myproject
```
```

### Command:

```bash
python md_to_html.py example.md
```

### Output (`example.html`):

A beautifully styled HTML page with proper formatting, code highlighting, and responsive design.

## Use Cases

### Documentation
Convert README.md files to HTML for hosting or sharing:
```bash
python md_to_html.py README.md docs.html "Project Documentation"
```

### Blog Posts
Transform Markdown blog posts to HTML:
```bash
python md_to_html.py post.md blog-post.html "My Blog Post"
```

### Notes and Guides
Create styled HTML versions of your notes:
```bash
python md_to_html.py notes.md study-guide.html "Study Guide"
```

### Project Pages
Generate simple project pages:
```bash
python md_to_html.py project.md index.html "My Project"
```

## Customization

### Modifying Styles

The CSS is embedded in the HTML template within the script. To customize styling:

1. Open `md_to_html.py`
2. Locate the `html_template` variable in the `convert_markdown_to_html` function
3. Modify the `<style>` section to your preferences
4. Run the conversion again

### Example Customizations

**Dark mode:**
```css
body {
    background-color: #1e1e1e;
    color: #d4d4d4;
}
```

**Custom fonts:**
```css
body {
    font-family: 'Georgia', serif;
}
```

**Custom colors:**
```css
a {
    color: #ff6b6b;
}
```

## Markdown Extensions

The converter uses the following Python Markdown extensions:

- **extra**: Enables tables, footnotes, definition lists, and more
- **codehilite**: Provides syntax highlighting for code blocks

To add more extensions, modify the `markdown.markdown()` call in the script:

```python
html_body = markdown.markdown(md_content, extensions=['extra', 'codehilite', 'toc'])
```

Available extensions: `toc` (table of contents), `abbr` (abbreviations), `attr_list` (attribute lists), and more.

## Batch Conversion

To convert multiple Markdown files at once, use a shell script:

**Linux/Mac:**
```bash
for file in *.md; do
    python md_to_html.py "$file"
done
```

**Windows (PowerShell):**
```powershell
Get-ChildItem *.md | ForEach-Object {
    python md_to_html.py $_.Name
}
```

## Error Handling

The script handles common errors gracefully:

- **File not found**: Clear error message if input file doesn't exist
- **Permission errors**: Reports issues with reading/writing files
- **Encoding issues**: Uses UTF-8 encoding by default
- **Invalid Markdown**: Processes what it can, ignoring invalid syntax

## Tips and Best Practices

1. **Preview in browser**: Open the generated HTML in a browser to verify formatting
2. **Validate Markdown**: Use a Markdown linter before conversion for best results
3. **Image paths**: Use relative paths for images to maintain portability
4. **Large files**: The converter handles large Markdown files efficiently
5. **Version control**: Keep both .md and .html files if tracking changes

## Comparison with Other Tools

| Feature | This Tool | Pandoc | Online Converters |
|---------|-----------|--------|-------------------|
| Offline | ✅ | ✅ | ❌ |
| Customizable | ✅ | ✅ | ❌ |
| Lightweight | ✅ | ❌ | ✅ |
| Built-in styling | ✅ | ❌ | ✅ |
| Command-line | ✅ | ✅ | ❌ |
| Python API | ✅ | ❌ | ❌ |

## Troubleshooting

### Code blocks not highlighted

**Problem:** Code blocks appear without syntax highlighting

**Solution:** Install the Pygments library for enhanced highlighting:
```bash
pip install Pygments
```

### Unicode characters display incorrectly

**Problem:** Special characters show as `�` or boxes

**Solution:** The script uses UTF-8 by default. Ensure your Markdown file is saved as UTF-8.

### Styles not applied

**Problem:** HTML shows plain text without styling

**Solution:** The CSS is embedded in the HTML. Check that the output file was fully written.

### Import error for markdown

**Problem:** `ModuleNotFoundError: No module named 'markdown'`

**Solution:** Install the markdown library:
```bash
pip install markdown
```
