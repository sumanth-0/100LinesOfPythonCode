from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import random

# Predefined list of Instagram captions
captions = [
    "Living my best life 🌟",
    "Chasing dreams and catching sunsets 🌅",
    # Add more captions as needed
]

def generate_caption():
    return random.choice(captions)

def custom_caption_generator(theme):
    themed_captions = {
        'travel': [
            "Wander often, wonder always ✈️",
            "Adventure is out there! 🌎",
            "Let's find some beautiful place to get lost 🏞️",
        ],
        'self-love': [
            "You are enough just as you are 💕",
            "Self-love is the best love 💖",
            "Be your own kind of beautiful 🌸",
        ],
        'fitness': [
            "Stronger than yesterday 💪",
            "Push yourself because no one else is going to do it for you 🏋️",
            "Every workout counts! 🏃‍♀️",
        ]
    }
    
    return random.choice(themed_captions.get(theme, ["Sorry, I don't have captions for that theme."]))

def generate_image_caption(image_path):
    try:
        # Load the BLIP model and processor
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        
        image = Image.open(image_path)
        inputs = processor(image, return_tensors="pt")

        # Generate caption
        output = model.generate(**inputs)
        generated_caption = processor.decode(output[0], skip_special_tokens=True)
        
        return generated_caption.strip()
    except Exception as e:
        return f"Error processing the image: {e}"

def main():
    print("🌟 Welcome to the Instagram Captions Generator! 🌟")
    while True:
        print("\nChoose an option:")
        print("1. Generate a random caption")
        print("2. Generate a caption by theme")
        print("3. Generate a caption from an image")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            print("\nHere's your random caption: ", generate_caption())
        elif choice == '2':
            theme = input("What's the theme? (travel, self-love, fitness): ").strip().lower()
            print("\nYour themed caption: ", custom_caption_generator(theme))
        elif choice == '3':
            image_path = input("Please enter the path to your image: ").strip()
            caption = generate_image_caption(image_path)
            print("\nGenerated caption for your image: ", caption)
        elif choice == '4':
            print("Thanks for using the generator! Goodbye! 👋")
            break
        else:
            print("Hmm, that didn't seem like a valid choice. Please try again.")

if __name__ == "__main__":
    main()
