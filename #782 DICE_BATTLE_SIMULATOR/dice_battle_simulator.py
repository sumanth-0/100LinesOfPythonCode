import random

# Print welcome message.
print("Welcome to Dice Battle Simulator! \n The game will continue until killed or the goal is reached ;)")

# Set goal.
GOAL = int(input("Please enter the goal score:"))


# Initialize player scores.
p1_score, p2_score = 0,0
scores = [0,0]

for i in range(GOAL):
    #Roll the die.
    roll = random.randint(1,6)

    # Decide whose turn it is.
    p_id = (i % 2)

    # Terminate the game when the goal is reached. Uses Walrus Operator ;)
    if (scores[p_id] := scores[p_id] + roll) >= GOAL:
        print(f"Player {p_id+1} has won! Congratulations!")
        print(f"The results are: \n Goal: {GOAL} \n Player 1: {scores[0]} \n Player 2: {scores[1]}")
        exit()