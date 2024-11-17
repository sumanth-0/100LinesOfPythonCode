import os
import random
from playsound import playsound

# Function to load bird songs from a directory
def load_bird_songs(directory):
    bird_songs = {}
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            bird_name = filename.replace(".mp3", "")
            bird_songs[bird_name] = os.path.join(directory, filename)
    return bird_songs

# Function to play a random bird song and ask user to identify the bird
def identify_bird(bird_songs):
    bird_name = random.choice(list(bird_songs.keys()))
    print("Listen carefully to the bird song!")
    playsound(bird_songs[bird_name])
    
    guess = input("Can you identify the bird from the song? Enter your guess: ").lower()
    
    if guess == bird_name.lower():
        print(f"Correct! It was a {bird_name}.")
    else:
        print(f"Oops! It was a {bird_name}. Try again next time.")

# Main function to load songs and start the game
def main():
    bird_songs = load_bird_songs("bird_songs")  # Directory containing .mp3 bird song files
    
    print("Welcome to the Birdsong Identifier!")
    while True:
        identify_bird(bird_songs)
        play_again = input("Would you like to identify another bird? (y/n): ").lower()
        if play_again != 'y':
            break

# Run the program
if __name__ == "__main__":
    main()
