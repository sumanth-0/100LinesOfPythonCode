# Mad Libs Story Generator
# Fill in story templates with user-inputted nouns, verbs, adjectives.

import random

class MadLibsGenerator:
    """A class to generate Mad Libs stories with user input."""
    
    def __init__(self):
        """Initialize the Mad Libs generator with story templates."""
        self.story_templates = [
            {
                "title": "The Crazy Adventure",
                "template": "Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} in the {noun2}. "
                          "Every {noun3}, they would {verb2} {adverb1} with their {adjective2} {noun4}. "
                          "One day, they discovered a {adjective3} {noun5} that could {verb3}!",
                "words_needed": [
                    ("adjective1", "adjective"), ("noun1", "noun"), ("verb1", "verb"),
                    ("noun2", "place"), ("noun3", "time period"), ("verb2", "verb"),
                    ("adverb1", "adverb"), ("adjective2", "adjective"), ("noun4", "noun"),
                    ("adjective3", "adjective"), ("noun5", "object"), ("verb3", "verb")
                ]
            },
            {
                "title": "The Silly School Day",
                "template": "At {noun1} School, the students were {adjective1} because their teacher, Mr. {noun2}, "
                          "decided to {verb1} on the {noun3}. The {adjective2} principal came running {adverb1} "
                          "and shouted, '{exclamation}! Everyone must {verb2} to the {noun4} immediately!'",
                "words_needed": [
                    ("noun1", "adjective/name"), ("adjective1", "feeling"), ("noun2", "last name"),
                    ("verb1", "action"), ("noun3", "furniture"), ("adjective2", "adjective"),
                    ("adverb1", "adverb"), ("exclamation", "exclamation"), ("verb2", "verb"),
                    ("noun4", "place")
                ]
            },
            {
                "title": "The Magical Kitchen",
                "template": "In the {adjective1} kitchen, Chef {noun1} was {verb1} a {adjective2} {noun2}. "
                          "Suddenly, the {noun3} started to {verb2} {adverb1}! '{exclamation}!' cried the chef, "
                          "as {number} {adjective3} {noun4} came {verb3} out of the {noun5}.",
                "words_needed": [
                    ("adjective1", "adjective"), ("noun1", "name"), ("verb1", "cooking verb"),
                    ("adjective2", "adjective"), ("noun2", "food"), ("noun3", "kitchen item"),
                    ("verb2", "action"), ("adverb1", "adverb"), ("exclamation", "exclamation"),
                    ("number", "number"), ("adjective3", "adjective"), ("noun4", "plural noun"),
                    ("verb3", "action"), ("noun5", "container")
                ]
            }
        ]
    
    def get_user_input(self, word_type, description):
        """Get user input for a specific word type."""
        prompt = f"Enter a {description}: "
        return input(prompt).strip()
    
    def collect_words(self, template):
        """Collect all required words from the user for a template."""
        print(f"\n📝 Let's create: {template['title']}")
        print("=" * 40)
        
        words = {}
        for word_key, word_type in template['words_needed']:
            words[word_key] = self.get_user_input(word_key, word_type)
        
        return words
    
    def generate_story(self, template, words):
        """Generate the final story by filling in the template."""
        story = template['template'].format(**words)
        return story
    
    def display_story(self, title, story):
        """Display the completed story in a nice format."""
        print("\n" + "🎉" * 20)
        print(f"📖 {title}")
        print("🎉" * 20)
        print(f"\n{story}\n")
        print("🎉" * 20)
    
    def play_game(self):
        """Main game loop."""
        print("🎭 Welcome to the Mad Libs Story Generator! 🎭")
        print("Create hilarious stories by filling in the blanks!")
        
        while True:
            print(f"\n📚 Available story templates:")
            for i, template in enumerate(self.story_templates, 1):
                print(f"{i}. {template['title']}")
            
            try:
                choice = input(f"\nChoose a story (1-{len(self.story_templates)}) or 'q' to quit: ").strip()
                
                if choice.lower() == 'q':
                    print("👋 Thanks for playing Mad Libs! Goodbye!")
                    break
                
                choice_num = int(choice) - 1
                if 0 <= choice_num < len(self.story_templates):
                    template = self.story_templates[choice_num]
                    words = self.collect_words(template)
                    story = self.generate_story(template, words)
                    self.display_story(template['title'], story)
                    
                    play_again = input("\n🔄 Would you like to create another story? (y/n): ").strip().lower()
                    if play_again != 'y':
                        print("👋 Thanks for playing Mad Libs! Goodbye!")
                        break
                else:
                    print("❌ Invalid choice. Please try again.")
                    
            except ValueError:
                print("❌ Please enter a valid number or 'q' to quit.")
            except KeyboardInterrupt:
                print("\n👋 Thanks for playing Mad Libs! Goodbye!")
                break

def main():
    """Main function to run the Mad Libs generator."""
    game = MadLibsGenerator()
    game.play_game()

if __name__ == "__main__":
    main()
