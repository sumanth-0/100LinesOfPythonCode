import random
import time # For a small delay to make the fight more readable

class Character:
    """Represents a fighter in the battle."""
    def __init__(self, name):
        self.name = name
        self.health = random.randint(80, 120)  # Health between 80-120
        self.attack = random.randint(15, 25)   # Attack between 15-25
        self.defense = random.randint(5, 15)   # Defense between 5-15
        self.is_alive = True

    def __str__(self):
        """String representation for character stats."""
        return (f"{self.name}:\n"
                f"  Health: {self.health}\n"
                f"  Attack: {self.attack}\n"
                f"  Defense: {self.defense}")

    def take_damage(self, damage_amount):
        """Calculates and applies damage taken."""
        self.health -= damage_amount
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
        print(f"  {self.name} takes {damage_amount} damage. Health: {self.health}")

    def attack_target(self, target):
        """Performs an attack on a target character."""
        # Calculate base damage from attacker's strength
        base_damage = self.attack + random.randint(-5, 5) # Slight variance in attack
        
        # Calculate actual damage after target's defense
        # Damage should always be at least 1, even if defense is high
        actual_damage = max(1, base_damage - target.defense)
        
        print(f"\n{self.name} attacks {target.name}!")
        target.take_damage(actual_damage)

def simulate_battle(char1, char2):
    """Simulates the turn-based battle between two characters."""
    print("\n--- BATTLE START! ---")
    print(char1)
    print(char2)
    print("---------------------\n")

    round_num = 1
    # Determine who goes first randomly
    current_attacker = random.choice([char1, char2])
    current_defender = char2 if current_attacker == char1 else char1

    print(f"{current_attacker.name} goes first!")

    while char1.is_alive and char2.is_alive:
        print(f"\n--- Round {round_num} ---")
        
        # Current attacker takes their turn
        current_attacker.attack_target(current_defender)
        
        # Check if the defender survived the attack
        if not current_defender.is_alive:
            break # Battle ends
            
        # Swap roles for the next turn
        current_attacker, current_defender = current_defender, current_attacker
        round_num += 1
        
        time.sleep(1) # Pause for readability

    print("\n--- BATTLE END! ---")
    if char1.is_alive:
        print(f"🎉 {char1.name} wins the battle with {char1.health} health remaining! 🎉")
    elif char2.is_alive:
        print(f"🎉 {char2.name} wins the battle with {char2.health} health remaining! 🎉")
    else:
        print("It's a draw! Both fighters fell at the same time.") # Very rare, but possible if last hit kills both

if __name__ == "__main__":
    # Seed the random number generator (optional, but good for consistent testing)
    # random.seed(42) 

    print("Generating two mighty warriors...")
    character1 = Character("Hero 1")
    character2 = Character("Hero 2")

    simulate_battle(character1, character2)