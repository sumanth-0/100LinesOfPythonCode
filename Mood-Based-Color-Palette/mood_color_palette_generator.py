import random

class MoodColorPaletteGenerator:
    def __init__(self):
        self.mood_colors = {
            "calm": ["#A4D7E1", "#B7E4E7", "#C9D6D5", "#F6F8E6", "#FFFAF0"],
            "happy": ["#FFDA77", "#FFAA33", "#FF5733", "#FFC300", "#FF8C00"],
            "energized": ["#FF007F", "#FF3D00", "#FF6F00", "#FF9E00", "#FFEB3B"],
            "sad": ["#3B3B58", "#757C9A", "#B0B2B3", "#A6B2D2", "#BDC3C7"],
            "romantic": ["#FFC0CB", "#FF69B4", "#FFB6C1", "#FF1493", "#DB7093"]
        }

    def generate_palette(self, mood):
        return self.mood_colors.get(mood.lower(), ["#FFFFFF"])  # Default to white if mood not found

def main():
    generator = MoodColorPaletteGenerator()
    mood = input("Enter your mood (calm, happy, energized, sad, romantic): ")
    palette = generator.generate_palette(mood)
    print(f"Color Palette for '{mood}':")
    for color in palette:
        print(color)

if __name__ == "__main__":
    main()
