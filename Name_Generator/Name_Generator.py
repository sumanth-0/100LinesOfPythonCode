import random

# Define consonants and vowels
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
              "m", "n", "p", "r", "s", "t", "v", "w", "z"]
vowels = ["a", "e", "i", "o", "u"]

# Define name patterns (you can add your own)
patterns = ["CVC", "CV", "CVCV", "CV-CV", "CVC-CV"]

def generate_name_from_pattern(pattern):
    """Generate a name based on pattern (C = consonant, V = vowel)."""
    name = ""
    for char in pattern:
        if char == "C":
            name += random.choice(consonants)
        elif char == "V":
            name += random.choice(vowels)
        elif char == "-":
            name += "-"  # keep hyphen
        else:
            name += char  # any literal character
    return name.capitalize()

def generate_names(count=10):
    """Generate multiple random names."""
    names = []
    for _ in range(count):
        pattern = random.choice(patterns)
        name = generate_name_from_pattern(pattern)
        names.append(name)
    return names

# Run the generator
if __name__ == "__main__":
    num = int(input("How many names do you want to generate? "))
    generated = generate_names(num)
    print("\nGenerated Fantasy Names:\n")
    for name in generated:
        print(name)
