def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to n terms.

    The Fibonacci sequence is a series of numbers where each number is the sum
    of the two preceding ones, usually starting with 0 and 1.

    Args:
        n (int): The number of terms to generate in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to n terms.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)
        return sequence

if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if num_terms < 0:
            print("Please enter a non-negative integer.")
        else:
            fib_sequence = fibonacci_sequence(num_terms)
            print("Fibonacci sequence:")
            for num in fib_sequence:
                print(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")