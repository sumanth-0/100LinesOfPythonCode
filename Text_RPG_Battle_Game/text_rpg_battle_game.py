import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_target(self, target):
        damage = max(1, self.attack - target.defense + random.randint(-2, 2))
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage! {target.name}'s health is now {target.health}.")

class Player(Character):
    def level_up(self):
        self.health += 10
        self.attack += 2
        self.defense += 1
        print(f"Level up! Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}")

class Monster(Character):
    pass

def battle(player, monster):
    print(f"A wild {monster.name} appears!")
    while player.health > 0 and monster.health > 0:
        player.attack_target(monster)
        if monster.health > 0:
            monster.attack_target(player)
    if player.health > 0:
        print(f"{player.name} defeated the {monster.name}!")
        player.level_up()
    else:
        print(f"{player.name} was defeated by the {monster.name}.")

# User Input
name = input("Enter your hero's name: ")
player = Player(name, health=50, attack=10, defense=5)

monsters = [
    Monster("Goblin", health=20, attack=5, defense=3),
    Monster("Dragon", health=80, attack=15, defense=10),
    Monster("Orc", health=40, attack=8, defense=4)
]

while player.health > 0:
    monster = random.choice(monsters)
    battle(player, monster)
    if player.health <= 0:
        print("Game Over!")
        break
    else:
        next_battle = input("Do you want to fight another monster? (yes/no): ")
        if next_battle.lower() != "yes":
            print("You have survived and gained strength. Game Ended!")
            break
