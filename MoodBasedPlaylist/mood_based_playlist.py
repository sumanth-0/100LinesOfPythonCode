# mood_based_playlist.py

def suggest_playlist(mood):
    mood_playlist_map = {
        "happy": ["Pop", "Rock", "Dance"],
        "sad": ["R&B", "Soul", "Acoustic"],
        "angry": ["Metal", "Punk", "Hardcore"],
        "relaxed": ["Classical", "Jazz", "Ambient"],
        "focused": ["Instrumental", "Lo-fi", "Study Music"]
    }

    if mood in mood_playlist_map:
        return mood_playlist_map[mood]
    else:
        return "Try a more specific mood, like 'happy', 'sad', 'angry', 'relaxed', or 'focused'."

# Example usage:
user_mood = input("How are you feeling today? ")
suggested_playlists = suggest_playlist(user_mood.lower())
print("Suggested playlists:", suggested_playlists)
