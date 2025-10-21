# Random Wikipedia Page Fetcher

## Description

A Python command-line application that fetches and displays random Wikipedia articles using the Wikipedia API. This tool provides an interactive and colorful way to explore random Wikipedia content with detailed information about each article.

## Features

- 🌍 **Random Article Fetching**: Get random Wikipedia articles with a single command
- 🎨 **Colorful Output**: Beautiful console formatting with ANSI colors
- 📊 **Detailed Information**: Displays article title, summary, URL, categories, and metadata
- 🔄 **Interactive Mode**: Fetch multiple articles in a single session
- ⚡ **Error Handling**: Robust error handling for network issues and API errors
- 📝 **Text Formatting**: Properly formatted text output with word wrapping
- 🏷️ **Category Display**: Shows relevant Wikipedia categories for each article
- 📊 **Metadata**: Displays page ID, language, and word count

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sumanth-0/100LinesOfPythonCode.git
cd 100LinesOfPythonCode/random_wikipedia_page
```

2. Install required dependencies:
```bash
pip install requests
```

## Usage

Run the script from the command line:

```bash
python random_wikipedia_page.py
```

### Example Output

```
╔══════════════════════════════════════════════════════════════╗
║        🌍 RANDOM WIKIPEDIA ARTICLE FETCHER 📚               ║
╚══════════════════════════════════════════════════════════════╝

🔄 Fetching random Wikipedia article...
🔍 Fetching additional details...

================================================================================
📄 ARTICLE TITLE:
Quantum Computing

📝 DESCRIPTION:
Emerging field of computing using quantum mechanics

📚 SUMMARY:
Quantum computing is a field that develops computer technology based on the
principles of quantum theory...

🔗 ARTICLE URL:
https://en.wikipedia.org/wiki/Quantum_Computing

ℹ️  METADATA:
  • Page ID: 12345
  • Language: EN
  • Word Count: 150

🏷️  CATEGORIES:
  1. Computer science
  2. Quantum physics
  3. Emerging technologies
  4. Computing
  5. Technology

================================================================================

Would you like to fetch another random article?
Enter 'y' for yes, any other key to exit:
```

## How It Works

1. **API Request**: The script makes a request to the Wikipedia REST API endpoint `/page/random/summary`
2. **Data Processing**: Parses the JSON response to extract article information
3. **Category Fetching**: Makes an additional API call to fetch article categories
4. **Display**: Formats and displays the information in a user-friendly manner
5. **User Interaction**: Prompts the user to fetch another article or exit

## API Endpoints Used

- **Random Article**: `https://en.wikipedia.org/api/rest_v1/page/random/summary`
- **Categories**: `https://en.wikipedia.org/w/api.php` (with appropriate query parameters)

## Features in Detail

### Colorful Console Output
The script uses ANSI color codes to create an attractive and readable console interface:
- Headers in purple/magenta
- URLs in cyan with underline
- Success messages in green
- Warnings in yellow
- Errors in red

### Error Handling
Comprehensive error handling for:
- Network timeouts
- Connection errors
- API failures
- Missing dependencies
- User interruptions (Ctrl+C)

### Text Formatting
- Automatic word wrapping at 80 characters
- Structured output with clear sections
- Unicode box drawing characters for headers
- Emoji icons for visual enhancement

## Contributing

This project is part of the [100 Lines of Python Code](https://github.com/sumanth-0/100LinesOfPythonCode) repository.

Contributions are welcome! Please feel free to submit a Pull Request.

## Issue Reference

This implementation addresses issue [#1037](https://github.com/sumanth-0/100LinesOfPythonCode/issues/1037)

## License

This project is part of the 100LinesOfPythonCode repository. Please refer to the main repository for license information.

## Author

Created as part of Hacktoberfest 2025 contributions.

## Acknowledgments

- Wikipedia API for providing free access to Wikipedia content
- The open-source community for inspiration and support
- Hacktoberfest for promoting open-source contributions

---

**Note**: This script requires an active internet connection to fetch articles from Wikipedia. Make sure you have the `requests` library installed before running the script.
