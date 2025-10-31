word=input("Enter word: ")
hint=input("Enter hint for word: ")
n=len(word)
dict1={}
for letter in word:
    if letter==' ':
        continue

    if letter in dict1:
        dict1[letter]+=1
    else:
        dict1[letter]=1
sorted_dict=dict(sorted(dict1.items()))
print(sorted_dict)
print("The letters in the word along with their frequencies are:")
print(sorted_dict)
print("You get five wrong guesses to guess the word")
print("Good luck!")
for it in range(1,6):
    flag1=0
    guess=(input(f"guess {it}:"))
    if guess==word:
        print("Congratulations you guessed the word!")
        break
    for i in range(0,it):
        print("💔",end=" ")
    for i in range(0,5-it):
        print("❤️",end="  ")
    print()
    if it==3:
        print("Only 2 lives left, do you want a hint?")
        ans=input("Enter yes/no:")
        if(ans.lower()=="yes"):
            print("Hint:",hint)
        else:
            print("Ok, you may continue.")
    if it==5:
        print(f"The word was {word}. Better luck next time.")