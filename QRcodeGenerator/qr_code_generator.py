import qrcode
from PIL import Image
import numpy as np

def create_qr_with_logo(data, logo_path, output_path, box_size=10, border=4):
    """
    Create a QR code with a logo in the center.
    
    :param data: The data to encode in the QR code
    :param logo_path: Path to the logo image file
    :param output_path: Path to save the final QR code
    :param box_size: Size of each box in the QR code
    :param border: Border size of the QR code
    """
    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR Code
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Open the logo image
    logo = Image.open(logo_path)
    
    # Calculate the maximum size for the logo (e.g., 20% of the QR code size)
    logo_max_size = int(qr_image.size[0] * 0.2)
    logo.thumbnail((logo_max_size, logo_max_size))
    
    # Calculate position to paste the logo (center of QR code)
    qr_width, qr_height = qr_image.size
    logo_width, logo_height = logo.size
    logo_pos = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)
    
    # Create a mask for the logo (this will make the logo's background transparent)
    mask = Image.new('L', logo.size, 255)
    
    # Paste the logo onto the QR code
    qr_image.paste(logo, logo_pos, mask)
    
    # Save the final image
    qr_image.save(output_path)
    print(f"QR code with logo saved to {output_path}")

def create_animated_qr(data, frames_folder, output_path, duration=500, loop=0):
    """
    Create an animated QR code from a series of images.
    
    :param data: The data to encode in the QR code
    :param frames_folder: Folder containing the frame images
    :param output_path: Path to save the final animated QR code
    :param duration: Duration of each frame in milliseconds
    :param loop: Number of times to loop the animation (0 for infinite)
    """
    import os
    
    # Generate base QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    # Get list of frame images
    frames = [Image.open(os.path.join(frames_folder, f)) for f in sorted(os.listdir(frames_folder))]
    
    # Resize frames to fit in the center of the QR code
    frame_size = int(qr_image.size[0] * 0.3)
    frames = [f.resize((frame_size, frame_size)) for f in frames]
    
    # Create QR codes with each frame
    qr_frames = []
    for frame in frames:
        qr_with_frame = qr_image.copy()
        position = ((qr_image.size[0] - frame.size[0]) // 2,
                    (qr_image.size[1] - frame.size[1]) // 2)
        qr_with_frame.paste(frame, position)
        qr_frames.append(qr_with_frame)
    
    # Save as animated GIF
    qr_frames[0].save(output_path, save_all=True, append_images=qr_frames[1:],
                      duration=duration, loop=loop)
    print(f"Animated QR code saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Create a QR code with a logo
    create_qr_with_logo("https://example.com", "logo.png", "qr_with_logo.png")
    
    # Create an animated QR code
    create_animated_qr("https://example.com", "animation_frames", "animated_qr.gif")

