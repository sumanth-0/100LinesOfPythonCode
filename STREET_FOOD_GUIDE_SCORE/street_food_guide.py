
import json

def load_street_food_data():
    return {
        "Tacos": {
            "description": "Soft or hard tortilla filled with various ingredients.",
            "image": "url_to_tacos_image"
        },
        "Poutine": {
            "description": "French fries topped with cheese curds and gravy.",
            "image": "url_to_poutine_image"
        },
        "Banh Mi": {
            "description": "Vietnamese sandwich with meat, pickled vegetables, and herbs.",
            "image": "url_to_banh_mi_image"
        },
        "Arepas": {
            "description": "Cornmeal cakes filled with various ingredients, popular in Colombia and Venezuela.",
            "image": "url_to_arepas_image"
        },
        "Dumplings": {
            "description": "Dough filled with meat or vegetables, popular in many cultures.",
            "image": "url_to_dumplings_image"
        }
    }

def display_street_foods(food_data):
    for food, details in food_data.items():
        print(f"\n{food}:")
        print(f"Description: {details['description']}")
        print(f"Image: {details['image']}")

def main():
    print("Welcome to the Street Food Guide!")
    street_food_data = load_street_food_data()
    display_street_foods(street_food_data)

if __name__ == "__main__":
    main()
