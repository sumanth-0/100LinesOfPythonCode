import random
# initialize variables

wins = 0
total_games = 0
playing = True
# Playing loop
while playing:
    print(f"You won {wins} out of {total_games} games!")
    print("Choose Rock, Paper, or Scissors:")
    player1_input = input()

    # Makes sure your input had correct capitalization
    while player1_input not in ["Rock", "Paper", "Scissors"]:
        print("Please try again, input is case sensitive (Rock, Paper, or Scissors):")
        player1_input = input()
    
    # Computer's choice
    player2_input = random.choice(["Rock", "Paper", "Scissors"])
    print(f"Computer picked {player2_input}")

    # Determine the outcome
    if player1_input == player2_input:
        print("It's a tie!")
    elif (player1_input == "Rock" and player2_input == "Paper") or \
         (player1_input == "Paper" and player2_input == "Scissors") or \
         (player1_input == "Scissors" and player2_input == "Rock"):
        print("You lose!")
    else:
        print("You win!")
        wins += 1

    total_games += 1  # Increment total games for every round played

    # Ask if the player wants to play again
    print("Would you like to play again? (Y/N)")
    answer = input()
    if answer == "N":
        playing = False
# Final message
print("Thanks for playing!")
print(f"You won {wins} out of {total_games} games!")
