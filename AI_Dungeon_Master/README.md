# AI Dungeon Master

A simple AI-powered dungeon master that generates scenarios and handles player actions in a text-based RPG game.

## Description

This Python script simulates a classic text-based RPG experience where the AI acts as a Dungeon Master, generating dynamic scenarios and responding to player actions. The game features:

- **Dynamic Scenario Generation**: Random scenarios with various locations, creatures, characters, and objects
- **Player Actions**: Support for multiple action types including attack, run, talk, search, and heal
- **Game State Management**: Track player HP, gold, and inventory
- **Natural Language Processing**: Simple pattern matching to interpret player commands
- **Turn-based Gameplay**: Interactive loop that continues until the player dies or quits

## Features

- 🎲 Random scenario generation using templates
- ⚔️ Combat system with attack and defense mechanics
- 💰 Loot and treasure collection
- 🗣️ Character interaction and dialogue
- 🔍 Exploration and item discovery
- ❤️ Health and inventory management
- 📦 Simple yet engaging gameplay loop

## How to Run

```bash
python ai_dungeon_master.py
```

## Gameplay Instructions

1. The game will present you with random scenarios
2. Type your action in natural language (e.g., "attack the goblin", "search for treasure", "run away")
3. The AI will interpret your action and respond with outcomes
4. Monitor your HP and inventory
5. Continue until you win, die, or quit

## Available Commands

- **attack/fight/strike**: Engage in combat with enemies
- **run/flee/escape**: Retreat from danger
- **talk/speak/negotiate**: Interact with characters
- **search/explore/investigate**: Look for items and treasure
- **heal/potion/rest**: Use a potion to restore HP
- **quit/exit/q**: End the game

## Example Gameplay

```
=== AI DUNGEON MASTER ===
Commands: attack, run, talk, search, heal, status, quit
Type your actions in natural language!

You enter a dark dungeon. A goblin attacks you!

HP: 100 | Gold: 50 | Items: sword, potion

What do you do? > attack

>>> You defeated the enemy! Gained 20 gold.
```

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Code Structure

- `PLAYER`: Dictionary storing game state (HP, gold, inventory)
- `SCENARIOS`: Template strings for scenario generation
- `generate_scenario()`: Creates random scenarios using templates
- `handle_action()`: Processes player actions and returns outcomes
- `display_status()`: Shows player's current stats
- `main()`: Main game loop

## Technical Details

- **Lines of Code**: Under 100 lines (excluding comments and blank lines)
- **Pattern Matching**: Uses regex for flexible command interpretation
- **Randomization**: Leverages Python's `random` module for unpredictability
- **State Management**: Simple dictionary-based player state

## Future Enhancements

Possible improvements for future versions:
- Save/load game functionality
- More complex combat mechanics
- Persistent world state
- Character progression and leveling
- Multiple enemy types with different behaviors
- Quest system
- More detailed item management

## Contributing

This project is part of the 100 Lines of Python Code repository. Contributions and suggestions are welcome!

## License

This code is provided as-is for educational and entertainment purposes.

## Issue Reference

This solution addresses issue #619: Make AI Dungeon Master for Roleplaying Games
