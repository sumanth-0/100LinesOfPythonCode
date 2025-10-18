import random

def generate_bingo():
    #Generate a 5x5 Bingo with random numbers.
    bingo = []
    for i in range(5):
        # Generate numbers for each column
        col = random.sample(range(1 + 15*i, 16 + 15*i), 5)
        bingo.append(col)
    #Transpose columns to rows
    bingo_card = [list(row) for row in zip(*bingo)]
    bingo_card[2][2] = 'FREE'
    return bingo_card

def print_card(card):
    #Show the Bingo card
    print(" B   I   N   G   O")
    for row in card:
        print(" ".join(f"{str(x):<3}" for x in row))

def check_win(card, called):
    #Check for row, column, or diagonal win
    #Convert all marked numbers to True
    def is_marked(x): return x == 'FREE' or x in called
    #Check rows & columns
    for i in range(5):
        if all(is_marked(card[i][j]) for j in range(5)): return True
        if all(is_marked(card[j][i]) for j in range(5)): return True
    #Check diagonals
    if all(is_marked(card[i][i]) for i in range(5)): return True
    if all(is_marked(card[i][4-i]) for i in range(5)): return True
    return False

def play_bingo():
    #Call Bingo until player wins
    card = generate_bingo()
    all_numbers = list(range(1, 76))
    random.shuffle(all_numbers)
    called = set()

    print_card(card)
    print("\nStarting Bingo game\n")

    for number in all_numbers:
        called.add(number)
        print(f"Number called: {number}")
        if check_win(card, called):
            print("\nBINGO! You won after", len(called), "numbers.")
            break

if __name__ == "__main__":
    play_bingo()