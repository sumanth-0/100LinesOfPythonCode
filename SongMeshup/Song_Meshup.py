import random

# Sample song lyrics lines (hardcoded for demo; expand as needed)
SONGS = {
    "Bohemian Rhapsody": [
        "Is this the real life? Is this just fantasy?",
        "Caught in a landslide, no escape from reality.",
        "Open your eyes, look up to the skies and see.",
        "I'm just a poor boy, I need no sympathy.",
        "Because I'm easy come, easy go, little high, little low.",
        "Any way the wind blows doesn't really matter to me, to me.",
        "Mama, just killed a man, put a gun against his head.",
        "Pulled my trigger, now he's dead.",
        "Mama, life had just begun, but now I've gone and thrown it all away."
    ],
    "Hotel California": [
        "On a dark desert highway, cool wind in my hair.",
        "Warm smell of colitas rising up through the air.",
        "Up ahead in the distance, I saw a shimmering light.",
        "My head grew heavy and my sight grew dim, I had to stop for the night.",
        "There she stood in the doorway; I heard the mission bell.",
        "And I was thinking to myself, 'This could be Heaven or this could be Hell'.",
        "Then she lit up a candle and she showed me the way.",
        "There were voices down the corridor, I thought I heard them say..."
    ],
    "Stairway to Heaven": [
        "There's a lady who's sure all that glitters is gold.",
        "And she's buying a stairway to Heaven.",
        "When she gets there she knows, if the stores are all closed.",
        "With a word she can get what she came for.",
        "Ooh, ooh, and she's buying a stairway to Heaven.",
        "There's a sign on the wall, but she wants to be sure.",
        "'Cause you know sometimes words have two meanings.",
        "In a tree by the brook, there's a songbird who sings,"
    ],
    "Imagine": [
        "Imagine there's no heaven, it's easy if you try.",
        "No hell below us, above us only sky.",
        "Imagine all the people living for today.",
        "Imagine there's no countries, it isn't hard to do.",
        "Nothing to kill or die for, and no religion too.",
        "Imagine all the people living life in peace.",
        "You may say I'm a dreamer, but I'm not the only one.",
        "I hope someday you'll join us, and the world will be as one."
    ]
}

def generate_mashup(num_lines=8, num_songs=None):
    """Generate a random mashup by combining lines from songs."""
    if num_songs is None:
        num_songs = len(SONGS)
    selected_songs = random.sample(list(SONGS.keys()), min(num_songs, len(SONGS)))
    mashup = []
    
    for _ in range(num_lines):
        song = random.choice(selected_songs)
        line = random.choice(SONGS[song])
        mashup.append(f"[{song}] {line}")
    
    return mashup

def main():
    print("Song Lyrics Mashup Generator")
    try:
        num_lines = int(input("Number of lines in mashup (default 8): ").strip() or "8")
    except ValueError:
        num_lines = 8
    
    try:
        num_songs_input = input("Number of songs to use (default all): ").strip()
        num_songs = int(num_songs_input) if num_songs_input else None
    except ValueError:
        num_songs = None
    
    mashup = generate_mashup(num_lines, num_songs)
    print("\n--- Your Random Mashup ---\n")
    for line in mashup:
        print(line)
    print("\n--- End Mashup ---")

if __name__ == "__main__":
    main()
