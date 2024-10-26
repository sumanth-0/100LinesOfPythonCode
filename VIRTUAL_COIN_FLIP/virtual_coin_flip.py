import random
import time

class VirtualCoinFlip:
    def __init__(self, coin_style="Classic"):
        self.coin_style = coin_style
        self.sides = ["Heads", "Tails"]
    
    def flip_coin(self):
        print(f"Flipping the coin in {self.coin_style} style...")
        time.sleep(1)  # Adding a short delay for effect
        result = random.choice(self.sides)
        print(f"The result is: {result}")
        return result

def main():
    print("Welcome to the Virtual Coin Flip!")
    style = input("Choose a coin style (e.g., Classic, Gold, Silver): ")
    
    coin_flip = VirtualCoinFlip(coin_style=style)
    result = coin_flip.flip_coin()
    
    # Optional: Allow user to flip again
    while input("Flip again? (y/n): ").lower() == 'y':
        coin_flip.flip_coin()

if __name__ == "__main__":
    main()
