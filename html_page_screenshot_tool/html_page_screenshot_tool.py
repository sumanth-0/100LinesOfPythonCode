#!/usr/bin/env python3
"""
HTML Page Screenshot Tool

This script captures a full-page screenshot of a website using Selenium WebDriver.
It saves the screenshot as a PNG file.

Usage:
    python html_page_screenshot_tool.py <URL> [output_filename]

Example:
    python html_page_screenshot_tool.py https://example.com screenshot.png
"""

import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def capture_screenshot(url, output_file="screenshot.png"):
    """
    Capture a full-page screenshot of the given URL.
    
    Args:
        url (str): The URL of the website to screenshot
        output_file (str): The output filename for the screenshot
    
    Returns:
        bool: True if successful, False otherwise
    """
    print(f"Capturing screenshot of: {url}")
    
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = None
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        
        # Navigate to the URL
        driver.get(url)
        
        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(2)  # Additional wait for dynamic content
        
        # Get the full page dimensions
        total_width = driver.execute_script("return document.body.scrollWidth")
        total_height = driver.execute_script("return document.body.scrollHeight")
        
        # Set window size to capture full page
        driver.set_window_size(total_width, total_height)
        time.sleep(1)  # Brief pause for rendering
        
        # Capture the screenshot
        driver.save_screenshot(output_file)
        
        print(f"Screenshot saved successfully as: {output_file}")
        print(f"Dimensions: {total_width}x{total_height}px")
        return True
        
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return False
        
    finally:
        if driver:
            driver.quit()


def main():
    """Main function to handle command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python html_page_screenshot_tool.py <URL> [output_filename]")
        print("Example: python html_page_screenshot_tool.py https://example.com screenshot.png")
        sys.exit(1)
    
    url = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "screenshot.png"
    
    # Validate URL format
    if not url.startswith(("http://", "https://")):
        print("Error: URL must start with http:// or https://")
        sys.exit(1)
    
    # Capture the screenshot
    success = capture_screenshot(url, output_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
