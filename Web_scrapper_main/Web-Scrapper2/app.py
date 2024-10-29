from flask import Flask, render_template, request
from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup
from lxml import html

app = Flask(__name__)

# 1. Function to scrape dynamic content using Playwright
def scrape_with_playwright(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            paragraphs = page.locator('p')
            scraped_content = "\n".join([paragraphs.nth(i).inner_text() for i in range(min(10, paragraphs.count()))])
            browser.close()
            return scraped_content if scraped_content else "No content found."
    except Exception as e:
        return f"Error during Playwright scraping: {str(e)}"

# 2. Function to scrape using BeautifulSoup
def scrape_with_beautifulsoup(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        scraped_content = "\n".join([p.text for p in paragraphs[:10]])
        return scraped_content if scraped_content else "No content found."
    except Exception as e:
        return f"Error during BeautifulSoup scraping: {str(e)}"

# 3. Function to scrape using lxml
def scrape_with_lxml(url):
    try:
        response = requests.get(url)
        tree = html.fromstring(response.content)
        paragraphs = tree.xpath('//p/text()')
        scraped_content = "\n".join(paragraphs[:10])
        return scraped_content if scraped_content else "No content found."
    except Exception as e:
        return f"Error during lxml scraping: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    scraped_content = None
    error_message = None

    if request.method == 'POST':
        url = request.form.get('url')
        method = request.form.get('method')

        if url:
            if method == 'playwright':
                scraped_content = scrape_with_playwright(url)
            elif method == 'beautifulsoup':
                scraped_content = scrape_with_beautifulsoup(url)
            elif method == 'lxml':
                scraped_content = scrape_with_lxml(url)
            else:
                error_message = "Invalid scraping method selected."
        else:
            error_message = "Please provide a valid URL."

    return render_template('index.html', scraped_content=scraped_content, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
