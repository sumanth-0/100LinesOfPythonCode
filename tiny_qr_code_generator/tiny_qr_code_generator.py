#!/usr/bin/env python3
"""
Tiny QR Code Generator
Generates QR codes from text or URLs using the qrcode library.
"""

import qrcode
import argparse
import sys
from pathlib import Path


def generate_qr_code(data, output_file="qr_code.png", box_size=10, border=4):
    """
    Generate a QR code from the provided data.
    
    Args:
        data (str): The text or URL to encode in the QR code
        output_file (str): The output filename for the QR code image
        box_size (int): The size of each box in the QR code grid
        border (int): The border size around the QR code
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        
        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)
        
        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        img.save(output_file)
        
        print(f"✓ QR code successfully generated and saved as '{output_file}'")
        print(f"  Data encoded: {data[:50]}{'...' if len(data) > 50 else ''}")
        return True
        
    except Exception as e:
        print(f"✗ Error generating QR code: {e}", file=sys.stderr)
        return False


def main():
    """
    Main function to handle command-line arguments and generate QR code.
    """
    parser = argparse.ArgumentParser(
        description="Generate QR codes from text or URLs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "Hello, World!"
  %(prog)s "https://github.com" -o github_qr.png
  %(prog)s "Contact: +1234567890" -s 15 -b 2
        """
    )
    
    parser.add_argument(
        "data",
        help="Text or URL to encode in the QR code"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="qr_code.png",
        help="Output filename for the QR code image (default: qr_code.png)"
    )
    
    parser.add_argument(
        "-s", "--size",
        type=int,
        default=10,
        help="Box size for each QR code pixel (default: 10)"
    )
    
    parser.add_argument(
        "-b", "--border",
        type=int,
        default=4,
        help="Border size around the QR code (default: 4)"
    )
    
    args = parser.parse_args()
    
    # Generate the QR code
    generate_qr_code(args.data, args.output, args.size, args.border)


if __name__ == "__main__":
    main()
