#  Random Battle Simulator

A fun **turn-based battle simulator** written in Python, where two randomly generated characters fight until one emerges victorious. Each fighter has unique health, attack, and defense stats — making every battle unpredictable!

---

##  Features

- **Randomized Character Stats** (Health, Attack, Defense)
-  **Turn-Based Combat System**
-  **Dynamic Damage Calculation** (includes variance and defense)
-  **Round-by-Round Simulation** with time delay for readability
-  **Automatic Winner Announcement**

---

##  How It Works

1. Two `Character` objects are created with random attributes.
2. The program prints their stats before the battle.
3. The first attacker is chosen randomly.
4. Each character alternately attacks until one’s health drops to `0`.
5. The winner (or draw) is displayed at the end.

---

##  Code Structure

### `Character` Class
Represents a fighter with:
- `name`: Name of the character.
- `health`: Random between 80–120.
- `attack`: Random between 15–25.
- `defense`: Random between 5–15.
- `is_alive`: Boolean tracking survival.

**Key Methods**
- `take_damage(damage_amount)`: Applies damage and updates health.
- `attack_target(target)`: Calculates and applies damage to another character.

### `simulate_battle(char1, char2)`
Runs the fight simulation between two characters turn by turn until one wins.

---


