from PIL import Image, ImageOps, ImageEnhance

def apply_filters(image_path):
    image = Image.open(image_path)

    # Black & White
    bw_image = ImageOps.grayscale(image)
    bw_image.show()

    # Sepia
    sepia_image = ImageOps.colorize(ImageOps.grayscale(image), '#704214', '#C0A080')
    sepia_image.show()

    # Invert Colors
    invert_image = ImageOps.invert(image.convert('RGB'))
    invert_image.show()

# Replace 'your_image.jpg' with the path to your image
apply_filters('your_image.jpg')
