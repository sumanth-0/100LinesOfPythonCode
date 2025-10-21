#!/usr/bin/env python3
"""
Reaction Timer Game
Measure how fast you can respond after a random time delay.

This game tests your reaction time by displaying a prompt after a random delay
and measuring how quickly you can press Enter. It includes multiple rounds,
statistics tracking, difficulty levels, and a high score system.
"""

import time
import random
import os
import json
from datetime import datetime
import statistics

# Constants
HIGH_SCORES_FILE = 'high_scores.json'
DIFFICULTY_LEVELS = {
    'easy': {'min_delay': 2.0, 'max_delay': 5.0, 'rounds': 3},
    'medium': {'min_delay': 1.0, 'max_delay': 4.0, 'rounds': 5},
    'hard': {'min_delay': 0.5, 'max_delay': 3.0, 'rounds': 7}
}

class ReactionTimer:
    """Main class for the Reaction Timer game."""
    
    def __init__(self):
        self.reaction_times = []
        self.difficulty = 'medium'
        self.player_name = ''
        
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_banner(self):
        """Display the game banner."""
        print("="*50)
        print("⚡ REACTION TIMER GAME ⚡".center(50))
        print("="*50)
        print()
    
    def get_player_info(self):
        """Get player name and difficulty level."""
        self.player_name = input("Enter your name: ").strip()
        if not self.player_name:
            self.player_name = "Anonymous"
        
        print("\nSelect Difficulty:")
        print("1. Easy (3 rounds, 2-5s delay)")
        print("2. Medium (5 rounds, 1-4s delay)")
        print("3. Hard (7 rounds, 0.5-3s delay)")
        
        while True:
            choice = input("\nEnter choice (1-3): ").strip()
            if choice == '1':
                self.difficulty = 'easy'
                break
            elif choice == '2':
                self.difficulty = 'medium'
                break
            elif choice == '3':
                self.difficulty = 'hard'
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    def countdown(self):
        """Display a countdown before starting."""
        print("\nGet ready...")
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        print("GO!\n")
    
    def play_round(self, round_num):
        """Play a single round of the reaction timer game."""
        config = DIFFICULTY_LEVELS[self.difficulty]
        delay = random.uniform(config['min_delay'], config['max_delay'])
        
        print(f"Round {round_num}/{config['rounds']}")
        print("Wait for the prompt...")
        
        # Random delay
        time.sleep(delay)
        
        print("\n🔴 PRESS ENTER NOW! 🔴")
        start_time = time.time()
        input()  # Wait for Enter key
        end_time = time.time()
        
        reaction_time = (end_time - start_time) * 1000  # Convert to milliseconds
        self.reaction_times.append(reaction_time)
        
        print(f"\nYour reaction time: {reaction_time:.2f} ms")
        self.rate_reaction(reaction_time)
        time.sleep(1.5)
    
    def rate_reaction(self, reaction_time):
        """Provide feedback on the reaction time."""
        if reaction_time < 200:
            print("⚡ AMAZING! Lightning fast!")
        elif reaction_time < 300:
            print("🌟 Excellent! Very quick!")
        elif reaction_time < 400:
            print("👍 Good! Above average!")
        elif reaction_time < 500:
            print("✓ Not bad! Keep practicing!")
        else:
            print("⏰ Could be better. Try to focus!")
    
    def display_statistics(self):
        """Display game statistics."""
        print("\n" + "="*50)
        print("GAME STATISTICS".center(50))
        print("="*50)
        
        avg_time = statistics.mean(self.reaction_times)
        best_time = min(self.reaction_times)
        worst_time = max(self.reaction_times)
        
        print(f"\nPlayer: {self.player_name}")
        print(f"Difficulty: {self.difficulty.upper()}")
        print(f"Rounds played: {len(self.reaction_times)}")
        print(f"\nAverage reaction time: {avg_time:.2f} ms")
        print(f"Best reaction time: {best_time:.2f} ms")
        print(f"Worst reaction time: {worst_time:.2f} ms")
        
        if len(self.reaction_times) > 1:
            stdev = statistics.stdev(self.reaction_times)
            print(f"Standard deviation: {stdev:.2f} ms")
        
        print("\nAll reaction times:")
        for i, rt in enumerate(self.reaction_times, 1):
            print(f"  Round {i}: {rt:.2f} ms")
    
    def save_high_score(self):
        """Save the player's score to the high scores file."""
        avg_time = statistics.mean(self.reaction_times)
        
        score_entry = {
            'name': self.player_name,
            'difficulty': self.difficulty,
            'avg_reaction_time': round(avg_time, 2),
            'best_time': round(min(self.reaction_times), 2),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        try:
            if os.path.exists(HIGH_SCORES_FILE):
                with open(HIGH_SCORES_FILE, 'r') as f:
                    scores = json.load(f)
            else:
                scores = []
            
            scores.append(score_entry)
            
            # Sort by average reaction time (lower is better)
            scores.sort(key=lambda x: x['avg_reaction_time'])
            
            # Keep only top 10 scores
            scores = scores[:10]
            
            with open(HIGH_SCORES_FILE, 'w') as f:
                json.dump(scores, f, indent=2)
            
            print("\n✓ Score saved to high scores!")
        except Exception as e:
            print(f"\n✗ Could not save score: {e}")
    
    def display_high_scores(self):
        """Display the high scores leaderboard."""
        try:
            if not os.path.exists(HIGH_SCORES_FILE):
                print("\nNo high scores yet. Be the first!")
                return
            
            with open(HIGH_SCORES_FILE, 'r') as f:
                scores = json.load(f)
            
            if not scores:
                print("\nNo high scores yet. Be the first!")
                return
            
            print("\n" + "="*50)
            print("🏆 HIGH SCORES LEADERBOARD 🏆".center(50))
            print("="*50)
            print(f"\n{'Rank':<6}{'Name':<15}{'Difficulty':<12}{'Avg Time':<12}{'Date':<20}")
            print("-"*65)
            
            for i, score in enumerate(scores, 1):
                print(f"{i:<6}{score['name']:<15}{score['difficulty']:<12}"
                      f"{score['avg_reaction_time']:<12}{score['date']:<20}")
        except Exception as e:
            print(f"\nError loading high scores: {e}")
    
    def play_game(self):
        """Main game loop."""
        self.clear_screen()
        self.display_banner()
        self.get_player_info()
        
        self.clear_screen()
        self.display_banner()
        self.countdown()
        
        config = DIFFICULTY_LEVELS[self.difficulty]
        
        for round_num in range(1, config['rounds'] + 1):
            self.play_round(round_num)
            if round_num < config['rounds']:
                print("\n" + "-"*50 + "\n")
        
        self.display_statistics()
        self.save_high_score()
        
        print("\n" + "="*50)
        input("\nPress Enter to continue...")

def main():
    """Main function to run the game."""
    while True:
        game = ReactionTimer()
        
        game.clear_screen()
        game.display_banner()
        
        print("1. Play Game")
        print("2. View High Scores")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            game.play_game()
        elif choice == '2':
            game.clear_screen()
            game.display_banner()
            game.display_high_scores()
            input("\nPress Enter to continue...")
        elif choice == '3':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
