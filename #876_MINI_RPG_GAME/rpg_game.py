import random


def create_character():
    print("Welcome to the Character Creation, what is your character's name?")
    character = {
        "name": input("Enter your character's name: "),
        "health": random.randint(20, 25),
        "attack": random.randint(7, 10),
        "skill": random.randint(5, 8),
        "defense": random.randint(5, 8),
        "speed": random.randint(5, 8),
    }
    print(f"\n--- Character stats for {character['name']} ---")
    for stat, value in character.items():
        if stat != "name":
            print(f"   [{stat.capitalize()}: {value}]")
    input("\nPress Enter to continue...")
    return character


def generate_enemy(arena_level):
    enemy = {
        "name": random.choice(["Soldier", "Mercenary", "Fighter"]),
        "health": random.randint(15+arena_level, 20+arena_level),
        "attack": random.randint(4+arena_level, 6+arena_level),
        "skill": arena_level,
        "defense": random.randint(2+arena_level, 4+arena_level),
        "speed": random.randint(2+arena_level, 4+arena_level),
    }
    print(f"A wild {enemy['name']} appears!")
    return enemy


def level_up(character):
    print(f"{character['name']} leveled up!")
    for stat in character:
        if stat != "name":
            old_value = character[stat]
            character[stat] += random.randint(0, 1)
            print(f"{stat.capitalize()}: {old_value} → {character[stat]}")
    input("\nPress Enter to continue...")


def battle(character, enemy):
    health = character["health"]
    print(f"\n{character['name']} (Health: {character['health']}) vs "
          f"{enemy['name']} (Health: {enemy['health']})")

    choice = input("\nWould you like to continue? (y/n): ").lower()
    if choice == 'n':
        character["health"] = 0

    attacker, defender = enemy, character
    if character["speed"] >= enemy["speed"]:
        attacker, defender = character, enemy

    while character["health"] > 0 and enemy["health"] > 0:
        hit_chance = (attacker['skill'] * 0.01) + 0.7
        if random.random() < hit_chance:
            damage = max(1, attacker["attack"] - defender["defense"])
            defender["health"] -= damage
            print(f"\n{attacker['name']} attacks! "
                  f"(Hit: {hit_chance:.0%}) → {damage} damage dealt.")
            print(f"{defender['name']} HP: {defender['health']} | "
                  f"{attacker['name']} HP: {attacker['health']}")
            if defender["health"] <= 0:
                print(f"\n{defender['name']} has been defeated!")
                break
        else:
            print(f"\n{attacker['name']} swings and misses! "
                  f"(Hit rate: {hit_chance:.0%})")
        attacker, defender = defender, attacker
        input("\nPress enter to continue...")

    if character["health"] > 0:
        print(f"{character['name']} wins the battle!")
        character["health"] = health  # restore after battle
        level_up(character)
    else:
        print(f"{enemy['name']} wins the battle!")


def game_loop(character):
    for arena_level in range(1, 100):
        print(f"\n--- Arena Level {arena_level} ---")
        enemy = generate_enemy(arena_level)
        while character["health"] > 0 and enemy["health"] > 0:
            battle(character, enemy)
        if character["health"] <= 0:
            print(f"Game Over! You made it to level {arena_level-1}")
            break


if __name__ == "__main__":
    player_character = create_character()
    game_loop(player_character)
