from PIL import Image, ImageDraw, ImageFont

def draw_flower(draw, position, size, color):
    """Draw a simple flower shape at the given position."""
    # Draw the petals as circles
    petal_radius = size // 3
    petals = [
        (position[0], position[1] - petal_radius),  # Top
        (position[0], position[1] + petal_radius),  # Bottom
        (position[0] - petal_radius, position[1]),  # Left
        (position[0] + petal_radius, position[1]),  # Right
        (position[0] - petal_radius // 1.5, position[1] - petal_radius // 1.5),  # Top-left
        (position[0] + petal_radius // 1.5, position[1] - petal_radius // 1.5),  # Top-right
        (position[0] - petal_radius // 1.5, position[1] + petal_radius // 1.5),  # Bottom-left
        (position[0] + petal_radius // 1.5, position[1] + petal_radius // 1.5)   # Bottom-right
    ]

    for petal in petals:
        draw.ellipse((petal[0] - petal_radius, petal[1] - petal_radius,
                       petal[0] + petal_radius, petal[1] + petal_radius), fill=color)

    # Draw the center of the flower
    draw.ellipse((position[0] - petal_radius // 1.5, position[1] - petal_radius // 1.5,
                   position[0] + petal_radius // 1.5, position[1] + petal_radius // 1.5), fill='yellow')


def create_greeting_card(header, message, output_path, card_color, text_color, border_color, border_width, card_size=(800, 600)):
    # Create a new image for the card
    card = Image.new('RGB', card_size, card_color)
    draw = ImageDraw.Draw(card)

    # Draw a border around the card
    draw.rectangle([0, 0, card_size[0], card_size[1]], outline=border_color, width=border_width)

    # Load fonts with larger sizes
    font_header = ImageFont.truetype("arial.ttf", 48)  # Header font (48 pt)
    font_message = ImageFont.truetype("arial.ttf", 32)  # Message font (32 pt)

    # Calculate text size for centering
    header_size = draw.textbbox((0, 0), header, font=font_header)[2:4]
    message_size = draw.textbbox((0, 0), message, font=font_message)[2:4]

    # Center the header
    header_x = (card_size[0] - header_size[0]) // 2
    header_y = 20  # Space from the top
    draw.text((header_x, header_y), header, fill=text_color, font=font_header)

    # Center the message
    message_x = (card_size[0] - message_size[0]) // 2
    message_y = header_y + header_size[1] + 20  # Space below the header
    draw.text((message_x, message_y), message, fill=text_color, font=font_message)

    # Draw flowers in each corner
    flower_color = 'pink'  # Color of the flower petals
    flower_size = 30       # Size of the flower
    draw_flower(draw, (30, 30), flower_size, flower_color)  # Top-left
    draw_flower(draw, (card_size[0] - 30, 30), flower_size, flower_color)  # Top-right
    draw_flower(draw, (30, card_size[1] - 30), flower_size, flower_color)  # Bottom-left
    draw_flower(draw, (card_size[0] - 30, card_size[1] - 30), flower_size, flower_color)  # Bottom-right

    # Save the card
    card.save(output_path)
    print(f"Greeting card saved to {output_path}")

def main():
    print("Welcome to the Enhanced Greeting Card Creator!")

    # Gather dynamic input from the user
    header = input("Enter the greeting card header (e.g., 'Happy Birthday!'): ")
    message = input("Enter your greeting message: ")
    output_path = input("Enter the output file name (e.g., 'greeting_card.png'): ")
    
    # Get card color from the user
    card_color_input = input("Enter card color as R,G,B (e.g., 255,255,255 for white): ")
    card_color = tuple(map(int, card_color_input.split(',')))

    # Get text color from the user
    text_color_input = input("Enter text color as R,G,B (e.g., 0,0,0 for black): ")
    text_color = tuple(map(int, text_color_input.split(',')))

    # Get border color and width from the user
    border_color_input = input("Enter border color as R,G,B (e.g., 0,0,0 for black): ")
    border_color = tuple(map(int, border_color_input.split(',')))
    border_width = int(input("Enter border width (e.g., 5): "))

    # Create the greeting card
    create_greeting_card(header, message, output_path, card_color, text_color, border_color, border_width)

if __name__ == "__main__":
    main()
