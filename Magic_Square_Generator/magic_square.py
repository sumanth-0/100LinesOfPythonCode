def generate_magic_square(n):
    """Generates a magic square of odd size `n` using the Siamese method."""
    if n % 2 == 0:
        raise ValueError("Magic square generation only works for odd values of `n`.")

    # Initialize the n x n magic square with zeros
    magic_square = [[0] * n for _ in range(n)]
    # Starting position for 1
    row, col = 0, n // 2

    for num in range(1, n * n + 1):
        # Place the current number
        magic_square[row][col] = num 
        # Compute the next position
        next_row, next_col = (row - 1) % n, (col + 1) % n
        # Check if the next cell is already filled
        if magic_square[next_row][next_col]:
            # Move down one row from the current position
            row = (row + 1) % n
        else:
            # Move to the calculated position
            row, col = next_row, next_col

    return magic_square

def print_magic_square(magic_square):
    """Prints the magic square in a formatted way."""
    n = len(magic_square)
    print(f"Magic Square (Size {n}x{n}) - Magic Constant: {n * (n * n + 1) // 2}\n")
    for row in magic_square:
        print(" ".join(f"{num:3}" for num in row))

# Get user input
def get_odd_size():
    while True:
        try:
            size = int(input("Enter an odd number for the size of the magic square: "))
            if size % 2 == 1:
                return size
            else:
                print("Please enter an odd number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    size = get_odd_size()
    magic_square = generate_magic_square(size)
    print_magic_square(magic_square)
