# Random Quote Visualizer

## Overview
The Random Quote Visualizer is a Python-based desktop application that fetches random quotes from the ZenQuotes API and displays them in a visually engaging window. Each quote appears with a random background color and font style, making it dynamic and interesting to use. The window automatically updates every few seconds, or you can manually click to fetch a new quote instantly.

## Features
- Fetches a random quote from the ZenQuotes API.
- Displays quotes with a random combination of background colors and fonts.
- Automatically updates the quote every 5 seconds.
- Supports manual updates by clicking anywhere in the window.
- Simple and clean UI using tkinter.

## Requirements
- Python 3.x
- requests library
- tkinter library
- Internet connection for fetching quotes from the API.

## Installation
1. **Clone or download the project to your local machine:**
   ```bash
   git clone <repository-url> <repository-directory>
   ```

2. **Install the required Python packages by running the following command:**
   ```bash
   pip install requests
   ```

3. **Make sure you have Python 3.x installed on your system. If not, you can download it from Python’s official website.**

## Usage
1. Navigate to `random-quote-visualizer` directory.
   ```bash
   cd random-quote-visualizer
   ```

2. Run the Python script:
   ```bash
   python RandomQuoteVisualizer.py
   ```

3. The application will open a window displaying a random quote with a random background and font. It will automatically refresh every 5 seconds.

4. If you'd like to manually fetch a new quote, simply click anywhere on the window, it will refresh after 1-2 seconds.

## Example Output
- Quotes will appear with random colors and fonts.
- Quotes will be updated every 5 seconds, or by clicking the window.