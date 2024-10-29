# Flask Web Scraper with Multiple Libraries

This project is a Flask web application that allows users to scrape content from websites using three different Python web scraping libraries. It provides a simple UI to input a URL, select a scraping method, and view the scraped content on the same page.

## Features

- **Scraping Methods**: Supports three popular scraping libraries:
  - **Playwright**: For scraping dynamic content. It’s ideal for pages that use JavaScript heavily for rendering, such as modern web applications that rely on client-side frameworks like React, Angular, or Vue.
  - **BeautifulSoup**: For simple and fast HTML parsing. It works best for scraping pages where all relevant content is directly present in the initial HTML response.
  - **lxml**: A fast XML and HTML parser using XPath. Like BeautifulSoup, it won’t capture content that’s dynamically loaded by JavaScript.

- **User Interface**: Input a URL, choose the scraping method, and view the scraped content via the web interface.
- **Dynamic Content Support**: Ability to scrape dynamic content (such as JavaScript-rendered pages) using Playwright.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Scraping Libraries**:
  - [Playwright](https://playwright.dev/python/)
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
  - [lxml](https://lxml.de/)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- A web browser

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd your_project

2. **Install Required Packages: Make sure you have Python installed (preferably Python 3). Install the required packages using pip**:
    ```bash
    pip install flask requests beautifulsoup4 lxml playwright

3. **Playwright requires an additional setup to install browsers**:
    ```bash
    playwright install
3. **Run the Application: Start the Flask application**:
    ```bash
    python app.py

4. **Access the App: Open your web browser and navigate to http://127.0.0.1:500 to access the application.**
