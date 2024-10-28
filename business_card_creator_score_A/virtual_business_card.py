import json
import qrcode

def create_card():
    """Create a virtual business card."""
    name = input("Enter your name: ")
    title = input("Enter your title: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    website = input("Enter your website URL: ")

    card = {
        'name': name,
        'title': title,
        'email': email,
        'phone': phone,
        'website': website
    }

    return card

def save_card(card, filename):
    """Save the business card to a file."""
    with open(filename, 'w') as file:
        json.dump(card, file)
    print("Business card saved successfully!")

def load_card(filename):
    """Load the business card from a file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def generate_qr_code(data):
    """Generate a QR code from the provided data."""
    img = qrcode.make(data)
    img.save('business_card_qr.png')
    print("QR code generated successfully!")

def main():
    """Main function to create and save a virtual business card."""
    card = create_card()
    filename = 'business_card.json'
    save_card(card, filename)
    generate_qr_code(json.dumps(card))

if __name__ == "__main__":
    main()
