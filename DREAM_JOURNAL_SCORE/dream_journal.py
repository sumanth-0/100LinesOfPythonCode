
class DreamJournal:
    def __init__(self):
        self.dreams = []

    def add_dream(self, dream, tags):
        self.dreams.append({'dream': dream, 'tags': tags})
        print("Dream added!")

    def search_dreams(self, keyword):
        print(f"\nDreams containing '{keyword}':")
        for entry in self.dreams:
            if keyword in entry['tags']:
                print(f"- {entry['dream']} (Tags: {', '.join(entry['tags'])})")

def main():
    journal = DreamJournal()
    print("Welcome to the Dream Journal!")

    while True:
        action = input("\nEnter 'add' to add a dream or 'search' to find dreams by tag (or 'quit' to exit): ").strip().lower()
        if action == 'add':
            dream = input("Describe your dream: ")
            tags = input("Enter keywords/tags (comma-separated): ").split(',')
            journal.add_dream(dream, [tag.strip() for tag in tags])
        elif action == 'search':
            keyword = input("Enter a keyword to search: ")
            journal.search_dreams(keyword)
        elif action == 'quit':
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
