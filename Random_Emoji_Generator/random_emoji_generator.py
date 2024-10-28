import random

class EmojiGenerator:
    """Class to generate random emojis."""
    def __init__(self):
        self.emojis = [
            '😀', '😂', '😍', '😎', '😢', '😡', '👍', '👎', '✨', '🎉',
            '🎈', '🌈', '🔥', '🍕', '🍣', '🍦', '🌍', '🚀', '⚡', '❤️',
            '🌼', '🍀', '🐶', '🐱', '🐰', '🐢', '🐳', '🐉', '🦄', '🎨'
        ]

    def generate_random_emoji(self):
        """Generate a random emoji."""
        return random.choice(self.emojis)

    def generate_random_combination(self, count):
        """Generate a random combination of emojis."""
        return ''.join(random.choices(self.emojis, k=count))


def main():
    """Run the random emoji generator."""
    emoji_generator = EmojiGenerator()
    
    print("Welcome to the Random Emoji Generator!")
    while True:
        try:
            choice = input("\nEnter '1' for a random emoji, '2' for a combination, or '0' to exit: ")
            if choice == '1':
                print("Random Emoji: ", emoji_generator.generate_random_emoji())
            elif choice == '2':
                count = int(input("How many emojis would you like to generate? "))
                print("Random Emoji Combination: ", emoji_generator.generate_random_combination(count))
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
