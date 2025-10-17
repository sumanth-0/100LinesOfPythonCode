'''
To Install the required libraries, run the following command:

pip install python-barcode Pillow

'''

import barcode 
import os
from barcode.writer import ImageWriter


barcode_format = 'code128'  # You can change this to any supported format like 'ean13', 'upc', etc.

# data 
data = input("Enter the Data to convert into barcode") # Replace with your desired data

output_filename = 'barcode_image'  # Desired output filename without extension
Barcode = barcode.get_barcode_class(barcode_format)

barcode_instance = Barcode(data, writer=ImageWriter())

barcode_instance.save(output_filename)

print(f"Barcode saved as {output_filename}.png")

os.startfile(f"{output_filename}.png")  # Opens the generated barcode image file