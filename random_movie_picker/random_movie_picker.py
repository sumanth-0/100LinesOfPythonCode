#!/usr/bin/env python3
"""
Random Movie Picker
Randomly selects a movie from a list to watch.
"""

import random
import sys
import os


def load_movies_from_file(filename):
    """
    Load movies from a text file (one movie per line).
    Returns a list of movie names.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            movies = [line.strip() for line in f if line.strip()]
        return movies
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


def get_default_movies():
    """
    Returns a default list of popular movies.
    """
    return [
        "The Shawshank Redemption",
        "The Godfather",
        "The Dark Knight",
        "Pulp Fiction",
        "Forrest Gump",
        "Inception",
        "The Matrix",
        "Interstellar",
        "Goodfellas",
        "The Silence of the Lambs",
        "Saving Private Ryan",
        "The Green Mile",
        "Parasite",
        "Spirited Away",
        "The Prestige"
    ]


def pick_random_movie(movies):
    """
    Randomly select and return a movie from the list.
    """
    if not movies:
        return None
    return random.choice(movies)


def main():
    print("\n🎬 Random Movie Picker 🍿\n")
    
    movies = []
    
    # Check if a file was provided as argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print(f"📁 Loading movies from '{filename}'...\n")
        movies = load_movies_from_file(filename)
        if movies is None:
            sys.exit(1)
    else:
        # Use default movie list
        print("📝 Using default movie list...\n")
        movies = get_default_movies()
    
    if not movies:
        print("❌ No movies available to pick from!")
        sys.exit(1)
    
    print(f"🎯 Total movies available: {len(movies)}\n")
    
    # Pick a random movie
    selected_movie = pick_random_movie(movies)
    
    print("="*50)
    print(f"\n🌟 Tonight's movie suggestion: {selected_movie} 🌟\n")
    print("="*50)
    print("\n🍿 Enjoy your movie! 🎬\n")


if __name__ == "__main__":
    main()
