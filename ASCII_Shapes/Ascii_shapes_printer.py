def print_triangle(size=5, repeat=3):
    """Print a triangle shape repeated horizontally."""
    for _ in range(repeat):
        for i in range(size):
            print(' ' * (size - i - 1) + '*' * (2 * i + 1))
        print()  # Space between repeats

def print_square(size=5, repeat=3):
    """Print a square shape repeated horizontally."""
    for _ in range(repeat):
        for i in range(size):
            print('*' * size)
        print()  # Space between repeats

def print_diamond(size=5, repeat=2):
    """Print a diamond shape repeated."""
    for rep in range(repeat):
        for i in range(size):
            print(' ' * (size - i - 1) + '*' * (2 * i + 1))
        for i in range(size - 2, -1, -1):
            print(' ' * (size - i - 1) + '*' * (2 * i + 1))
        print()  # Space between repeats

def main():
    print("ASCII Geometric Shapes Printer")
    choice = input("Choose shape (t= triangle, s= square, d= diamond): ").strip().lower()
    try:
        repeat = int(input("Number of repeats (default 3): ").strip() or "3")
    except ValueError:
        repeat = 3
    
    if choice == 't':
        print_triangle(repeat=repeat)
    elif choice == 's':
        print_square(repeat=repeat)
    elif choice == 'd':
        print_diamond(repeat=repeat)
    else:
        print("Invalid choice. Printing default triangle.")
        print_triangle(repeat=repeat)

if __name__ == "__main__":
    main()
