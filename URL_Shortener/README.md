Simple URL Shortener
A simple command-line Python script that shortens a given URL using the TinyURL service.

Description
This program prompts the user to enter a long URL. It then uses the pyshorteners library to connect to TinyURL, generate a shortened link, and print the result back to the console. The program exits after one successful use.

Features
Simple, single-use command-line interface.

Uses the reliable TinyURL service.

Includes error handling for invalid URLs or network issues.

Installation
Clone the repository or download the script.

Install the required Python library: This script depends on the pyshorteners library. You can install it using pip:

Bash

pip install pyshorteners
Usage
Run the script from your terminal:

Bash

python your_script_name.py
(Replace your_script_name.py with the actual name of the file, e.g., shorten.py)

When prompted, paste or type the long URL you want to shorten and press Enter.

Example
Bash

$ python shorten.py
Enter the URL to shorten: https://www.example-long-domain-name.com/a-very-long-path/page.html
Shortened URL: https://tinyurl.com/a1b2c3d4