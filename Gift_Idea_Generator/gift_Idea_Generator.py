# Gift_Idea_Generator.py

def get_gift_ideas(personality, budget):
    # Example gift ideas based on personality and budget
    gift_ideas = {
        "adventurous": {
            "low": "A portable hammock for camping trips.",
            "medium": "A hiking backpack with water-resistant features.",
            "high": "A weekend skydiving experience voucher."
        },
        "creative": {
            "low": "A set of high-quality sketching pencils.",
            "medium": "A pottery wheel for beginners.",
            "high": "An art retreat weekend with professional artists."
        },
        "techie": {
            "low": "A portable charger for their devices.",
            "medium": "A Bluetooth speaker with great sound quality.",
            "high": "A smart home assistant like Google Home or Alexa."
        },
        "bookworm": {
            "low": "A personalized leather bookmark.",
            "medium": "A book subscription service.",
            "high": "A first edition copy of their favorite novel."
        }
    }
    
    # Find the gift idea based on personality and budget
    if personality in gift_ideas:
        if budget in gift_ideas[personality]:
            return gift_ideas[personality][budget]
        else:
            return "Sorry, we don't have gift ideas for this budget range."
    else:
        return "Sorry, we don't have gift ideas for this personality."

def get_user_input():
    # Input personality and budget
    print("Select the recipient's personality:")
    print("1. Adventurous\n2. Creative\n3. Techie\n4. Bookworm")
    personality_choice = int(input("Enter choice (1-4): "))
    
    if personality_choice == 1:
        personality = "adventurous"
    elif personality_choice == 2:
        personality = "creative"
    elif personality_choice == 3:
        personality = "techie"
    elif personality_choice == 4:
        personality = "bookworm"
    else:
        print("Invalid choice! Defaulting to 'creative'.")
        personality = "creative"

    print("Select your budget range:")
    print("1. Low\n2. Medium\n3. High")
    budget_choice = int(input("Enter choice (1-3): "))
    
    if budget_choice == 1:
        budget = "low"
    elif budget_choice == 2:
        budget = "medium"
    elif budget_choice == 3:
        budget = "high"
    else:
        print("Invalid choice! Defaulting to 'medium'.")
        budget = "medium"
    
    return personality, budget

def main():
    personality, budget = get_user_input()
    gift_idea = get_gift_ideas(personality, budget)
    print(f"Suggested Gift Idea: {gift_idea}")

# Run the program
if __name__ == "__main__":
    main()
