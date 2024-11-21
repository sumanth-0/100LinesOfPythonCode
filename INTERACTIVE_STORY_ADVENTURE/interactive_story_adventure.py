# interactive_story_adventure.py

def display_scene(scene):
    """Display the current scene and choices."""
    print("\n" + scene["text"])
    for idx, choice in enumerate(scene["choices"], 1):
        print(f"{idx}. {choice['text']}")
    return scene["choices"]

def get_choice(choices):
    """Get the user's choice and validate input."""
    while True:
        try:
            user_input = int(input("Choose an option (enter the number): "))
            if 1 <= user_input <= len(choices):
                return choices[user_input - 1]["next"]
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    # Define the story
    story = {
        "start": {
            "text": "You wake up in a dense forest with no memory of how you got there. You see a path ahead.",
            "choices": [
                {"text": "Take the path to the left.", "next": "left_path"},
                {"text": "Take the path to the right.", "next": "right_path"}
            ]
        },
        "left_path": {
            "text": "You encounter a friendly deer. It seems to want you to follow it.",
            "choices": [
                {"text": "Follow the deer.", "next": "cabin"},
                {"text": "Ignore the deer and continue walking.", "next": "river"}
            ]
        },
        "right_path": {
            "text": "You find a mysterious box on the ground. It looks ancient.",
            "choices": [
                {"text": "Open the box.", "next": "trap"},
                {"text": "Leave the box and keep moving.", "next": "cave"}
            ]
        },
        "cabin": {
            "text": "The deer leads you to a hidden cabin filled with supplies. You rest and regain your strength. The End.",
            "choices": []
        },
        "river": {
            "text": "You reach a river but realize it's too wide to cross. You decide to return to the starting point. The End.",
            "choices": []
        },
        "trap": {
            "text": "The box was a trap! You find yourself locked in a cage. Game over.",
            "choices": []
        },
        "cave": {
            "text": "You discover a hidden cave with a treasure chest. You are rich! The End.",
            "choices": []
        }
    }

    print("Welcome to the Interactive Story Adventure!")
    current_scene = "start"

    while current_scene in story:
        scene = story[current_scene]
        choices = display_scene(scene)
        if not choices:  # End of the story
            print("Thank you for playing!")
            break
        current_scene = get_choice(choices)

if __name__ == "__main__":
    main()
