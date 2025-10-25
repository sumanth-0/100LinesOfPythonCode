import re
import sys
import os
from html import unescape #this is done to convert escape characters like &lt; back to normal
def extract_emails(text):
    text = unescape(text)
    pattern = re.compile(
        r"(?<![\w.-])([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?=[^\w@-]|$)",
        re.IGNORECASE
    )
    return set(re.findall(pattern, text))

def read_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    try:
        with open(filepath,"r",encoding="utf-8",errors="ignore") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def main():
    if len(sys.argv)<2: #invalid usage
        print("Usage: python extract_emails.py <file>")
        sys.exit(1)

    filename=sys.argv[1] #second argument in usage
    text=read_file(filename)
    emails=extract_emails(text)

    if emails:
        print(f"Found {len(emails)} email address(es):\n")
        for email in sorted(emails):
            print(email)
    else:
        print("No email addresses found.")
if __name__ == "__main__":
    main()

