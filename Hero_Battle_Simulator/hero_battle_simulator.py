#!/usr/bin/env python3
"""
Hero Battle Simulator - A CLI game where two randomly generated heroes battle.
Each hero has randomized stats and abilities.
"""

import random
import time

class Hero:
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.is_alive = True

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp -= actual_damage
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
        return actual_damage

    def attack_enemy(self, enemy):
        base_damage = random.randint(self.attack - 5, self.attack + 5)
        crit_chance = random.random()
        if crit_chance > 0.85:
            base_damage = int(base_damage * 1.5)
            print(f"  💥 CRITICAL HIT!")
        damage_dealt = enemy.take_damage(base_damage)
        return damage_dealt

    def display_stats(self):
        print(f"\n{self.name}:")
        print(f"  HP: {self.hp}/{self.max_hp} ❤️")
        print(f"  Attack: {self.attack} ⚔️")
        print(f"  Defense: {self.defense} 🛡️")
        print(f"  Speed: {self.speed} ⚡")

def generate_random_hero(hero_number):
    """Generate a hero with random stats and name."""
    first_names = ["Brave", "Mighty", "Swift", "Dark", "Noble", "Fierce", "Wild", "Wise"]
    last_names = ["Warrior", "Knight", "Assassin", "Mage", "Ranger", "Berserker", "Paladin", "Monk"]
    
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    hp = random.randint(80, 150)
    attack = random.randint(15, 35)
    defense = random.randint(5, 15)
    speed = random.randint(5, 20)
    
    return Hero(name, hp, attack, defense, speed)

def battle_round(hero1, hero2):
    """Execute one round of battle."""
    # Determine who attacks first based on speed
    if hero1.speed >= hero2.speed:
        first, second = hero1, hero2
    else:
        first, second = hero2, hero1
    
    # First attacker
    damage = first.attack_enemy(second)
    print(f"\n{first.name} attacks {second.name} for {damage} damage!")
    
    if not second.is_alive:
        return
    
    # Second attacker counterattacks
    time.sleep(0.5)
    damage = second.attack_enemy(first)
    print(f"{second.name} counterattacks {first.name} for {damage} damage!")

def main():
    print("="*50)
    print("⚔️  HERO BATTLE SIMULATOR ⚔️")
    print("="*50)
    
    # Generate two random heroes
    hero1 = generate_random_hero(1)
    hero2 = generate_random_hero(2)
    
    print("\n🎲 Two heroes have been summoned to battle!")
    hero1.display_stats()
    hero2.display_stats()
    
    input("\nPress Enter to start the battle...")
    
    round_number = 1
    while hero1.is_alive and hero2.is_alive:
        print(f"\n{'='*50}")
        print(f"⚔️  ROUND {round_number} ⚔️")
        print(f"{'='*50}")
        
        battle_round(hero1, hero2)
        
        print(f"\n--- Current Status ---")
        print(f"{hero1.name}: {hero1.hp}/{hero1.max_hp} HP")
        print(f"{hero2.name}: {hero2.hp}/{hero2.max_hp} HP")
        
        round_number += 1
        time.sleep(1)
    
    # Declare winner
    print(f"\n{'='*50}")
    if hero1.is_alive:
        print(f"🏆 {hero1.name} WINS! 🏆")
    else:
        print(f"🏆 {hero2.name} WINS! 🏆")
    print(f"{'='*50}")
    print(f"\nBattle lasted {round_number - 1} rounds!")

if __name__ == "__main__":
    main()
