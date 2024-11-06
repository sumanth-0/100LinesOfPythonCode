import random

class MovieNight:
    def __init__(self):
        self.genres = {
            "comedy": ["The Mask", "Superbad", "The Grand Budapest Hotel"],
            "horror": ["A Quiet Place", "Hereditary", "The Conjuring"],
            "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
            "drama": ["The Godfather", "Forrest Gump", "The Shawshank Redemption"]
        }
        self.snacks = ["popcorn", "nachos", "chocolate", "fruit platter"]

    def suggest_movie(self, genre):
        return random.choice(self.genres.get(genre, ["Genre not available"]))

    def suggest_snack(self):
        return random.choice(self.snacks)

    def create_movie_night(self):
        genre = input("Choose a genre (comedy, horror, action, drama): ").lower()
        movie = self.suggest_movie(genre)
        snack = self.suggest_snack()
        return f"Tonight’s Movie: {movie}\nSnack Suggestion: {snack}"

def main():
    movie_night = MovieNight()
    plan = movie_night.create_movie_night()
    print("\nYour Personalized Movie Night Plan:")
    print(plan)

if __name__ == "__main__":
    main()
