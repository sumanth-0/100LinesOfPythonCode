# IP Geolocation CLI

A powerful command-line tool to lookup geographical location information for IP addresses using the free ip-api.com service.

## Features

- **Single IP Lookup**: Query location data for individual IP addresses
- **Batch Processing**: Process multiple IPs from a file efficiently
- **Interactive Mode**: Continuous lookup mode for multiple queries
- **JSON Output**: Export results in JSON format for further processing
- **Comprehensive Data**: Retrieve country, region, city, timezone, ISP, coordinates, and more

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Install Dependencies

```bash
pip install requests
```

## Usage

### Single IP Lookup

Lookup a single IP address:

```bash
python ip_geolocation_cli.py 8.8.8.8
```

Output:
```
============================================================
IP Address: 8.8.8.8
============================================================
Country: United States (US)
Region: California (CA)
City: Mountain View
ZIP Code: 94035
Timezone: America/Los_Angeles
Coordinates: 37.386, -122.0838
ISP: Google LLC
Organization: Google Public DNS
AS Number: AS15169 Google LLC
============================================================
```

### Batch Processing

Process multiple IP addresses from a file:

```bash
python ip_geolocation_cli.py --batch ips.txt
```

Create a file `ips.txt` with one IP per line:
```
8.8.8.8
1.1.1.1
208.67.222.222
```

### Interactive Mode

Enter interactive mode for continuous lookups:

```bash
python ip_geolocation_cli.py --interactive
```

Then enter IP addresses one by one, or type `quit` to exit.

### JSON Output

Get results in JSON format:

```bash
python ip_geolocation_cli.py 8.8.8.8 --json
```

## Command Line Options

```
usage: ip_geolocation_cli.py [-h] [--batch FILE] [--interactive] [--json] [ip]

IP Geolocation CLI - Lookup location data for IP addresses

positional arguments:
  ip                    IP address to lookup

optional arguments:
  -h, --help            show this help message and exit
  --batch FILE, -b FILE
                        File containing IP addresses (one per line)
  --interactive, -i     Run in interactive mode
  --json, -j            Output results in JSON format
```

## API Information

This tool uses the free [ip-api.com](http://ip-api.com/) service which provides:

- **Rate Limit**: 45 requests per minute for non-commercial use
- **Batch Requests**: Up to 100 IPs per batch request
- **No API Key Required**: Free tier doesn't require registration

### Data Fields Retrieved

- IP Address
- Country (name and code)
- Region (name and code)
- City
- ZIP/Postal Code
- Latitude and Longitude
- Timezone
- ISP (Internet Service Provider)
- Organization
- AS (Autonomous System) Number

## Examples

### Example 1: Lookup Google DNS

```bash
python ip_geolocation_cli.py 8.8.8.8
```

### Example 2: Batch lookup multiple IPs

```bash
echo "8.8.8.8" > ips.txt
echo "1.1.1.1" >> ips.txt
echo "208.67.222.222" >> ips.txt
python ip_geolocation_cli.py --batch ips.txt
```

### Example 3: Get JSON output for scripting

```bash
python ip_geolocation_cli.py 8.8.8.8 --json | jq '.country'
```

## Error Handling

The tool handles various errors gracefully:

- Invalid IP addresses
- Network connectivity issues
- API rate limiting
- File not found errors
- JSON parsing errors

## Limitations

- Free tier has rate limits (45 requests/minute)
- Geolocation accuracy may vary
- Some IPs (private ranges) won't return location data
- Requires internet connection

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is part of the 100LinesOfPythonCode repository.

## Related Issues

References: #1038

## Credits

- API Service: [ip-api.com](http://ip-api.com/)
- Repository: [100LinesOfPythonCode](https://github.com/sumanth-0/100LinesOfPythonCode)

## Support

If you encounter any issues or have questions, please open an issue in the repository.
