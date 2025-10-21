import random

def GenerateSuperhero() -> str:
    adjectives = [
        "Mighty", "Incredible", "Fantastic", "Amazing", "Invincible", "Ultrasonnic","Silver", "Spectacular", "Dynamic", "Fearless", "Brave", "Super"]
    nouns = ["Falcon", "Tiger", "Shadow", "Knight", "Panther", "Blade", "Storm", "Phoenix", "Wolf", "Dragon", "Eagle", "Guardian", "Man", "Crusader", "Ranger"]


    return f"The {random.choice(adjectives)} {random.choice(nouns)}"

if __name__ == "__main__":
    print("Your superhero name:  ", GenerateSuperhero())