import pandas as pd
import random
import os

def load_words(file_path):
    """Load adjectives and nouns from Excel, skipping header words."""
    try:

        df = pd.read_excel(file_path, header=None)
        
        adjectives = df.iloc[1:, 0].dropna().tolist()
        nouns = df.iloc[1:, 1].dropna().tolist()

        if not adjectives or not nouns:
            print(f"❌ Error: Excel file '{file_path}' is empty or columns 1/2 are missing data after the first row.")

            raise ValueError("Word lists are empty.")
        
        return adjectives, nouns
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{file_path}' was not found. Please check the file name and path.")
        return None, None
    except Exception as e:
        print(f"❌ An error occurred while reading the Excel file: {e}")
        return None, None


def generate_username(adjectives, nouns):
    """Generate one random username."""

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    number = random.randint(10, 9999)

    return f"{adjective}{noun}{number}"

def main():
    file_path = "excell_py.xlsx"

    adjectives, nouns = load_words(file_path)

    if adjectives and nouns:
        print("🎮 Welcome to the Random Username Generator! (Words loaded successfully!)")
        print("Type 'username' to get one, or 'exit' to quit.\n")

        while True:
            
            user_input = input("👉 Enter command: ").strip().lower()
            
            if user_input == "username":
                print("💡 Your username:", generate_username(adjectives, nouns))
            elif user_input == "exit":
                print("👋 Goodbye! Have a great day!")
                break
            else:
                print("⚠️ Please type 'username' or 'exit'.")

if __name__ == "__main__":
    main()