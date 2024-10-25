import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            joke = response.json()
            print(f"{joke['setup']}\n{joke['punchline']}")
        else:
            print("Couldn't fetch a joke right now. Try again later!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Random Joke Generator!")
    while True:
        print("\n1. Get a joke")
        print("2. Exit")
        choice = input("Choose an option (1/2): ")
        
        if choice == '1':
            get_joke()
        elif choice == '2':
            print("Goodbye! Hope you had a laugh!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
