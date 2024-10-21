import random
wins = 0
total_games = 0
playing = True
while playing:
  print(f"You won {wins} out of {total_games} games!")
  print("Chose Rock, Paper, or Scissors")
  player1_input = input()
  while player1_input != "Rock" or "Paper" or "Scissors":
    print("Please try again, input is case sensituive")
  
  player2_input = random.randint(1,3)
  if player2_input == 1:
    player2_input = "Rock"
  elif player2_input == 2:
    player2_input = "Paper"
  else:
    player2_input = "Scissors"
  print(f"Computer picked {player2_input}")
  if player1_input == player2_input:
    print("its a tie!")
  elif (player1_input == "Rock" and player2_input == "Paper") or (player1_input == "Paper" and player2_input == "Scissors") or (player1_input == "Scissors" and player2_input == "Rock"):
    print("You lose!")
    total_games += 1
  else:
    print("You win!")
    wins += 1
    total_games += 1

  print("Would you like to play again? (Y/N)")
  answer = input()
  if input == "N":
    playing = False
    break
