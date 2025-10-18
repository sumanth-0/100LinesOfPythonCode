# Random Wikipedia Page Viewer

A small Python application using **Tkinter** that fetches a random Wikipedia page and displays the title and first paragraph.  

---

## Features

- Fetches a random Wikipedia article.
- Displays the **title** of the page.
- Shows the **first paragraph** (intro extract) of the article.
- Easy-to-use GUI with a single button.

---

## Requirements

- Python 3.6+  
- `requests` library
- `tkinter` (usually included with Python on Windows/Mac/Linux)

Install `requests` if you don’t have it:

bash
pip install requests

## Notes
- Uses the Wikipedia API: https://www.mediawiki.org/wiki/API:Main_page
- A User-Agent header is included to comply with Wikipedia’s API policy.
- If the API is down or there’s a network issue, an error message will appear in the app.