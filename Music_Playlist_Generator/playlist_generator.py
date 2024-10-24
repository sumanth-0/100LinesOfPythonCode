import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
from mutagen.easyid3 import EasyID3
# Function to extract metadata (artist/genre) from mp3 files
def get_music_metadata(file_path):
    try:
        audio = EasyID3(file_path)
        artist = audio.get('artist', ['Unknown Artist'])[0]
        genre = audio.get('genre', ['Unknown Genre'])[0]
        return artist, genre
    except Exception as e:
        return 'Unknown Artist', 'Unknown Genre'
# Function to shuffle and filter songs based on user input
def create_playlist(folder, filter_by=None, filter_value=None):
    songs = []
    # Read all mp3 files in the folder
    for filename in os.listdir(folder):
        if filename.endswith('.mp3'):
            file_path = os.path.join(folder, filename)
            artist, genre = get_music_metadata(file_path)
            songs.append({
                'filename': filename,
                'artist': artist,
                'genre': genre
            })
    if filter_by == 'artist':
        songs = [song for song in songs if filter_value.lower() in song['artist'].lower()]
    elif filter_by == 'genre':
        songs = [song for song in songs if filter_value.lower() in song['genre'].lower()]
    random.shuffle(songs)

    # Format the playlist with aligned song names and metadata
    playlist = ""
    for i, song in enumerate(songs, start=1):
        song_name = f"{i}. Song Name: {song['filename'].replace('-', ' ').title()}"
        artist_info = f"   Artist: {song['artist']}"
        genre_info = f"   Genre: {song['genre']}"
        playlist += f"{song_name}\n{artist_info}\n{genre_info}\n\n"
    if not playlist:
        playlist = "No songs found with the given filter."
    
    return playlist
# Function to handle the playlist creation and display it
def generate_playlist():
    folder = folder_var.get()
    filter_option = filter_var.get()
    filter_value = entry_filter.get()

    if not folder:
        messagebox.showerror("Error", "Please select a folder with music files!")
        return

    if filter_option == "None":
        filter_option = None
        filter_value = None
    playlist = create_playlist(folder, filter_option.lower(), filter_value)
    # Display the playlist in the text box with custom tag for indentation
    text_playlist.delete(1.0, tk.END)
    lines = playlist.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{i+1}. Song Name:"):
            text_playlist.insert(tk.END, line + '\n')
            text_playlist.tag_add(f"song_indent{i}", f"{i+1}.0", f"{i+1}.end")
            text_playlist.tag_config(f"song_indent{i}", lmargin2=30)  # Hanging indent for wrapped text
        elif line.strip().startswith("Artist:") or line.strip().startswith("Genre:"):
            text_playlist.insert(tk.END, line + '\n')
            text_playlist.tag_add(f"meta_indent{i}", f"{i+1}.0", f"{i+1}.end")
            text_playlist.tag_config(f"meta_indent{i}", lmargin1=10, lmargin2=10)  # Regular indent for metadata
        else:
            text_playlist.insert(tk.END, line + '\n')
def browse_folder(): # Function to browse and select folder
    folder_selected = filedialog.askdirectory(title="Select Folder with Music Files")
    if folder_selected:
        folder_var.set(folder_selected)
# Main window setup
root = tk.Tk()
root.title("Music Playlist Generator")
# Folder selection
folder_var = tk.StringVar()
tk.Label(root, text="Music Folder:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=folder_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_folder).grid(row=0, column=2, padx=10, pady=10)
# Filter selection
tk.Label(root, text="Filter by:").grid(row=1, column=0, padx=10, pady=10)
filter_var = tk.StringVar(value="None")
tk.OptionMenu(root, filter_var, "None", "Artist", "Genre").grid(row=1, column=1, padx=10, pady=10)
# Filter value input
tk.Label(root, text="Enter Artist/Genre (if applicable):").grid(row=2, column=0, padx=10, pady=10)
entry_filter = tk.Entry(root, width=50)
entry_filter.grid(row=2, column=1, padx=10, pady=10)
# Generate playlist button
tk.Button(root, text="Generate Playlist", command=generate_playlist).grid(row=3, column=1, padx=10, pady=20)
text_playlist = tk.Text(root, height=25, width=100, wrap=tk.WORD)
text_playlist.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
root.mainloop()