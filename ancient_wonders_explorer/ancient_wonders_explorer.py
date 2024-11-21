# ancient_wonders_explorer.py

ANCIENT_WONDERS = {
    "Great Pyramid of Giza": {
        "Location": "Egypt",
        "History": "The oldest and only surviving wonder, built as a tomb for Pharaoh Khufu around 2560 BC.",
        "Image": "images/great_pyramid.jpg"
    },
    "Hanging Gardens of Babylon": {
        "Location": "Babylon (modern-day Iraq)",
        "History": "A terraced garden said to have been built by King Nebuchadnezzar II for his wife around 600 BC.",
        "Image": "images/hanging_gardens.jpg"
    },
    "Statue of Zeus at Olympia": {
        "Location": "Greece",
        "History": "A monumental statue of the god Zeus, created by the sculptor Phidias around 435 BC.",
        "Image": "images/statue_of_zeus.jpg"
    },
    "Temple of Artemis at Ephesus": {
        "Location": "Turkey",
        "History": "A grand temple dedicated to the goddess Artemis, rebuilt multiple times, with its final version completed in 550 BC.",
        "Image": "images/temple_of_artemis.jpg"
    },
    "Mausoleum at Halicarnassus": {
        "Location": "Turkey",
        "History": "A tomb built for Mausolus, a satrap of the Persian Empire, and his wife around 350 BC.",
        "Image": "images/mausoleum.jpg"
    },
    "Colossus of Rhodes": {
        "Location": "Greece",
        "History": "A giant bronze statue of the sun god Helios, erected around 280 BC and toppled by an earthquake 60 years later.",
        "Image": "images/colossus.jpg"
    },
    "Lighthouse of Alexandria": {
        "Location": "Egypt",
        "History": "A towering lighthouse on the island of Pharos, guiding sailors to the harbor of Alexandria around 280 BC.",
        "Image": "images/lighthouse.jpg"
    },
}

def display_wonders():
    """Display a list of ancient wonders."""
    print("\nExplore the Seven Wonders of the Ancient World!")
    for i, wonder in enumerate(ANCIENT_WONDERS.keys(), 1):
        print(f"[{i}] {wonder}")
    print("[0] Exit")

def show_details(wonder_name):
    """Display details about the selected wonder."""
    wonder = ANCIENT_WONDERS[wonder_name]
    print(f"\n{wonder_name}")
    print(f"Location: {wonder['Location']}")
    print(f"History: {wonder['History']}")
    print(f"Image: {wonder['Image']} (Pretend this displays the image!)")

def main():
    """Main function to run the explorer."""
    print("Welcome to the Ancient Wonders Explorer!")
    while True:
        display_wonders()
        choice = input("\nSelect a wonder to learn more (or 0 to exit): ").strip()

        if choice == "0":
            print("Thanks for exploring! Come back soon!")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(ANCIENT_WONDERS):
            selected_wonder = list(ANCIENT_WONDERS.keys())[int(choice) - 1]
            show_details(selected_wonder)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
