import phonenumbers
from phonenumbers import geocoder

def get_phone_location(phone_number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number, None)
    
    # Get the country name
    country = geocoder.description_for_number(parsed_number, "en")
    
    return country

# Example usage
if __name__ == "__main__":
    phone_number = "+14155552671"  # Replace with the phone number you want to track
    location = get_phone_location(phone_number)
    print(f"The location of the phone number {phone_number} is: {location}")