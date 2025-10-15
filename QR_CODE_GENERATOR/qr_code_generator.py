"""
QR Code Generator - Generates QR codes for any URL or text input
Features: Multiple styles, error correction levels, and custom colors
"""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
import os
from datetime import datetime

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def print_banner():
    print("=" * 60 + "\n" + " " * 18 + "QR CODE GENERATOR\n" + "=" * 60 + "\n")

def get_user_input():
    print("Enter the text or URL you want to encode:")
    data = input("> ").strip()
    return data if data else None

def get_customization_options():
    print("\n--- Customization Options ---")
    print("\nError Correction: 1=Low(7%) 2=Medium(15%) 3=Quartile(25%) 4=High(30%)")
    error_levels = {'1': qrcode.constants.ERROR_CORRECT_L, '2': qrcode.constants.ERROR_CORRECT_M,
                   '3': qrcode.constants.ERROR_CORRECT_Q, '4': qrcode.constants.ERROR_CORRECT_H}
    choice = input("Choose (1-4) [2]: ").strip() or '2'
    error_correction = error_levels.get(choice, qrcode.constants.ERROR_CORRECT_M)
    
    print("\nStyle: 1=Square 2=Rounded 3=Circle")
    styles = {'1': SquareModuleDrawer(), '2': RoundedModuleDrawer(), '3': CircleModuleDrawer()}
    style_choice = input("Choose (1-3) [1]: ").strip() or '1'
    module_drawer = styles.get(style_choice, SquareModuleDrawer())
    
    print("\nColors (hex format):")
    fg_color = input("Foreground [#000000]: ").strip() or "#000000"
    bg_color = input("Background [#FFFFFF]: ").strip() or "#FFFFFF"
    
    return error_correction, module_drawer, fg_color, bg_color

def generate_qr_code(data, error_correction, module_drawer, fg_color, bg_color):
    qr = qrcode.QRCode(version=1, error_correction=error_correction, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=module_drawer,
                        color_mask=SolidFillColorMask(front_color=hex_to_rgb(fg_color), 
                                                      back_color=hex_to_rgb(bg_color)))
    return img

def save_qr_code(img, data):
    output_dir = "generated_qr_codes"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(output_dir, f"qr_code_{timestamp}.png")
    img.save(filepath)
    print(f"\n✓ QR Code successfully generated!\n✓ Saved to: {filepath}")
    print(f"✓ Data: {data[:50]}{'...' if len(data) > 50 else ''}")
    return filepath

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        
        data = get_user_input()
        if not data:
            print("⚠ Error: Input cannot be empty!")
            input("\nPress Enter to continue...")
            continue
        
        error_correction, module_drawer, fg_color, bg_color = get_customization_options()
        print("\nGenerating QR code...")
        try:
            img = generate_qr_code(data, error_correction, module_drawer, fg_color, bg_color)
            save_qr_code(img, data)
        except Exception as e:
            print(f"\n⚠ Error: {e}")
        
        print("\n" + "-" * 60)
        if input("\nGenerate another? (y/n): ").strip().lower() != 'y':
            print("\nThank you for using QR Code Generator! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
