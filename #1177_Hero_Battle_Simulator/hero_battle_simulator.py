#!/usr/bin/env python3
"""
Hero Battle Simulator - A CLI game that simulates battles between randomly generated heroes.
"""

import random
import time
import sys

class Hero:
    """Represents a hero with stats and abilities."""
    
    HERO_NAMES = [
        "Aragorn", "Legolas", "Gimli", "Thor", "Hulk", "Wonder Woman",
        "Superman", "Batman", "Spiderman", "Iron Man", "Black Widow",
        "Captain America", "Wolverine", "Storm", "Jean Grey", "Cyclops"
    ]
    
    HERO_CLASSES = ["Warrior", "Mage", "Archer", "Rogue", "Paladin"]
    
    def __init__(self, name=None, hero_class=None):
        self.name = name or random.choice(self.HERO_NAMES)
        self.hero_class = hero_class or random.choice(self.HERO_CLASSES)
        self.max_health = random.randint(80, 150)
        self.health = self.max_health
        self.attack = random.randint(10, 30)
        self.defense = random.randint(5, 20)
        self.speed = random.randint(5, 15)
        self.crit_chance = random.uniform(0.1, 0.3)
    
    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        return actual_damage
    
    def attack_enemy(self, enemy):
        base_damage = self.attack
        is_crit = random.random() < self.crit_chance
        
        if is_crit:
            damage = int(base_damage * 2)
            damage_dealt = enemy.take_damage(damage)
            return damage_dealt, True
        else:
            damage_dealt = enemy.take_damage(base_damage)
            return damage_dealt, False
    
    def display_stats(self):
        print(f"\n{'='*50}")
        print(f"{self.name} the {self.hero_class}")
        print(f"{'='*50}")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print(f"Crit Chance: {self.crit_chance:.1%}")
        print(f"{'='*50}\n")

def simulate_battle(hero1, hero2):
    """Simulates a battle between two heroes."""
    print("\n" + "*"*60)
    print("BATTLE BEGINS!".center(60))
    print("*"*60)
    
    hero1.display_stats()
    hero2.display_stats()
    
    round_num = 1
    
    while hero1.is_alive() and hero2.is_alive():
        print(f"\n{'─'*60}")
        print(f"ROUND {round_num}".center(60))
        print(f"{'─'*60}\n")
        
        # Determine who attacks first based on speed
        if hero1.speed >= hero2.speed:
            first, second = hero1, hero2
        else:
            first, second = hero2, hero1
        
        # First hero attacks
        damage, is_crit = first.attack_enemy(second)
        crit_text = " (CRITICAL HIT!)" if is_crit else ""
        print(f"{first.name} attacks {second.name} for {damage} damage{crit_text}")
        print(f"{second.name}'s remaining health: {max(0, second.health)}/{second.max_health}")
        
        time.sleep(1)
        
        if not second.is_alive():
            break
        
        # Second hero attacks
        damage, is_crit = second.attack_enemy(first)
        crit_text = " (CRITICAL HIT!)" if is_crit else ""
        print(f"\n{second.name} attacks {first.name} for {damage} damage{crit_text}")
        print(f"{first.name}'s remaining health: {max(0, first.health)}/{first.max_health}")
        
        time.sleep(1)
        round_num += 1
    
    # Declare winner
    print("\n" + "*"*60)
    if hero1.is_alive():
        print(f"🏆 {hero1.name} WINS! 🏆".center(60))
    else:
        print(f"🏆 {hero2.name} WINS! 🏆".center(60))
    print("*"*60 + "\n")

def main():
    print("\n" + "="*60)
    print("HERO BATTLE SIMULATOR".center(60))
    print("="*60)
    
    print("\nGenerating two random heroes...\n")
    time.sleep(1)
    
    hero1 = Hero()
    hero2 = Hero()
    
    # Ensure heroes have different names
    while hero1.name == hero2.name:
        hero2 = Hero()
    
    simulate_battle(hero1, hero2)
    
    while True:
        choice = input("\nWould you like to simulate another battle? (y/n): ").lower()
        if choice == 'y':
            hero1 = Hero()
            hero2 = Hero()
            while hero1.name == hero2.name:
                hero2 = Hero()
            simulate_battle(hero1, hero2)
        elif choice == 'n':
            print("\nThanks for watching the battles! Goodbye!\n")
            sys.exit(0)
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
