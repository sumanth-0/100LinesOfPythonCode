import qrcode
import cv2

def generate_qr_code(data):
    """Generate a QR code from the provided data."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    print("QR Code generated and saved as 'qr_code.png'.")

def scan_qr_code():
    """Scan and decode a QR code from the webcam."""
    cap = cv2.VideoCapture(0)
    print("Scanning for QR Code. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        detector = cv2.QRCodeDetector()
        data, bbox, _ = detector(frame)
        
        if bbox is not None:
            cv2.polylines(frame, [np.int32(bbox)], True, (0, 255, 0), 3)
            if data:
                print(f"Decoded data: {data}")
        
        cv2.imshow("QR Code Scanner", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    choice = input("Would you like to (1) Generate QR Code or (2) Scan QR Code? (Enter 1 or 2): ")
    if choice == '1':
        data = input("Enter the text or URL to encode in the QR code: ")
        generate_qr_code(data)
    elif choice == '2':
        scan_qr_code()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
