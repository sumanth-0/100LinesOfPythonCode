def calculate_human_age(pet_age, pet_type):
    """Calculates the approximate human equivalent age of a pet.

    Args:
        pet_age: The age of the pet in years.
        pet_type: The type of pet (e.g., 'dog', 'cat', 'bird').

    Returns:
        The approximate human equivalent age.
    """

    if pet_type == "dog":
        # Approximate conversion for dogs
        if pet_age <= 1:
            return pet_age * 15
        elif pet_age <= 2:
            return pet_age * 9 + 15
        else:
            return pet_age * 4 + 21

    elif pet_type == "cat":
        # Approximate conversion for cats
        if pet_age <= 1:
            return pet_age * 15
        else:
            return pet_age * 4 + 16

    elif pet_type == "bird":
        # Approximate conversion for birds (varies widely)
        return pet_age * 7

    else:
        return "Invalid pet type"

if __name__ == "__main__":
    pet_type = input("Enter your pet's type (dog, cat, bird): ")
    pet_age = int(input("Enter your pet's age in years: "))

    human_age = calculate_human_age(pet_age, pet_type)
    print(f"Your {pet_type} is approximately {human_age} years old in human years.")
