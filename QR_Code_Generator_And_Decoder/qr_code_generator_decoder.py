#========== QR Code Generaor and Decoder ===============

import qrcode
import cv2

# ========== QR Code Generator ==========
def generate_qr(data, filename="qrcode.png"):
    """
    Generate a QR code image from given data.
    """
    qr = qrcode.QRCode(
        version=1,  # size of the QR code (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # pixel size of each box
        border=4,  # border size
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"[✅] QR Code saved as '{filename}'")


# ========== QR Code Decoder ==========
def decode_qr(filename):
    """
    Decode data from a QR code image.
    """
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()

    data, vertices, _ = detector.detectAndDecode(image)
    if data:
        print(f"[🔍] Decoded Data: {data}")
    else:
        print("[⚠️] No QR code detected in the image.")


# ========== Main Program ==========
if __name__ == "__main__":
    print("=== QR Code Generator and Decoder ===")
    user_data = input("Enter text or URL to encode: ")
    file_name = "my_qr.png"

    generate_qr(user_data, file_name)
    decode_qr(file_name)
