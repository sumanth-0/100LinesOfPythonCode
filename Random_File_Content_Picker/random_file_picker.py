#!/usr/bin/env python3
import random
import os
import sys


def get_random_line(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
            
        if not lines:
            print("Error: The file is empty or contains no valid lines.")
            return None
            
        return random.choice(lines)
        
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except PermissionError:
        print(f"Error: Permission denied: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def create_sample_file(file_path):
    """Create a sample quotes file if it doesn't exist."""
    sample_quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Life is what happens to you while you're busy making other plans. - John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It is during our darkest moments that we must focus to see the light. - Aristotle",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Don't let yesterday take up too much of today. - Will Rogers",
        "You learn more from failure than from success. Don't let it stop you. - Unknown",
        "If you are working on something that you really care about, you don't have to be pushed. - Steve Jobs",
        "Experience is a hard teacher because she gives the test first, the lesson afterward. - Vernon Law",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
    ]
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for quote in sample_quotes:
                file.write(quote + '\n')
        print(f"Created sample file: {file_path}")
        return True
    except Exception as e:
        print(f"Error creating sample file: {e}")
        return False


def main():
    """Main function to run the random file content picker."""
    print("Random File Content Picker")
    print("=" * 40)
    
    # Check if file path is provided as command line argument
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Interactive mode
        file_path = input("Enter file path (or press Enter for sample quotes): ").strip()
        
        # Use default sample file if no path provided
        if not file_path:
            file_path = "sample_quotes.txt"
            
            # Create sample file if it doesn't exist
            if not os.path.exists(file_path):
                print("\nNo file specified. Creating sample quotes file...")
                if not create_sample_file(file_path):
                    return
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"\nError: File does not exist: {file_path}")
        
        # Offer to create sample file
        if input("Create a sample quotes file? (y/n): ").lower().startswith('y'):
            file_path = "sample_quotes.txt"
            if not create_sample_file(file_path):
                return
        else:
            return
    
    # Get and display random line
    print(f"\nReading from: {file_path}")
    random_line = get_random_line(file_path)
    
    if random_line:
        print("\n" + "=" * 50)
        print("Random Pick:")
        print(f"   {random_line}")
        print("=" * 50)
        
        # Show file stats
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                total_lines = len([line for line in file if line.strip()])
            print(f"\nFile contains {total_lines} lines")
        except:
            pass


if __name__ == "__main__":
    main()