#!/usr/bin/env python3
"""Multilingual Flashcard Learning System - Interactive language learning tool"""

import random
import json
import os
from typing import Dict, List

class MultilingualFlashcards:
    def __init__(self):
        self.flashcards = {
            'spanish': {'hola': 'hello', 'gracias': 'thank you', 'adiós': 'goodbye', 
                       'agua': 'water', 'casa': 'house', 'libro': 'book', 'gato': 'cat'},
            'french': {'bonjour': 'hello', 'merci': 'thank you', 'au revoir': 'goodbye',
                      'eau': 'water', 'maison': 'house', 'livre': 'book', 'chat': 'cat'},
            'german': {'hallo': 'hello', 'danke': 'thank you', 'auf wiedersehen': 'goodbye',
                      'wasser': 'water', 'haus': 'house', 'buch': 'book', 'katze': 'cat'}
        }
        self.score = 0
        self.total_questions = 0

    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("🌍 MULTILINGUAL FLASHCARD LEARNING SYSTEM 🌍")
        print("="*50)
        print("\nAvailable Languages:")
        for idx, lang in enumerate(self.flashcards.keys(), 1):
            print(f"{idx}. {lang.capitalize()} ({len(self.flashcards[lang])} words)")
        print(f"{len(self.flashcards) + 1}. Practice All Languages")
        print(f"{len(self.flashcards) + 2}. View Statistics")
        print(f"{len(self.flashcards) + 3}. Exit")

    def practice_language(self, language: str, num_questions: int = 5):
        """Practice flashcards for a specific language"""
        if language not in self.flashcards:
            print(f"❌ Language '{language}' not found!")
            return
        
        cards = list(self.flashcards[language].items())
        random.shuffle(cards)
        
        print(f"\n📚 Starting {language.capitalize()} practice ({num_questions} questions)\n")
        
        for i, (foreign, english) in enumerate(cards[:num_questions], 1):
            print(f"Question {i}/{num_questions}: Translate '{foreign}' to English")
            answer = input("Your answer: ").strip().lower()
            
            self.total_questions += 1
            if answer == english.lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {english}\n")

    def practice_all_languages(self, num_questions: int = 10):
        """Practice flashcards from all languages"""
        all_cards = []
        for lang, cards in self.flashcards.items():
            for foreign, english in cards.items():
                all_cards.append((foreign, english, lang))
        
        random.shuffle(all_cards)
        print(f"\n🌐 Practicing all languages ({num_questions} questions)\n")
        
        for i, (foreign, english, lang) in enumerate(all_cards[:num_questions], 1):
            print(f"Question {i}/{num_questions} [{lang.capitalize()}]: Translate '{foreign}'")
            answer = input("Your answer: ").strip().lower()
            
            self.total_questions += 1
            if answer == english.lower():
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer is: {english}\n")

    def show_statistics(self):
        """Display learning statistics"""
        print("\n" + "="*50)
        print("📊 YOUR STATISTICS")
        print("="*50)
        print(f"Total Questions Answered: {self.total_questions}")
        print(f"Correct Answers: {self.score}")
        if self.total_questions > 0:
            accuracy = (self.score / self.total_questions) * 100
            print(f"Accuracy: {accuracy:.1f}%")
        print("="*50)

    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("\nSelect an option: ").strip()
            
            if choice == '1':
                self.practice_language('spanish')
            elif choice == '2':
                self.practice_language('french')
            elif choice == '3':
                self.practice_language('german')
            elif choice == '4':
                self.practice_all_languages()
            elif choice == '5':
                self.show_statistics()
            elif choice == '6':
                print("\n👋 Thank you for practicing! Keep learning!")
                self.show_statistics()
                break
            else:
                print("\n❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    app = MultilingualFlashcards()
    app.run()
