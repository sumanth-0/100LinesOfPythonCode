import sys
import cv2

# Inform user about correct usage.
if len(sys.argv) < 2:
    print("Usage: python qr_reader.py path/to/image.png")
    exit()

# Store file path.
img_path = sys.argv[1]

# Import and store the image.
image = cv2.imread(img_path)

# Create a QRCodeDetector instance.
detector = cv2.QRCodeDetector()

# Decode the information.
# Note that fancy QR codes may not work well. For best results use simplistic QR codes.
decoded_text, points, _ = detector.detectAndDecode(image)

# Print out the contents.
print(decoded_text)
