# Mini RPG Battle

A turn-based RPG battle game implemented in Python where players fight against progressively difficult enemies.

## Features

- **Turn-based Combat System**: Strategic gameplay with multiple action choices
- **Character Classes**: Player and Enemy classes with unique attributes
- **Combat Mechanics**:
  - Basic Attacks: Standard damage dealing
  - Magic Attacks: Powerful spells that consume magic points
  - Potions: Health restoration items (limited quantity)
  - Defense: Reduce incoming damage by taking a defensive stance
- **Progressive Difficulty**: Fight through 4 increasingly challenging enemies
- **Health & Magic Management**: Strategic resource management is key to victory

## Game Structure

### Character Attributes
- **Health (HP)**: Character's life points
- **Attack**: Base damage output
- **Defense**: Damage reduction
- **Magic**: Resource for casting spells

### Enemies
1. **Goblin** (Level 1) - Beginner enemy
2. **Orc Warrior** (Level 2) - Stronger melee fighter
3. **Dark Wizard** (Level 3) - Magic-focused enemy
4. **Dragon** (Level 4) - Final boss with high stats

## How to Play

1. Run the game:
   ```bash
   python mini_rpg_battle.py
   ```

2. Enter your character's name when prompted

3. During each battle, choose your action:
   - **1**: Basic Attack - Deal standard damage
   - **2**: Magic Attack - Deal increased damage (costs 10 magic)
   - **3**: Use Potion - Restore 20-30 HP (limited to 3 potions)
   - **4**: Defend - Reduce incoming damage by 50% for one turn

4. Defeat all enemies to win the game!

## Requirements

- Python 3.x
- Standard library modules: `random`, `time`, `sys`

## Game Tips

- Save your potions for tough battles
- Use magic attacks strategically on stronger enemies
- Pay attention to your HP and defend when necessary
- Magic regenerates between battles

## Code Structure

- `Character` class: Base class for all game characters
- `Player` class: Player-specific functionality including potions
- `Enemy` class: Enemy-specific attributes with level scaling
- `battle()` function: Main battle loop
- `main()` function: Game initialization and progression

## Related Issue

This project was created for [Issue #876](https://github.com/sumanth-0/100LinesOfPythonCode/issues/876) of the 100LinesOfPythonCode repository.

## License

This project is part of the 100LinesOfPythonCode repository and follows its licensing terms.
