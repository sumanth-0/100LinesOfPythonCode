import random, colorama, os, time # importing modules
colorama.init() # initialize colorame
print(chr(27) + "[2J") # clearing the screen
word="" # placeholder word
termSize = os.get_terminal_size()
tries, maxTries = 0,6
triesList = []
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "dictionary.txt"), "r") as dict:
    words=dict.read().splitlines() # splitting the file lines
    word=words[random.randint(0,len(words)-1)] # setting word to random list item of words
print(colorama.Cursor.POS(1,1))
for _ in range(maxTries-1): print("\u25a0 " * len(word))
def clearLine(lineNum): print(colorama.Cursor.POS(1, lineNum) + (" " * termSize.columns) + colorama.Cursor.POS(1, lineNum), end="")
def NINENINE():
    print(colorama.Fore.RED, end="")
    while True:
        print("\aL", end="", flush=True)
        time.sleep(0.05)
        print("\aI", end="", flush=True)
        time.sleep(0.05)
        print("\aA", end="", flush=True)
        time.sleep(0.05)
        print("\aR", end="", flush=True)
        time.sleep(0.05)
def gameTry():
    global tries
    clearLine(maxTries+1)
    guess = input(colorama.ansi.clear_line(7) + colorama.Cursor.POS(1,maxTries+1) + f"Try {tries+1}/{maxTries}:")
    output = ''
    correctness = 0
    if guess == "NINENINE":
        NINENINE()
        raise SystemExit
    else: 
        for i in range(len(word)):
            try:
                if guess[i] == word[i]:
                    output += colorama.Fore.GREEN + guess[i] + colorama.Style.RESET_ALL + colorama.Cursor.FORWARD(1)
                    correctness += 1
                elif guess[i] in word:
                    output += colorama.Fore.YELLOW + guess[i] + colorama.Style.RESET_ALL + colorama.Cursor.FORWARD(1)
                else:
                    output += colorama.Fore.WHITE + guess[i] + colorama.Style.RESET_ALL + colorama.Cursor.FORWARD(1)
            except:
                print(colorama.Fore.RED + "\aThis might've been an error!")
                print("Also I'm too lazy to implement an actual error handler so this is gonna exit.")
                raise SystemExit
    clearLine(tries+1)
    print(colorama.Cursor.POS(1,tries+1) + output)
    tries += 1
    if correctness == len(word):
        win()
    correctness = 0
def win():
    print(colorama.ansi.clear_screen(), end='')
    print('\u250C' + '\u2500'*42 + '\u2510')
    print(f"\u2502 You got the word {word} right in {tries} tries! \u2502")
    print('\u2514' + '\u2500'*42 + '\u2518')
    raise SystemExit
for a in range(maxTries):
    gameTry()
print('\u250C' + '\u2500'*31 + '\u2510' + f"\n\u2502 You lost! The word was {word}. \u2502\n" + '\u2514' + '\u2500'*31 + '\u2518')