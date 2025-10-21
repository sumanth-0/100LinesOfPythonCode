#!/usr/bin/env python3
"""
Mini RPG Battle Game
A simple turn-based RPG battle system where players fight against enemies.
"""

import random
import time
import sys

class Character:
    """Base class for all characters in the game."""
    
    def __init__(self, name, health, attack, defense, magic=0):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.is_alive = True
    
    def take_damage(self, damage):
        """Apply damage to character with defense reduction."""
        actual_damage = max(1, damage - self.defense)
        self.health -= actual_damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
        return actual_damage
    
    def heal(self, amount):
        """Heal the character."""
        self.health = min(self.max_health, self.health + amount)
    
    def basic_attack(self, target):
        """Perform a basic attack on target."""
        damage = random.randint(self.attack - 2, self.attack + 2)
        actual_damage = target.take_damage(damage)
        return actual_damage
    
    def magic_attack(self, target):
        """Perform a magic attack on target."""
        if self.magic < 10:
            return 0
        self.magic -= 10
        damage = random.randint(self.attack + 5, self.attack + 10)
        actual_damage = target.take_damage(damage)
        return actual_damage

class Player(Character):
    """Player character with special abilities."""
    
    def __init__(self, name):
        super().__init__(name, health=100, attack=15, defense=5, magic=50)
        self.potions = 3
    
    def use_potion(self):
        """Use a health potion."""
        if self.potions > 0:
            heal_amount = random.randint(20, 30)
            self.heal(heal_amount)
            self.potions -= 1
            return heal_amount
        return 0

class Enemy(Character):
    """Enemy character."""
    
    def __init__(self, name, level=1):
        health = 50 + (level * 10)
        attack = 10 + (level * 2)
        defense = 2 + level
        magic = 20 + (level * 5)
        super().__init__(name, health, attack, defense, magic)
        self.level = level

def print_slow(text, delay=0.03):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_status(player, enemy):
    """Display current status of both characters."""
    print("\n" + "="*50)
    print(f"{player.name}: HP={player.health}/{player.max_health} | Magic={player.magic} | Potions={player.potions}")
    print(f"{enemy.name}: HP={enemy.health}/{enemy.max_health} | Magic={enemy.magic}")
    print("="*50 + "\n")

def player_turn(player, enemy):
    """Handle player's turn."""
    while True:
        print("\nYour turn! Choose an action:")
        print("1. Basic Attack")
        print("2. Magic Attack (Cost: 10 Magic)")
        print("3. Use Potion")
        print("4. Defend (Reduce damage next turn)")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            damage = player.basic_attack(enemy)
            print_slow(f"\n{player.name} attacks {enemy.name} for {damage} damage!")
            return False
        elif choice == "2":
            if player.magic >= 10:
                damage = player.magic_attack(enemy)
                print_slow(f"\n{player.name} casts a powerful spell on {enemy.name} for {damage} damage!")
                return False
            else:
                print("Not enough magic!")
        elif choice == "3":
            if player.potions > 0:
                heal = player.use_potion()
                print_slow(f"\n{player.name} uses a potion and restores {heal} HP!")
                return False
            else:
                print("No potions left!")
        elif choice == "4":
            print_slow(f"\n{player.name} takes a defensive stance!")
            return True
        else:
            print("Invalid choice! Try again.")

def enemy_turn(enemy, player, player_defending):
    """Handle enemy's turn."""
    time.sleep(1)
    action = random.randint(1, 10)
    
    if action <= 7:  # 70% basic attack
        damage = enemy.basic_attack(player)
        if player_defending:
            damage = damage // 2
        print_slow(f"{enemy.name} attacks {player.name} for {damage} damage!")
    elif action <= 9 and enemy.magic >= 10:  # 20% magic attack
        damage = enemy.magic_attack(player)
        if player_defending:
            damage = damage // 2
        print_slow(f"{enemy.name} unleashes a magic attack on {player.name} for {damage} damage!")
    else:  # 10% heal
        heal_amount = random.randint(10, 20)
        enemy.heal(heal_amount)
        print_slow(f"{enemy.name} regenerates {heal_amount} HP!")

def battle(player, enemy):
    """Main battle loop."""
    print_slow(f"\n⚔️  A wild {enemy.name} (Level {enemy.level}) appears! ⚔️\n")
    time.sleep(1)
    
    while player.is_alive and enemy.is_alive:
        display_status(player, enemy)
        player_defending = player_turn(player, enemy)
        
        if not enemy.is_alive:
            print_slow(f"\n🎉 Victory! {enemy.name} has been defeated! 🎉")
            return True
        
        enemy_turn(enemy, player, player_defending)
        
        if not player.is_alive:
            print_slow(f"\n💀 Defeat! {player.name} has been defeated... 💀")
            return False
    
    return player.is_alive

def main():
    """Main game function."""
    print("="*50)
    print("      Welcome to Mini RPG Battle!")
    print("="*50)
    
    player_name = input("\nEnter your character's name: ").strip() or "Hero"
    player = Player(player_name)
    
    enemies = [
        ("Goblin", 1),
        ("Orc Warrior", 2),
        ("Dark Wizard", 3),
        ("Dragon", 4)
    ]
    
    for enemy_name, level in enemies:
        enemy = Enemy(enemy_name, level)
        
        if not battle(player, enemy):
            print("\nGame Over! Better luck next time!")
            break
        
        # Restore some stats between battles
        player.magic = min(player.max_health, player.magic + 20)
        player.heal(15)
        print(f"\n{player.name} recovers 15 HP and 20 Magic before the next battle!")
        time.sleep(2)
    else:
        print("\n" + "="*50)
        print("🏆 CONGRATULATIONS! You defeated all enemies! 🏆")
        print("="*50)

if __name__ == "__main__":
    main()
