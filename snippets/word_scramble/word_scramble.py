import random
import time

# Word categories and their words
WORD_CATEGORIES = {
    'Animals': ['elephant', 'giraffe', 'penguin', 'kangaroo', 'dolphin', 'butterfly', 'crocodile', 'flamingo'],
    'Countries': ['australia', 'brazil', 'canada', 'denmark', 'egypt', 'france', 'germany', 'india'],
    'Fruits': ['apple', 'banana', 'cherry', 'dragon', 'elderberry', 'fig', 'grape', 'honeydew'],
    'Sports': ['basketball', 'football', 'cricket', 'tennis', 'volleyball', 'swimming', 'baseball', 'hockey'],
    'Colors': ['purple', 'orange', 'yellow', 'green', 'crimson', 'azure', 'violet', 'scarlet'],
    'Professions': ['doctor', 'teacher', 'engineer', 'artist', 'chef', 'pilot', 'scientist', 'lawyer']
}

def scramble_word(word):
    """Scramble the letters of a word"""
    word_list = list(word)
    random.shuffle(word_list)
    scrambled = ''.join(word_list)
    
    # Make sure the scrambled word is different from original
    while scrambled == word and len(word) > 1:
        random.shuffle(word_list)
        scrambled = ''.join(word_list)
    
    return scrambled

def select_word():
    """Select a random word from a random category"""
    category = random.choice(list(WORD_CATEGORIES.keys()))
    word = random.choice(WORD_CATEGORIES[category])
    return word, category

def display_game_header():
    """Display game header"""
    print("\n" + "="*50)
    print("     WORD SCRAMBLE CHALLENGE")
    print("="*50)

def get_user_guess():
    """Get user's guess"""
    return input("\nYour answer: ").lower().strip()

def display_hint(word, attempts):
    """Display hints based on number of attempts"""
    if attempts == 2:
        print(f"\n💡 Hint: The word starts with '{word[0].upper()}'")
    elif attempts == 3:
        print(f"\n💡 Hint: The word has {len(word)} letters")
        print(f"First letter: {word[0].upper()}, Last letter: {word[-1].upper()}")

def play_round():
    """Play one round of the game"""
    word, category = select_word()
    scrambled = scramble_word(word)
    attempts = 0
    max_attempts = 3
    
    print(f"\n🎯 Category: {category}")
    print(f"Scrambled word: {scrambled.upper()}")
    
    start_time = time.time()
    
    while attempts < max_attempts:
        attempts += 1
        
        if attempts > 1:
            display_hint(word, attempts)
        
        guess = get_user_guess()
        
        if guess == word:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            print(f"\n✅ Correct! The word was '{word.upper()}'")
            print(f"⏱️ Time taken: {time_taken} seconds")
            print(f"⭐ Solved in {attempts} attempt(s)!")
            return True, attempts
        else:
            if attempts < max_attempts:
                print(f"❌ Incorrect! Try again. ({max_attempts - attempts} attempts left)")
            else:
                print(f"\n❌ Game Over! The correct word was '{word.upper()}'")
    
    return False, attempts

def main():
    """Main game loop"""
    display_game_header()
    
    score = 0
    total_rounds = 0
    
    while True:
        total_rounds += 1
        print(f"\n--- Round {total_rounds} ---")
        
        won, attempts = play_round()
        
        if won:
            score += 1
        
        print(f"\n{'='*50}")
        print(f"Current Score: {score}/{total_rounds}")
        print(f"{'='*50}")
        
        play_again = input("\n🎮 Play another round? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("\n" + "="*50)
    print("      GAME OVER")
    print(f"Final Score: {score}/{total_rounds}")
    if total_rounds > 0:
        percentage = (score / total_rounds) * 100
        print(f"Success Rate: {percentage:.1f}%")
    print("Thanks for playing Word Scramble Challenge!")
    print("="*50)

if __name__ == "__main__":
    main()
