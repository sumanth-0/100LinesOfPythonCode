#IMPORT RANDOM MODULE TO SHUFFLE WORDS
import random

def shuffle_word(word):
    #SCRAMBLES THE LETTERS OF THE GIVEN WORD
    word_letters = list(word)
    random.shuffle(word_letters) #SHUFFLE THE LETTERS IN THE LIST
    return ''.join(word_letters) #JOIN THE SHUFFLED LETTERS BACK INTO A STRING
#MAIN GAME LOGIC

def main():
    word_array=["python","matplotlib","numpy","pandas","scikit-learn","tensorflow","keras","flask","django","jupyter","anaconda","spyder","visualstudio","github","bitbucket","docker","kubernetes","aws","azure","gcp","linux","tkinter","selenium","pytest","pycharm","notebook","terminal","commandline","algorithm","function","variable","loop","condition","string","integer","float","boolean","list","dictionary","tuple","set"]
    word=random.choice(word_array) #RANDOMLY SELECT A WORD FROM THE ARRAY
    shuffled=shuffle_word(word) #SCRAMBLE THE SELECTED WORD   
    #ENSURE THE SCRAMBLED WORD IS DIFFERENT FROM THE ORIGINAL
    while shuffled==word:
        shuffled=scramble_word(word)
    
    print("WELCOME TO THE WORD SCRAMBLE GAME")
    print("Unscramble the letters to form a valid word.")
    print("Scrambled word:", shuffled)

    attempts=3 #NUMBER OF ATTEMPTS ALLOWED
    while attempts>0:
        guess=input("Your guess: ").strip().lower() #GET USER INPUT AND NORMALIZE IT
        if guess==word:
            print("CONGRATULATIONS! You guessed the word correctly.")
            break
        else:
            attempts-=1
            if attempts>0:
                print(f"Incorrect! You have {attempts} attempts left. Try again.")
            else:
                print(f"Sorry, you've run out of attempts. The correct word was '{word}'.")

if __name__ == "__main__":
    main()