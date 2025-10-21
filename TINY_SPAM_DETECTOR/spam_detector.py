#!/usr/bin/env python3
"""
Tiny Spam Message Detector
A simple spam detection system using rule-based and ML approaches
For issue #681 in 100LinesOfPythonCode
"""

import re
import argparse
from collections import Counter
from typing import List, Tuple
import random

# Common spam keywords and patterns
SPAM_KEYWORDS = [
    'winner', 'congratulations', 'prize', 'free', 'click here', 'urgent',
    'act now', 'limited time', 'offer', 'cash', 'bonus', 'guarantee',
    'risk free', 'no obligation', 'call now', 'order now', 'buy now',
    'discount', 'save money', 'earn money', 'work from home', 'investment',
    'viagra', 'pharmacy', 'weight loss', 'credit card', 'loan approved'
]

# Simple training dataset
TRAINING_DATA = [
    ("Congratulations! You've won a free prize! Click here to claim!", 1),
    ("Hey, are we still meeting for lunch tomorrow?", 0),
    ("URGENT: Your account needs verification. Act now!", 1),
    ("Thanks for the meeting notes. I'll review them tonight.", 0),
    ("Limited time offer! Buy now and save 90%!", 1),
    ("Can you send me the project report by Friday?", 0),
    ("FREE MONEY! Click this link to earn $5000 daily!", 1),
    ("I'll be working from home tomorrow.", 0),
    ("You have been selected for a special discount on Viagra!", 1),
    ("Let's schedule a call to discuss the proposal.", 0),
]

class SpamDetector:
    """A hybrid spam detector using rule-based and statistical methods"""
    
    def __init__(self):
        self.spam_word_freq = Counter()
        self.ham_word_freq = Counter()
        self.trained = False
        
    def extract_features(self, text: str) -> dict:
        """Extract features from text for classification"""
        text_lower = text.lower()
        
        features = {
            'length': len(text),
            'num_urls': len(re.findall(r'http[s]?://|www\.', text)),
            'num_exclamations': text.count('!'),
            'num_uppercase': sum(1 for c in text if c.isupper()),
            'has_money_symbol': '$' in text or '£' in text or '€' in text,
            'num_digits': sum(1 for c in text if c.isdigit()),
            'spam_keyword_count': sum(1 for kw in SPAM_KEYWORDS if kw in text_lower),
        }
        
        return features
    
    def rule_based_score(self, text: str) -> float:
        """Calculate spam score using rule-based approach"""
        features = self.extract_features(text)
        score = 0.0
        
        # Weight different features
        score += features['spam_keyword_count'] * 15
        score += features['num_exclamations'] * 5
        score += features['num_urls'] * 10
        score += features['has_money_symbol'] * 8
        
        # High uppercase ratio is suspicious
        if features['length'] > 0:
            uppercase_ratio = features['num_uppercase'] / features['length']
            if uppercase_ratio > 0.3:
                score += 20
        
        return min(score, 100)  # Cap at 100
    
    def train(self, messages: List[Tuple[str, int]]):
        """Train the detector with labeled messages"""
        for text, label in messages:
            words = text.lower().split()
            
            if label == 1:  # Spam
                self.spam_word_freq.update(words)
            else:  # Ham (not spam)
                self.ham_word_freq.update(words)
        
        self.trained = True
    
    def ml_based_score(self, text: str) -> float:
        """Calculate spam probability using simple Naive Bayes approach"""
        if not self.trained:
            return 50.0  # Neutral if not trained
        
        words = text.lower().split()
        spam_score = 1.0
        ham_score = 1.0
        
        for word in words:
            # Add smoothing to avoid zero probabilities
            spam_count = self.spam_word_freq.get(word, 0) + 1
            ham_count = self.ham_word_freq.get(word, 0) + 1
            
            spam_score *= spam_count
            ham_score *= ham_count
        
        # Normalize to percentage
        total = spam_score + ham_score
        return (spam_score / total) * 100 if total > 0 else 50.0
    
    def predict(self, text: str) -> Tuple[bool, float]:
        """Predict if a message is spam"""
        rule_score = self.rule_based_score(text)
        ml_score = self.ml_based_score(text)
        
        # Combine scores (weighted average)
        combined_score = (rule_score * 0.6) + (ml_score * 0.4)
        
        is_spam = combined_score > 50
        return is_spam, combined_score

def test_accuracy(detector: SpamDetector, test_data: List[Tuple[str, int]]) -> float:
    """Test the detector's accuracy on test data"""
    correct = 0
    total = len(test_data)
    
    print("\n=== Testing Spam Detector ===")
    for text, actual_label in test_data:
        predicted_spam, confidence = detector.predict(text)
        predicted_label = 1 if predicted_spam else 0
        
        if predicted_label == actual_label:
            correct += 1
            result = "✓ CORRECT"
        else:
            result = "✗ WRONG"
        
        print(f"{result} | Confidence: {confidence:.1f}% | Text: {text[:50]}...")
    
    accuracy = (correct / total) * 100
    print(f"\nAccuracy: {correct}/{total} ({accuracy:.1f}%)")
    return accuracy

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(description='Tiny Spam Message Detector')
    parser.add_argument('message', nargs='?', help='Message to check for spam')
    parser.add_argument('--test', action='store_true', help='Run accuracy test')
    parser.add_argument('--interactive', '-i', action='store_true', help='Interactive mode')
    
    args = parser.parse_args()
    
    # Initialize and train detector
    detector = SpamDetector()
    detector.train(TRAINING_DATA)
    
    if args.test:
        # Run accuracy test
        test_accuracy(detector, TRAINING_DATA)
    elif args.interactive:
        # Interactive mode
        print("=== Spam Detector Interactive Mode ===")
        print("Type 'quit' to exit\n")
        
        while True:
            message = input("Enter message to check: ").strip()
            if message.lower() == 'quit':
                break
            
            is_spam, confidence = detector.predict(message)
            status = "SPAM" if is_spam else "HAM (Not Spam)"
            print(f"Result: {status} (Confidence: {confidence:.1f}%)\n")
    elif args.message:
        # Single message check
        is_spam, confidence = detector.predict(args.message)
        status = "SPAM" if is_spam else "HAM (Not Spam)"
        print(f"Message: {args.message}")
        print(f"Result: {status}")
        print(f"Confidence: {confidence:.1f}%")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
