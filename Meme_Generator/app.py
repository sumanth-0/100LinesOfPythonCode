from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Function to add text to the image and ensure it fits within the image size
def add_text_to_image(image_path, top_text, bottom_text='', font_path=None, initial_font_size=20):
    # Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Function to get font size that fits the text within the image width
    def get_fitting_font(draw, text, image_width, font_path, initial_font_size):
        font_size = initial_font_size
        font = ImageFont.truetype(font_path, font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]

        # Reduce the font size until the text fits within the image width
        while text_width > image_width - 20:  # Leave some padding
            font_size -= 1
            font = ImageFont.truetype(font_path, font_size)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
        
        return font

    # Check if the font is available, else use a default one
    if font_path is None or not os.path.exists(font_path):
        try:
            font_path = "arial.ttf"
            font = ImageFont.truetype(font_path, initial_font_size)
        except IOError:
            # Fallback font if Arial is not available
            font_path = None
            font = ImageFont.load_default()
    else:
        font = ImageFont.truetype(font_path, initial_font_size)

    # Text wrap function to handle long lines and resize the font if needed
    def draw_text(draw, text, position, font, max_width, color="white", stroke_width=2):
        wrapped_text = textwrap.fill(text, width=max_width)

        # Adjust the font size if the wrapped text doesn't fit
        font = get_fitting_font(draw, wrapped_text, image_width, font_path, initial_font_size)
        
        # Get text width and height
        bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        width, height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        x, y = position
        draw.text((x - width // 2, y), wrapped_text, font=font, fill=color, stroke_width=stroke_width, stroke_fill="black")

    # Set text positions and adjust max width for smaller images
    image_width, image_height = img.size
    max_text_width = max(10, image_width // (initial_font_size // 2))  # Tighter wrap for small images

    # Top text position with padding
    if top_text:
        draw_text(draw, top_text, position=(image_width // 2, 10), font=font, max_width=max_text_width)

    # Bottom text position with additional padding from bottom
    if bottom_text:
        bottom_text_y = image_height - initial_font_size * 2 - 15
        draw_text(draw, bottom_text, position=(image_width // 2, bottom_text_y), font=font, max_width=max_text_width)

    # Save or show the image with added text
    img.show()

# Main function to take user input
def generate_meme():
    image_path = input("Enter the path to the image: ")
    top_text = input("Enter the top text: ")
    bottom_text = input("Enter the bottom text (optional): ")
    font_path = input("Enter the path to the font (or press Enter to use default): ")

    # Generate the meme
    add_text_to_image(image_path, top_text, bottom_text, font_path if font_path else None)

# Run the generator
if __name__ == "__main__":
    generate_meme()
