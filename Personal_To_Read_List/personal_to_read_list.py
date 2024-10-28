class Book:
    """Class to represent a book with title, author, notes, and rating."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.notes = ""
        self.rating = None

    def add_notes(self, notes):
        """Add notes for the book."""
        self.notes = notes

    def set_rating(self, rating):
        """Set a rating for the book."""
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            print("Rating must be between 1 and 5.")

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author} - Rating: {self.rating}/5\nNotes: {self.notes}"


class ToReadList:
    """Class to manage a personal to-read list."""
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        """Add a new book to the reading list."""
        self.books.append(Book(title, author))

    def show_list(self):
        """Display all books in the reading list."""
        if not self.books:
            print("Your reading list is empty.")
            return
        for idx, book in enumerate(self.books, 1):
            print(f"{idx}. {book}")

def main():
    """Main function to interact with the user."""
    to_read_list = ToReadList()
    
    while True:
        print("\n1. Add Book\n2. Show Reading List\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            to_read_list.add_book(title, author)
            notes = input("Enter any notes for this book: ")
            to_read_list.books[-1].add_notes(notes)
            rating = input("Rate the book (1-5): ")
            to_read_list.books[-1].set_rating(int(rating))
        
        elif choice == '2':
            to_read_list.show_list()
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
