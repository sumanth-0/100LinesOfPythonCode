import random
import time

class SlotMachine:
    def __init__(self):
        self.symbols = ['🍒', '🍋', '🍊', '🍇', '💎', '7️⃣', '⭐']
        self.payouts = {
            '🍒': 2,
            '🍋': 3,
            '🍊': 4,
            '🍇': 5,
            '💎': 10,
            '7️⃣': 20,
            '⭐': 50
        }
        self.balance = 100
        self.bet_amount = 0

    def display_header(self):
        print("\n" + "="*50)
        print("🎰  MINI SLOT MACHINE  🎰")
        print("="*50)
        print(f"Current Balance: ${self.balance}")
        print("="*50 + "\n")

    def spin_reels(self):
        reel1 = random.choice(self.symbols)
        reel2 = random.choice(self.symbols)
        reel3 = random.choice(self.symbols)
        return [reel1, reel2, reel3]

    def animate_spin(self):
        print("\nSpinning...")
        for _ in range(5):
            temp = [random.choice(self.symbols) for _ in range(3)]
            print(f"\r| {temp[0]} | {temp[1]} | {temp[2]} |", end="", flush=True)
            time.sleep(0.2)
        print()

    def calculate_payout(self, reels):
        if reels[0] == reels[1] == reels[2]:
            symbol = reels[0]
            multiplier = self.payouts[symbol]
            return self.bet_amount * multiplier
        elif reels[0] == reels[1] or reels[1] == reels[2]:
            return self.bet_amount
        return 0

    def display_result(self, reels, payout):
        print(f"\n┌─────┬─────┬─────┐")
        print(f"│  {reels[0]}  │  {reels[1]}  │  {reels[2]}  │")
        print(f"└─────┴─────┴─────┘\n")
        
        if payout > self.bet_amount:
            print(f"🎉 WINNER! You won ${payout}!")
        elif payout == self.bet_amount:
            print(f"↩️  You got your bet back! ${payout}")
        else:
            print(f"😔 No win this time. You lost ${self.bet_amount}")

    def display_paytable(self):
        print("\n" + "="*50)
        print("PAYTABLE (3 matching symbols)")
        print("="*50)
        for symbol, multiplier in sorted(self.payouts.items(), key=lambda x: x[1]):
            print(f"{symbol} {symbol} {symbol}  →  {multiplier}x your bet")
        print("\nTwo matching symbols → Get your bet back")
        print("="*50 + "\n")

    def get_bet(self):
        while True:
            try:
                bet = int(input(f"Enter bet amount (1-{self.balance}): $"))
                if 1 <= bet <= self.balance:
                    return bet
                else:
                    print(f"Please enter amount between $1 and ${self.balance}")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def play_round(self):
        self.display_header()
        self.bet_amount = self.get_bet()
        self.balance -= self.bet_amount
        
        self.animate_spin()
        reels = self.spin_reels()
        payout = self.calculate_payout(reels)
        
        self.display_result(reels, payout)
        self.balance += payout
        
        print(f"\nNew Balance: ${self.balance}")
        return self.balance > 0

    def play(self):
        print("Welcome to Mini Slot Machine!")
        self.display_paytable()
        
        while self.balance > 0:
            if not self.play_round():
                break
            
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                break
        
        if self.balance <= 0:
            print("\n💸 Game Over! You're out of money.")
        else:
            print(f"\n👋 Thanks for playing! Final balance: ${self.balance}")

if __name__ == "__main__":
    game = SlotMachine()
    game.play()
