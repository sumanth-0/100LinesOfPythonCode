# personal_hobby_finder.py

def get_hobby_recommendation(interests, time_availability, energy_level):
    """Recommend hobbies based on user preferences."""
    hobby_categories = {
        "artistic": ["Painting", "Sketching", "Pottery"],
        "active": ["Hiking", "Cycling", "Dancing"],
        "relaxing": ["Reading", "Gardening", "Knitting"],
        "adventurous": ["Rock Climbing", "Scuba Diving", "Skydiving"],
        "intellectual": ["Chess", "Coding", "Learning a new language"]
    }

    if "creative" in interests:
        return hobby_categories["artistic"]
    elif energy_level == "high" and time_availability > 1:
        return hobby_categories["active"] + hobby_categories["adventurous"]
    elif energy_level == "low" or time_availability <= 1:
        return hobby_categories["relaxing"]
    else:
        return hobby_categories["intellectual"]

def take_quiz():
    print("Welcome to the Personal Hobby Finder Quiz!")
    print("Answer the following questions to discover a new hobby:")
    
    interests = input("What are your interests? (e.g., creative, physical, intellectual): ").lower()
    time_availability = int(input("How many hours per week can you dedicate to a hobby? "))
    energy_level = input("Do you prefer high-energy or low-energy activities? (high/low): ").lower()

    recommended_hobbies = get_hobby_recommendation(interests, time_availability, energy_level)
    print("\nBased on your preferences, here are some hobbies you might enjoy:")
    for hobby in recommended_hobbies:
        print(f"- {hobby}")

def main():
    while True:
        take_quiz()
        retry = input("\nWould you like to take the quiz again? (yes/no): ").lower()
        if retry != "yes":
            print("Thanks for using the Personal Hobby Finder! Enjoy your new hobbies!")
            break

if __name__ == "__main__":
    main()
