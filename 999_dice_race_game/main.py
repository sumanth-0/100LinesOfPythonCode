from random import randint
from time import sleep


def main():
    # Inputs for setup
    print("Let's play a game!")
    player1_name = input("Player 1 Name: ")
    player2_name = input("Player 2 Name: ")
    goal = input("Input the score goal: ")

    # Input validation
    try:
        goal = int(goal)
    except ValueError:
        print("Goal must be an integer")
        return

    # Variable setup
    player1 = player2 = 0
    game_over = False

    # Main game loop
    while not game_over:
        print("Rolling dice...")
        sleep(1.5)
        player1_roll = randint(1, 6)
        player2_roll = randint(1, 6)

        player1 += player1_roll
        player2 += player2_roll

        print(f"{player1_name} rolled: {player1_roll}. Total score: {player1}")
        sleep(0.5)
        print(f"{player2_name} rolled: {player2_roll}. Total score: {player2}")

        game_over = player1 >= goal or player2 >= goal
        if not game_over:
            sleep(0.5)
            print("No winners yet, another round!")
            sleep(1)

    # Announce the winner
    if player1 >= goal and player2 >= goal:
        print("You both win!")
    elif player1 >= goal:
        print(f"{player1_name} wins!")
    else:
        print(f"{player2_name} wins!")


if __name__ == "__main__":
    main()
