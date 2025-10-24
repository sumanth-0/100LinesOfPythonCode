import pyshorteners
import sys

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        return short_url
    except Exception as e:
        print(f"Error: Could not shorten URL. Details: {e}", file=sys.stderr)
        return None

def main():
    long_url = input("Enter the URL to shorten: ")

    if not long_url.strip():
        print("Error: No URL provided.", file=sys.stderr)
        sys.exit(1)

    short_url = shorten_url(long_url)

    if short_url:
        print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()