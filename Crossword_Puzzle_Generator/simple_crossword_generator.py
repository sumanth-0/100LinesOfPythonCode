import random

# Sample words and clues
words_and_clues = {
    "PYTHON": "A type of programming language.",
    "JAVA": "A popular high-level programming language.",
    "HTML": "The standard markup language for creating web pages.",
    "CSS": "Style sheet language used for describing the presentation of a document.",
    "CODE": "A set of instructions for a computer.",
}

def generate_crossword(words_and_clues):
    """Generate a simple crossword puzzle."""
    size = 10
    grid = [[" " for _ in range(size)] for _ in range(size)]

    for word in words_and_clues.keys():
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical'])
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)

            if direction == 'horizontal' and col + len(word) <= size:
                if all(grid[row][col + i] in [" ", word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                    placed = True
            elif direction == 'vertical' and row + len(word) <= size:
                if all(grid[row + i][col] in [" ", word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                    placed = True

    return grid

def print_crossword(grid):
    """Print the crossword grid."""
    for row in grid:
        print(" | ".join(row))
    print("\nClues:")
    for word, clue in words_and_clues.items():
        print(f"{word}: {clue}")

def main():
    """Main function to run the crossword generator."""
    crossword_grid = generate_crossword(words_and_clues)
    print_crossword(crossword_grid)

if __name__ == "__main__":
    main()
