from PIL import Image, ImageEnhance, ImageOps
import os

class VintagePhotoFilter:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def apply_sepia(self):
        sepia_image = ImageOps.colorize(self.image.convert("L"), "#704214", "#C0C080")
        return sepia_image

    def add_grain(self, img, intensity=10):
        noise = Image.effect_noise(img.size, intensity)
        grainy_image = Image.blend(img.convert("RGB"), noise.convert("RGB"), 0.3)
        return grainy_image

    def adjust_fade(self, img, brightness=0.8, contrast=0.8):
        enhancer_bright = ImageEnhance.Brightness(img)
        faded_image = enhancer_bright.enhance(brightness)
        enhancer_contrast = ImageEnhance.Contrast(faded_image)
        return enhancer_contrast.enhance(contrast)

    def apply_vintage_filter(self, output_path):
        sepia_img = self.apply_sepia()
        grainy_img = self.add_grain(sepia_img)
        final_image = self.adjust_fade(grainy_img)
        final_image.save(output_path)
        print(f"Vintage filter applied and saved to {output_path}")

if __name__ == "__main__":
    input_path = input("Enter the path of the image: ").strip()
    output_path = "vintage_" + os.path.basename(input_path)
    filter_app = VintagePhotoFilter(input_path)
    filter_app.apply_vintage_filter(output_path)
