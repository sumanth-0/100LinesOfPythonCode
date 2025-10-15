#!/usr/bin/env python3
"""
Email Subject Line Generator
Generates catchy email subject lines for newsletters or promotions
using random templates and adjectives.
"""

import random
import argparse
from typing import List, Dict


class EmailSubjectGenerator:
    """Generate engaging email subject lines for marketing campaigns."""

    def __init__(self):
        """Initialize the generator with templates and word lists."""
        self.adjectives = [
            "Amazing", "Exclusive", "Limited", "Incredible", "Stunning",
            "Revolutionary", "Ultimate", "Perfect", "Essential", "Premium",
            "Fantastic", "Spectacular", "Remarkable", "Extraordinary", "Unbeatable",
            "Outstanding", "Brilliant", "Magnificent", "Superb", "Exceptional"
        ]

        self.action_verbs = [
            "Discover", "Unlock", "Explore", "Grab", "Get",
            "Claim", "Secure", "Seize", "Don't Miss", "Transform"
        ]

        self.urgency_words = [
            "Today", "Now", "This Week", "Right Now", "Immediately",
            "Limited Time", "Last Chance", "Ending Soon", "While Supplies Last"
        ]

        self.templates = [
            "{action} {adjective} {offer}",
            "{adjective} {offer} - {urgency}!",
            "{urgency}: {action} Your {adjective} {offer}",
            "🎁 {adjective} {offer} Inside!",
            "{action} {number}% Off {adjective} {offer}",
            "⚡ {urgency}: {adjective} {offer} Available",
            "{adjective} {offer} You Can't Miss",
            "Hey! {action} This {adjective} {offer}",
            "{number} Reasons to Try Our {adjective} {offer}",
            "Your {adjective} {offer} Awaits - {urgency}!"
        ]

        self.offers = [
            "Deal", "Offer", "Discount", "Sale", "Collection",
            "Products", "Selection", "Bundle", "Package", "Opportunity"
        ]

    def generate_subject(self, category: str = "general") -> str:
        """
        Generate a random email subject line.

        Args:
            category: The category of subject line (general, sale, newsletter)

        Returns:
            A formatted email subject line
        """
        template = random.choice(self.templates)
        subject = template.format(
            action=random.choice(self.action_verbs),
            adjective=random.choice(self.adjectives),
            offer=random.choice(self.offers),
            urgency=random.choice(self.urgency_words),
            number=random.choice([10, 20, 30, 40, 50])
        )
        return subject

    def generate_multiple(self, count: int = 5) -> List[str]:
        """
        Generate multiple subject lines.

        Args:
            count: Number of subject lines to generate

        Returns:
            List of generated subject lines
        """
        return [self.generate_subject() for _ in range(count)]


def main():
    """Main function to run the subject line generator."""
    parser = argparse.ArgumentParser(
        description="Generate catchy email subject lines"
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        default=5,
        help="Number of subject lines to generate (default: 5)"
    )
    args = parser.parse_args()

    generator = EmailSubjectGenerator()
    print("\n📧 Email Subject Line Generator\n")
    print("="*50)

    subjects = generator.generate_multiple(args.number)
    for i, subject in enumerate(subjects, 1):
        print(f"{i}. {subject}")

    print("="*50)
    print(f"\nGenerated {len(subjects)} subject lines!\n")


if __name__ == "__main__":
    main()
