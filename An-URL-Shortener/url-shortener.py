import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        short_hash = hashlib.md5(long_url.encode()).hexdigest()[:6]
        short_url = f"https://short.url/{short_hash}"
        self.url_mapping[short_url] = long_url
        return short_url

    def retrieve_url(self, short_url):
        return self.url_mapping.get(short_url, "URL not found")

# Example usage
if __name__ == "__main__":
    shortener = URLShortener()
    long_url = "https://www.example.com/some/very/long/url"
    short_url = shortener.shorten_url(long_url)
    print("Short URL:", short_url)

    original_url = shortener.retrieve_url(short_url)
    print("Original URL:", original_url)
