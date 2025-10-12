import random
import time

# Print welcome message.
print("Welcome to Dice Battle Simulator! \n The game will continue until killed or the goal is reached ;)")

# Set goal.
GOAL = int(input("Please enter the goal score:"))


# Initialize player scores.
p1_score, p2_score = 0,0
scores = [0,0]

for i in range(GOAL):
    time.sleep(random.randint(10,20)/10)
    # Decide whose turn it is.
    p_id = (i % 2)

    #Roll the die.
    roll = random.randint(1,6)
    print(f"Player {p_id+1} rolled {roll}.")

    # Terminate the game when the goal is reached. Uses Walrus Operator ;)
    scores[p_id] += roll
    c_score = scores[p_id]
    if c_score >= GOAL:
        print(f"Player {p_id+1} has won! Congratulations!")
        print(f"The results are: \n Goal: {GOAL} \n Player 1: {scores[0]} \n Player 2: {scores[1]}")
        exit()

    print(f"Player {p_id+1} has a score of {c_score}.")