"""
Example usage of the URL Shortener module.
This demonstrates how to import and use the url_shortener functions.
"""

from url_shortener import shorten_url, shorten_multiple_urls

# Example 1: Shorten a single URL
print("Example 1: Single URL")
print("-" * 40)
long_url = "https://www.example.com/very/long/url/path/that/needs/shortening"
short_url = shorten_url(long_url)
print(f"Original: {long_url}")
print(f"Shortened: {short_url}\n")

# Example 2: Shorten multiple URLs
print("Example 2: Multiple URLs")
print("-" * 40)
urls_to_shorten = [
    "https://github.com/sumanth-0/100LinesOfPythonCode",
    "https://www.python.org/dev/peps/pep-0008/",
    "https://docs.python.org/3/library/urllib.parse.html"
]

results = shorten_multiple_urls(urls_to_shorten)
for original, shortened in results.items():
    print(f"{original}")
    print(f"  → {shortened}\n")

