import random

# Sample movie database
movies = {
    "happy": [
        "The Intouchables",
        "Zootopia",
        "Crazy Rich Asians",
        "The Grand Budapest Hotel",
        "Paddington"
    ],
    "sad": [
        "The Notebook",
        "A Star is Born",
        "Eternal Sunshine of the Spotless Mind",
        "The Pursuit of Happyness",
        "Me Before You"
    ],
    "motivational": [
        "The Pursuit of Happyness",
        "Rocky",
        "Remember the Titans",
        "Good Will Hunting",
        "Hidden Figures"
    ],
    "scary": [
        "The Conjuring",
        "A Quiet Place",
        "Get Out",
        "Hereditary",
        "It Follows"
    ],
    "adventurous": [
        "Inception",
        "Mad Max: Fury Road",
        "The Lord of the Rings: The Fellowship of the Ring",
        "Jurassic Park",
        "Indiana Jones: Raiders of the Lost Ark"
    ]
}

def recommend_movie(mood):
    """Suggest a movie based on the user's mood."""
    mood = mood.lower()
    if mood in movies:
        return random.choice(movies[mood])
    else:
        return "Mood not recognized. Please try happy, sad, motivational, scary, or adventurous."

def main():
    user_mood = input("How are you feeling today? (happy, sad, motivational, scary, adventurous): ")
    recommendation = recommend_movie(user_mood)
    print(f"Movie recommendation for you: {recommendation}")

if __name__ == "__main__":
    main()
