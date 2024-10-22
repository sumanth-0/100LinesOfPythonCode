import random 
#assign variables
randomNum = random.randint(1, 100)
playing = True
guesses = 0
while playing:
    # start code sequence
    print(f"Guess {guesses}:")
    print("What is your guess?")
    guess = int(input())
    
    # win logic
    if guess == randomNum:
      print(f"You won in {guesses} guesses! The number was {randomNum}")
      playing = False
    elif guess > randomNum:
      print("Your guess is over!")
    else:
      print("Your guess is under!")
    
    #adds to guess counter
    guesses += 1
