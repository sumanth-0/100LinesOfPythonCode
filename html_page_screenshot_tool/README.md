# HTML Page Screenshot Tool

A Python script that captures full-page screenshots of websites using Selenium WebDriver and saves them as PNG files.

## Description

This tool allows you to capture full-page screenshots of any website by providing its URL. It uses Selenium WebDriver with Chrome in headless mode to render the page and capture a complete screenshot, including content that might be below the fold.

## Features

- 🖼️ Capture full-page screenshots of websites
- 🚀 Headless browser operation (no GUI required)
- 📏 Automatic page dimension detection
- 💾 Save screenshots as PNG files
- ⚡ Fast and efficient
- 🔧 Customizable output filename

## Requirements

- Python 3.6+
- selenium
- webdriver-manager

## Installation

1. Clone this repository or download the script:

```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/html_page_screenshot_tool
```

2. Install the required dependencies:

```bash
pip install selenium webdriver-manager
```

Note: Chrome browser must be installed on your system. The script will automatically download and manage the appropriate ChromeDriver.

## Usage

### Basic Usage

Capture a screenshot with default filename (screenshot.png):

```bash
python html_page_screenshot_tool.py https://example.com
```

### Custom Filename

Specify a custom output filename:

```bash
python html_page_screenshot_tool.py https://example.com my_screenshot.png
```

### Command Format

```bash
python html_page_screenshot_tool.py <URL> [output_filename]
```

**Arguments:**
- `URL` (required): The website URL to capture (must start with http:// or https://)
- `output_filename` (optional): The output filename for the screenshot (default: screenshot.png)

## Examples

```bash
# Capture GitHub homepage
python html_page_screenshot_tool.py https://github.com github.png

# Capture a news website
python html_page_screenshot_tool.py https://news.ycombinator.com hackernews.png

# Capture with default filename
python html_page_screenshot_tool.py https://python.org
```

## How It Works

1. **Setup**: The script configures Chrome WebDriver in headless mode for background operation
2. **Navigation**: It navigates to the specified URL
3. **Wait**: Waits for the page to load completely
4. **Measure**: Calculates the full page dimensions (width and height)
5. **Resize**: Adjusts the browser window to capture the entire page
6. **Capture**: Takes a screenshot and saves it as a PNG file
7. **Cleanup**: Closes the browser and reports success

## Technical Details

- Uses Selenium WebDriver with Chrome in headless mode
- Automatically installs and manages ChromeDriver using webdriver-manager
- Captures full page height and width for complete screenshots
- Default window size: 1920x1080 (adjusts based on page content)
- Waits for page load and dynamic content rendering

## Error Handling

The script handles common errors gracefully:
- Invalid URL format
- Network connectivity issues
- Page load timeouts
- Browser driver issues

## Limitations

- Requires Chrome browser to be installed
- May not capture content that loads after extensive delays
- JavaScript-heavy sites might require longer wait times
- Very large pages might result in large PNG files

## Contributing

This project is part of the 100 Lines of Python Code challenge. Contributions, issues, and feature requests are welcome!

## License

This project is open source and available under the MIT License.

## Related Projects

For alternative screenshot tools, check out:
- html2image (alternative library)
- Pyppeteer (Python port of Puppeteer)
- Playwright (modern automation library)

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Part of [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) - Issue #674**
