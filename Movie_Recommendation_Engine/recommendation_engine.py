import random

def get_movie_recommendations(preference, genre_movies):
    """Return a list of recommended movies based on user preference."""
    return random.sample(genre_movies.get(preference, []), 3)

def main():
    print("Welcome to the Movie Recommendation Engine!")
    
    # Sample movie data
    genre_movies = {
        'Action': ['Mad Max: Fury Road', 'John Wick', 'Die Hard', 'The Dark Knight'],
        'Comedy': ['Superbad', 'Step Brothers', 'The Hangover', 'Groundhog Day'],
        'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'Fight Club', 'The Godfather'],
        'Horror': ['Get Out', 'A Quiet Place', 'The Shining', 'Hereditary'],
        'Sci-Fi': ['Inception', 'Interstellar', 'The Matrix', 'Blade Runner 2049']
    }

    preference = input("Enter your preferred genre (Action, Comedy, Drama, Horror, Sci-Fi): ")
    
    recommendations = get_movie_recommendations(preference.capitalize(), genre_movies)

    if recommendations:
        print(f"Here are some {preference} movie recommendations for you:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print("Sorry, we don't have recommendations for that genre.")

if __name__ == "__main__":
    main()
