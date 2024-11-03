import numpy as np

def is_arithmetic(sequence):
    """Check if the sequence is arithmetic."""
    difference = sequence[1] - sequence[0]
    return all(sequence[i] - sequence[i - 1] == difference for i in range(2, len(sequence))), difference

def is_geometric(sequence):
    """Check if the sequence is geometric."""
    ratio = sequence[1] / sequence[0] if sequence[0] != 0 else None
    return all(sequence[i] / sequence[i - 1] == ratio for i in range(2, len(sequence))), ratio

def is_power_pattern(sequence):
    """Check if the sequence follows a perfect power pattern for any integer power."""
    for power in range(2, 11):  # Check powers from 2 to 10
        expected_sequence = [i ** power for i in range(1, len(sequence) + 1)]
        if sequence == expected_sequence:
            return power  # Return the matching power
    return None

def find_next_number(sequence):
    # Check for arithmetic pattern
    arithmetic_check, arith_diff = is_arithmetic(sequence)
    if arithmetic_check:
        next_number = sequence[-1] + arith_diff
        explanation = f"This is an arithmetic sequence with a common difference of {arith_diff}."
        return next_number, explanation

    # Check for geometric pattern
    geometric_check, geo_ratio = is_geometric(sequence)
    if geometric_check:
        next_number = sequence[-1] * geo_ratio
        explanation = f"This is a geometric sequence with a common ratio of {geo_ratio}."
        return next_number, explanation

    # Check for perfect power patterns (1^n, 2^n, ...)
    power = is_power_pattern(sequence)
    if power is not None:
        next_number = (len(sequence) + 1) ** power  # Next power value
        explanation = f"This follows a perfect power pattern (power {power})."
        return next_number, explanation

    # Check for varying sum patterns
    for n in range(2, len(sequence) + 1):
        if all(sequence[i] == sum(sequence[i - n:i]) for i in range(n, len(sequence))):
            next_number = sum(sequence[-n:])  # Sum of the last n numbers
            explanation = f"This pattern is based on the sum of the last {n} terms."
            return next_number, explanation

    # For polynomial patterns, fit a polynomial
    degree = min(4, len(sequence) - 1)  # Limit degree to avoid overfitting
    coefficients = np.polyfit(range(len(sequence)), sequence, degree)
    polynomial = np.poly1d(coefficients)
    next_number = polynomial(len(sequence))
    explanation = f"This follows a polynomial pattern of degree {degree}."

    return next_number, explanation

def main():
    # Ask user for the first four numbers of the sequence
    user_input = input("Enter the first four numbers of the sequence separated by commas: ")
    sequence = list(map(float, user_input.split(',')))
    
    if len(sequence) < 4:
        print("Please enter at least four numbers.")
        return
    
    next_number, explanation = find_next_number(sequence)
    
    print(f"Next number in the sequence: {next_number:.2f}")
    print(f"Explanation: {explanation}")

if __name__ == "__main__":
    main()
0,
