# IP Geolocation CLI

## Description
A command-line tool to find location information (city, country, ISP) from IP addresses. This script uses the free ip-api.com API to retrieve geolocation data for any given IP address or your current public IP.

## Features
- Get geolocation information for any IP address
- Automatically detect and use your current public IP if no IP is provided
- Display detailed information including:
  - City, Region, Country
  - ZIP Code
  - Latitude and Longitude coordinates
  - Timezone
  - ISP and Organization details
- Support for both text and JSON output formats
- No API key required

## Requirements
- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation
No installation required! Just download the script and run it.

```bash
wget https://raw.githubusercontent.com/anieoni0/100LinesOfPythonCode/main/%231095_IP_Geolocation_CLI/ip_geolocation_cli.py
chmod +x ip_geolocation_cli.py
```

## Usage

### Basic usage (your current IP):
```bash
python ip_geolocation_cli.py
```

### Lookup a specific IP address:
```bash
python ip_geolocation_cli.py 8.8.8.8
```

### Get output in JSON format:
```bash
python ip_geolocation_cli.py --json 1.1.1.1
```

### Help:
```bash
python ip_geolocation_cli.py --help
```

## Example Output

### Text format:
```
==================================================
IP Geolocation Information
==================================================
IP Address: 8.8.8.8

Location:
  City: Mountain View
  Region: California (CA)
  Country: United States (US)
  ZIP Code: 94035

Coordinates:
  Latitude: 37.386
  Longitude: -122.0838
  Timezone: America/Los_Angeles

ISP Information:
  ISP: Google LLC
  Organization: Google Public DNS
  AS: AS15169 Google LLC
==================================================
```

### JSON format:
```json
{
  "status": "success",
  "country": "United States",
  "countryCode": "US",
  "region": "CA",
  "regionName": "California",
  "city": "Mountain View",
  "zip": "94035",
  "lat": 37.386,
  "lon": -122.0838,
  "timezone": "America/Los_Angeles",
  "isp": "Google LLC",
  "org": "Google Public DNS",
  "as": "AS15169 Google LLC",
  "query": "8.8.8.8"
}
```

## API Information
This tool uses the free tier of ip-api.com which allows:
- 45 requests per minute from a single IP address
- No API key required
- HTTP access (HTTPS requires paid subscription)

## License
This project is part of the 100LinesOfPythonCode repository.

## Contributing
Fixes Issue #1095

## Author
Contributed to 100LinesOfPythonCode repository
