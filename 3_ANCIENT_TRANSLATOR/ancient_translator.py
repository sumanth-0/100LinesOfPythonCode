from PIL import Image, ImageDraw, ImageFont

class AncientTranslator:
    def __init__(self, text, script="hieroglyphs"):
        self.text = text
        self.script = script

    def translate_to_script(self):
        if self.script == "hieroglyphs":
            return ''.join(['\u1300' for _ in self.text])  # Mock glyphs for demonstration
        elif self.script == "cuneiform":
            return ''.join(['\u1240' for _ in self.text])  # Mock glyphs for demonstration
        elif self.script == "runes":
            return ''.join(['᛫' for _ in self.text])  # Mock runes for demonstration
        else:
            return "Translation not available for this script."

    def save_translation_image(self):
        translated_text = self.translate_to_script()
        img = Image.new('RGB', (600, 100), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        d.text((10, 10), translated_text, fill=(0, 0, 0), font=font)
        img.save("translation.png")
        print("Translation image saved as 'translation.png'")

if __name__ == "__main__":
    text = input("Enter text to translate: ")
    script = input("Choose script (hieroglyphs, cuneiform, runes): ")
    translator = AncientTranslator(text, script)
    translator.save_translation_image()
