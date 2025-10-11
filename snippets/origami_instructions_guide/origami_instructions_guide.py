#!/usr/bin/env python3
"""Origami Instructions Guide - Step-by-step folding instructions from preset selection"""

origami_library = {
    "1": {
        "name": "Traditional Crane",
        "difficulty": "Intermediate",
        "steps": [
            "Start with a square piece of paper, colored side down",
            "Fold in half diagonally both ways, then unfold",
            "Fold in half horizontally both ways, then unfold",
            "Bring the top three corners down to the bottom corner (waterbomb base)",
            "Fold the top triangular flaps into the center",
            "Fold the top down over the flaps",
            "Unfold the last two steps",
            "Petal fold: Lift the first layer up and fold the sides inward",
            "Flip and repeat the petal fold on the other side",
            "Fold both flaps up to create the legs",
            "Inside reverse fold one leg to make the head",
            "Fold down the wings and your crane is complete!"
        ]
    },
    "2": {
        "name": "Paper Boat",
        "difficulty": "Easy",
        "steps": [
            "Start with a rectangular piece of paper",
            "Fold the paper in half lengthwise",
            "Fold in half widthwise, then unfold",
            "Fold the top corners down to the center crease",
            "Fold the bottom edge up on both sides",
            "Open from the bottom and flatten into a square",
            "Fold the bottom corners up on both sides",
            "Open from the bottom and flatten again",
            "Gently pull the top corners apart",
            "Your boat is ready to sail!"
        ]
    },
    "3": {
        "name": "Jumping Frog",
        "difficulty": "Easy",
        "steps": [
            "Start with a square piece of paper",
            "Fold in half lengthwise, then unfold",
            "Fold the top corners down to the center line",
            "Fold the angled sides to the center",
            "Fold the bottom edge up to the base of the triangle",
            "Fold the bottom corners up and out",
            "Fold the bottom edge up again",
            "Fold in half, bringing the bottom to the back",
            "Fold the back layer down to create a step",
            "Press on the frog's back to make it jump!"
        ]
    },
    "4": {
        "name": "Simple Butterfly",
        "difficulty": "Easy",
        "steps": [
            "Start with a square piece of paper, colored side down",
            "Fold in half diagonally, then unfold",
            "Fold in half diagonally the other way",
            "Fold the top corner down to the bottom corner",
            "Fold a small triangle at the top down",
            "Flip the paper over",
            "Fold in half vertically, bringing the wings together",
            "Your butterfly is complete!"
        ]
    }
}

def display_menu():
    print("\n=== ORIGAMI INSTRUCTIONS GUIDE ===")
    print("\nAvailable Origami Designs:")
    for key, origami in origami_library.items():
        print(f"{key}. {origami['name']} - Difficulty: {origami['difficulty']}")
    print("0. Exit")

def display_instructions(origami_data):
    print(f"\n{'='*50}")
    print(f"{origami_data['name'].upper()}")
    print(f"Difficulty Level: {origami_data['difficulty']}")
    print(f"{'='*50}\n")
    for i, step in enumerate(origami_data['steps'], 1):
        print(f"Step {i}: {step}")
        input("\nPress Enter for next step..." if i < len(origami_data['steps']) else "\nPress Enter to return to menu...")

def main():
    while True:
        display_menu()
        choice = input("\nSelect an origami design (0-4): ").strip()
        if choice == "0":
            print("\nHappy folding! Goodbye!")
            break
        elif choice in origami_library:
            display_instructions(origami_library[choice])
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
