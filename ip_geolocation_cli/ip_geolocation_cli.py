#!/usr/bin/env python3
"""
IP Geolocation CLI

A command-line tool to lookup geographical location information for IP addresses.
This tool uses the free ip-api.com service to retrieve location data including:
- Country, Region, City
- Latitude and Longitude
- ISP and Organization
- Timezone

Usage:
    python ip_geolocation_cli.py <ip_address>
    python ip_geolocation_cli.py --batch <file_with_ips>
    python ip_geolocation_cli.py --interactive
"""

import sys
import json
import argparse
from typing import Dict, List, Optional
try:
    import requests
except ImportError:
    print("Error: 'requests' library not installed.")
    print("Install it using: pip install requests")
    sys.exit(1)


class IPGeolocation:
    """Main class for IP geolocation lookup functionality."""
    
    API_URL = "http://ip-api.com/json/{}"
    BATCH_API_URL = "http://ip-api.com/batch"
    
    def __init__(self):
        """Initialize the IPGeolocation class."""
        self.session = requests.Session()
    
    def lookup_ip(self, ip_address: str) -> Optional[Dict]:
        """
        Lookup geolocation data for a single IP address.
        
        Args:
            ip_address: The IP address to lookup
            
        Returns:
            Dictionary containing location data or None on failure
        """
        try:
            response = self.session.get(
                self.API_URL.format(ip_address),
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get('status') == 'fail':
                print(f"Error: {data.get('message', 'Unknown error')}")
                return None
                
            return data
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except json.JSONDecodeError:
            print("Error: Failed to parse response")
            return None
    
    def lookup_batch(self, ip_addresses: List[str]) -> List[Dict]:
        """
        Lookup geolocation data for multiple IP addresses.
        
        Args:
            ip_addresses: List of IP addresses to lookup
            
        Returns:
            List of dictionaries containing location data
        """
        try:
            # API allows max 100 IPs per batch request
            batch_size = 100
            results = []
            
            for i in range(0, len(ip_addresses), batch_size):
                batch = ip_addresses[i:i + batch_size]
                response = self.session.post(
                    self.BATCH_API_URL,
                    json=batch,
                    timeout=30
                )
                response.raise_for_status()
                results.extend(response.json())
            
            return results
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return []
        except json.JSONDecodeError:
            print("Error: Failed to parse response")
            return []
    
    def display_result(self, data: Dict) -> None:
        """
        Display formatted geolocation data.
        
        Args:
            data: Dictionary containing location data
        """
        print("\n" + "="*60)
        print(f"IP Address: {data.get('query', 'N/A')}")
        print("="*60)
        print(f"Country: {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
        print(f"Region: {data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"ZIP Code: {data.get('zip', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
        print(f"Coordinates: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
        print(f"ISP: {data.get('isp', 'N/A')}")
        print(f"Organization: {data.get('org', 'N/A')}")
        print(f"AS Number: {data.get('as', 'N/A')}")
        print("="*60 + "\n")


def read_ips_from_file(filename: str) -> List[str]:
    """
    Read IP addresses from a file (one per line).
    
    Args:
        filename: Path to file containing IP addresses
        
    Returns:
        List of IP addresses
    """
    try:
        with open(filename, 'r') as f:
            ips = [line.strip() for line in f if line.strip()]
        return ips
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def interactive_mode():
    """
    Run the tool in interactive mode, allowing multiple lookups.
    """
    geo = IPGeolocation()
    print("\n=== IP Geolocation CLI - Interactive Mode ===")
    print("Enter IP addresses to lookup (or 'quit' to exit)\n")
    
    while True:
        try:
            ip_input = input("Enter IP address: ").strip()
            
            if ip_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not ip_input:
                continue
            
            result = geo.lookup_ip(ip_input)
            if result:
                geo.display_result(result)
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    """
    Main entry point for the CLI application.
    """
    parser = argparse.ArgumentParser(
        description="IP Geolocation CLI - Lookup location data for IP addresses",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        'ip',
        nargs='?',
        help='IP address to lookup'
    )
    parser.add_argument(
        '--batch',
        '-b',
        metavar='FILE',
        help='File containing IP addresses (one per line)'
    )
    parser.add_argument(
        '--interactive',
        '-i',
        action='store_true',
        help='Run in interactive mode'
    )
    parser.add_argument(
        '--json',
        '-j',
        action='store_true',
        help='Output results in JSON format'
    )
    
    args = parser.parse_args()
    geo = IPGeolocation()
    
    # Interactive mode
    if args.interactive:
        interactive_mode()
        return
    
    # Batch mode
    if args.batch:
        ips = read_ips_from_file(args.batch)
        if not ips:
            sys.exit(1)
        
        print(f"Looking up {len(ips)} IP addresses...")
        results = geo.lookup_batch(ips)
        
        if args.json:
            print(json.dumps(results, indent=2))
        else:
            for result in results:
                if result.get('status') == 'success':
                    geo.display_result(result)
        return
    
    # Single IP mode
    if args.ip:
        result = geo.lookup_ip(args.ip)
        if result:
            if args.json:
                print(json.dumps(result, indent=2))
            else:
                geo.display_result(result)
        return
    
    # No arguments provided
    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
