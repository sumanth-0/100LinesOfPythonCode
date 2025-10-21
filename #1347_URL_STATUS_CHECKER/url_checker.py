import requests
import sys
import os
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def is_valid_url(url):
    """Check if the URL has a valid format."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def check_url(url, timeout=10):
    """
    Check if a URL is online or broken.
    
    Args:
        url: The URL to check
        timeout: Request timeout in seconds
    
    Returns:
        dict: Status information about the URL
    """
    url = url.strip()
    
    if not url or url.startswith('#'):
        return None
    
    if not is_valid_url(url):
        return {
            'url': url,
            'status': 'INVALID',
            'status_code': None,
            'message': 'Invalid URL format'
        }
    
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        
        if response.status_code >= 400:
            response = requests.get(url, timeout=timeout, allow_redirects=True)
        
        if response.status_code < 400:
            status = 'ONLINE'
            message = 'URL is accessible'
        else:
            status = 'BROKEN'
            message = f'HTTP error {response.status_code}'
        
        return {
            'url': url,
            'status': status,
            'status_code': response.status_code,
            'message': message
        }
    
    except requests.exceptions.Timeout:
        return {
            'url': url,
            'status': 'TIMEOUT',
            'status_code': None,
            'message': 'Request timed out'
        }
    except requests.exceptions.ConnectionError:
        return {
            'url': url,
            'status': 'BROKEN',
            'status_code': None,
            'message': 'Connection failed'
        }
    except requests.exceptions.TooManyRedirects:
        return {
            'url': url,
            'status': 'BROKEN',
            'status_code': None,
            'message': 'Too many redirects'
        }
    except Exception as e:
        return {
            'url': url,
            'status': 'ERROR',
            'status_code': None,
            'message': str(e)
        }

def check_urls_from_file(input_file, output_file=None, max_workers=10, timeout=10):
    """
    Check all URLs from a text file.
    
    Args:
        input_file: Path to file containing URLs (one per line)
        output_file: Path to output report file (optional)
        max_workers: Number of concurrent threads
        timeout: Request timeout in seconds
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    if not urls:
        print("No URLs found in the file.")
        return
    
    print(f"Checking {len(urls)} URLs...\n")
    
    results = []
    online_count = 0
    broken_count = 0
    error_count = 0
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(check_url, url, timeout): url for url in urls}
        
        for i, future in enumerate(as_completed(future_to_url), 1):
            result = future.result()
            
            if result:
                results.append(result)
                
                print(f"[{i}/{len(urls)}] {result['status']}: {result['url']}")
                
                if result['status'] == 'ONLINE':
                    online_count += 1
                elif result['status'] in ['BROKEN', 'TIMEOUT']:
                    broken_count += 1
                else:
                    error_count += 1
    
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total URLs checked: {len(results)}")
    print(f"Online: {online_count}")
    print(f"Broken/Timeout: {broken_count}")
    print(f"Invalid/Error: {error_count}")
    print("="*80)
    
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"URL Check Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*80 + "\n\n")
                
                f.write(f"Total URLs checked: {len(results)}\n")
                f.write(f"Online: {online_count}\n")
                f.write(f"Broken/Timeout: {broken_count}\n")
                f.write(f"Invalid/Error: {error_count}\n")
                f.write("\n" + "="*80 + "\n\n")
                
                for status_type in ['BROKEN', 'TIMEOUT', 'INVALID', 'ERROR', 'ONLINE']:
                    filtered = [r for r in results if r['status'] == status_type]
                    if filtered:
                        f.write(f"\n{status_type} URLs ({len(filtered)}):\n")
                        f.write("-"*80 + "\n")
                        for r in filtered:
                            f.write(f"URL: {r['url']}\n")
                            if r['status_code']:
                                f.write(f"Status Code: {r['status_code']}\n")
                            f.write(f"Message: {r['message']}\n\n")
            
            print(f"\nDetailed report saved to: {output_file}")
        except Exception as e:
            print(f"\nError writing report: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python url_checker.py <input_file.txt> [output_report.txt] [--timeout SECONDS] [--workers NUM]")
        print("\nExample: python url_checker.py urls.txt report.txt --timeout 5 --workers 20")
        print("\nThe input file should contain one URL per line.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = None
    timeout = 10
    max_workers = 10
    
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--timeout' and i + 1 < len(sys.argv):
            timeout = int(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == '--workers' and i + 1 < len(sys.argv):
            max_workers = int(sys.argv[i + 1])
            i += 2
        else:
            output_file = sys.argv[i]
            i += 1
    
    check_urls_from_file(input_file, output_file, max_workers, timeout)

if __name__ == "__main__":
    main()