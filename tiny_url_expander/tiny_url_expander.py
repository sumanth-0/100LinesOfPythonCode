#!/usr/bin/env python3
"""Tiny URL Expander - Expand shortened URLs to their full destination."""

import sys
import argparse
from urllib.parse import urlparse

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    import http.client
    import urllib.parse
    HAS_REQUESTS = False


def expand_url_requests(short_url, timeout=10):
    """Expand URL using requests library."""
    try:
        response = requests.head(short_url, allow_redirects=True, timeout=timeout)
        return response.url
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def expand_url_http_client(short_url, timeout=10, max_redirects=10):
    """Expand URL using http.client (stdlib)."""
    parsed = urlparse(short_url)
    if not parsed.scheme:
        short_url = 'http://' + short_url
        parsed = urlparse(short_url)
    
    host = parsed.netloc
    path = parsed.path or '/'
    if parsed.query:
        path += '?' + parsed.query
    
    redirects = 0
    
    while redirects < max_redirects:
        try:
            if parsed.scheme == 'https':
                conn = http.client.HTTPSConnection(host, timeout=timeout)
            else:
                conn = http.client.HTTPConnection(host, timeout=timeout)
            
            conn.request('HEAD', path)
            response = conn.getresponse()
            
            if response.status in (301, 302, 303, 307, 308):
                location = response.getheader('Location')
                if not location:
                    return short_url
                
                # Handle relative URLs
                if location.startswith('/'):
                    location = f"{parsed.scheme}://{host}{location}"
                elif not location.startswith('http'):
                    location = f"{parsed.scheme}://{host}/{location}"
                
                parsed = urlparse(location)
                host = parsed.netloc
                path = parsed.path or '/'
                if parsed.query:
                    path += '?' + parsed.query
                short_url = location
                redirects += 1
            else:
                return short_url
            
            conn.close()
        except Exception as e:
            return f"Error: {e}"
    
    return short_url


def expand_url(short_url, timeout=10):
    """Expand shortened URL to full destination."""
    if HAS_REQUESTS:
        return expand_url_requests(short_url, timeout)
    else:
        return expand_url_http_client(short_url, timeout)


def main():
    parser = argparse.ArgumentParser(
        description='Expand shortened URLs to their full destination'
    )
    parser.add_argument('url', help='Shortened URL to expand')
    parser.add_argument('-t', '--timeout', type=int, default=10,
                        help='Request timeout in seconds (default: 10)')
    
    args = parser.parse_args()
    
    print(f"Expanding: {args.url}")
    expanded = expand_url(args.url, args.timeout)
    print(f"Full URL: {expanded}")


if __name__ == '__main__':
    main()
