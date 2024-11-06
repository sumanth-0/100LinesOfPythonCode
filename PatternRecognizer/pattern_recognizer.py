import numpy as np

def recognize_pattern(sequence):
    diffs = np.diff(sequence)
    
    # Check for arithmetic sequence
    if np.all(np.isclose(diffs, diffs[0])):
        return "Arithmetic sequence", diffs[0]

    # Check for geometric sequence
    ratios = sequence[1:] / sequence[:-1]
    if np.all(np.isclose(ratios, ratios[0])):
        return "Geometric sequence", ratios[0]

    # Check for Fibonacci sequence
    if len(sequence) >= 3:
        for i in range(2, len(sequence)):
            if sequence[i] != sequence[i-1] + sequence[i-2]:
                break
        else:
            return "Fibonacci sequence"

    # Other patterns or no pattern recognized
    return "Unknown pattern"

# Example usage:
sequence = [1, 3, 5, 7, 9]
pattern, value = recognize_pattern(sequence)
print(f"The sequence is a {pattern} with a common {value}")
