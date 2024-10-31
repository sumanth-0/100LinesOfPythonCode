
class ChordFinder:
    def __init__(self):
        self.chord_progressions = {
            "C": ["C", "Dm", "Em", "F", "G", "Am"],
            "D": ["D", "Em", "F#m", "G", "A", "Bm"],
            "E": ["E", "F#m", "G#m", "A", "B", "C#m"],
            "G": ["G", "Am", "Bm", "C", "D", "Em"],
            "A": ["A", "Bm", "C#m", "D", "E", "F#m"]
        }

    def find_chords(self, root_note):
        return self.chord_progressions.get(root_note.upper(), "Invalid root note. Please enter C, D, E, G, or A.")

def main():
    finder = ChordFinder()
    root_note = input("Enter the root note (C, D, E, G, A): ")
    chords = finder.find_chords(root_note)
    print(f"Suggested chords for {root_note}: {chords}")

if __name__ == "__main__":
    main()
