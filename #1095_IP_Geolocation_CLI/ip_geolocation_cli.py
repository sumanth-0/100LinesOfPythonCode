#!/usr/bin/env python3
"""
IP Geolocation CLI Tool
Finds location information (city, country, ISP) from an IP address
Uses ip-api.com free API (no key required)
"""

import sys
import json
import argparse
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from typing import Dict, Optional


class IPGeolocation:
    """Class to handle IP geolocation lookups"""
    
    API_URL = "http://ip-api.com/json/"
    
    def __init__(self):
        self.fields = "status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
    
    def get_location(self, ip: Optional[str] = None) -> Dict:
        """Get geolocation data for IP address"""
        try:
            url = f"{self.API_URL}{ip or ''}?fields={self.fields}"
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            
            with urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                return data
        except HTTPError as e:
            return {"status": "fail", "message": f"HTTP Error: {e.code}"}
        except URLError as e:
            return {"status": "fail", "message": f"Connection Error: {e.reason}"}
        except Exception as e:
            return {"status": "fail", "message": f"Error: {str(e)}"}
    
    def format_output(self, data: Dict, format_type: str = "text") -> str:
        """Format the geolocation data"""
        if data.get("status") == "fail":
            return f"Error: {data.get('message', 'Unknown error')}"
        
        if format_type == "json":
            return json.dumps(data, indent=2)
        
        # Text format
        output = []
        output.append(f"\n{'='*50}")
        output.append(f"IP Geolocation Information")
        output.append(f"{'='*50}")
        output.append(f"IP Address: {data.get('query', 'N/A')}")
        output.append(f"\nLocation:")
        output.append(f"  City: {data.get('city', 'N/A')}")
        output.append(f"  Region: {data.get('regionName', 'N/A')} ({data.get('region', 'N/A')})")
        output.append(f"  Country: {data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
        output.append(f"  ZIP Code: {data.get('zip', 'N/A')}")
        output.append(f"\nCoordinates:")
        output.append(f"  Latitude: {data.get('lat', 'N/A')}")
        output.append(f"  Longitude: {data.get('lon', 'N/A')}")
        output.append(f"  Timezone: {data.get('timezone', 'N/A')}")
        output.append(f"\nISP Information:")
        output.append(f"  ISP: {data.get('isp', 'N/A')}")
        output.append(f"  Organization: {data.get('org', 'N/A')}")
        output.append(f"  AS: {data.get('as', 'N/A')}")
        output.append(f"{'='*50}\n")
        return "\n".join(output)


def main():
    """Main function to run the CLI"""
    parser = argparse.ArgumentParser(
        description="IP Geolocation CLI - Find location info from IP addresses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Examples:\n"
               "  python ip_geolocation_cli.py 8.8.8.8\n"
               "  python ip_geolocation_cli.py --json 1.1.1.1\n"
               "  python ip_geolocation_cli.py  # Uses your current IP"
    )
    
    parser.add_argument(
        "ip",
        nargs="?",
        help="IP address to lookup (if omitted, uses your current IP)"
    )
    
    parser.add_argument(
        "-j", "--json",
        action="store_true",
        help="Output in JSON format"
    )
    
    args = parser.parse_args()
    
    geo = IPGeolocation()
    data = geo.get_location(args.ip)
    output_format = "json" if args.json else "text"
    result = geo.format_output(data, output_format)
    print(result)


if __name__ == "__main__":
    main()
