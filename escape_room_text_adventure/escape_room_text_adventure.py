#!/usr/bin/env python3
"""
Escape Room Text Adventure Game
A simple text-based adventure game where the player must solve puzzles to escape a virtual room.
"""

import sys
import time

class EscapeRoom:
    def __init__(self):
        self.inventory = []
        self.room_state = {
            'door_locked': True,
            'safe_opened': False,
            'painting_checked': False,
            'desk_searched': False,
            'key_found': False,
            'flashlight_on': False,
            'vent_opened': False,
            'code_found': False
        }
        self.safe_code = '7328'
        self.attempts = 0
        self.max_attempts = 3

    def print_slow(self, text, delay=0.03):
        """Print text with a typing effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def display_intro(self):
        """Display the introduction to the game"""
        self.print_slow("="*60)
        self.print_slow("ESCAPE ROOM: THE LOCKED CHAMBER")
        self.print_slow("="*60)
        self.print_slow("\nYou wake up in a dimly lit room with no memory of how you got here.")
        self.print_slow("The door is locked. You must find a way to escape!\n")
        time.sleep(1)

    def display_room(self):
        """Display the current state of the room"""
        print("\n" + "="*60)
        print("You see:")
        print("- A heavy wooden DOOR (locked)" if self.room_state['door_locked'] else "- The DOOR is now unlocked!")
        print("- A DESK with drawers")
        print("- A PAINTING on the wall")
        print("- A SAFE built into the wall")
        print("- An air VENT near the ceiling")
        print("- A WINDOW with bars")
        print("="*60)

    def display_inventory(self):
        """Display player's inventory"""
        if self.inventory:
            print("\nInventory:", ", ".join(self.inventory))
        else:
            print("\nInventory: Empty")

    def examine_desk(self):
        """Examine the desk"""
        if not self.room_state['desk_searched']:
            self.print_slow("\nYou search the desk thoroughly...")
            self.print_slow("You find a FLASHLIGHT in one of the drawers!")
            self.inventory.append('flashlight')
            self.room_state['desk_searched'] = True
        else:
            print("\nYou've already searched the desk. Nothing more to find here.")

    def examine_painting(self):
        """Examine the painting"""
        if 'flashlight' in self.inventory and not self.room_state['painting_checked']:
            self.print_slow("\nYou shine the flashlight on the painting...")
            self.print_slow("Behind the painting, you find a note!")
            self.print_slow("The note says: 'The code is the year I was born: 7328'")
            self.room_state['painting_checked'] = True
            self.room_state['code_found'] = True
        elif 'flashlight' not in self.inventory:
            print("\nIt's too dark to see the painting clearly. You need a light source.")
        else:
            print("\nYou've already checked behind the painting.")

    def open_safe(self):
        """Attempt to open the safe"""
        if self.room_state['safe_opened']:
            print("\nThe safe is already open. You see the KEY inside.")
            if 'key' not in self.inventory:
                print("You should TAKE the key.")
            return

        if self.attempts >= self.max_attempts:
            print("\nThe safe has locked permanently due to too many failed attempts.")
            print("Game Over! You're trapped forever!")
            sys.exit()

        print("\nThe safe has a 4-digit code lock.")
        if self.room_state['code_found']:
            print("You know the code: 7328")

        code = input("Enter the 4-digit code (or 'back' to return): ")
        
        if code.lower() == 'back':
            return
        
        if code == self.safe_code:
            self.print_slow("\n*Click* The safe opens!")
            self.print_slow("Inside, you find a shiny KEY!")
            self.room_state['safe_opened'] = True
        else:
            self.attempts += 1
            remaining = self.max_attempts - self.attempts
            print(f"\nIncorrect code! Attempts remaining: {remaining}")
            if remaining == 0:
                print("The safe has locked permanently!")
                print("Game Over!")
                sys.exit()

    def take_key(self):
        """Take the key from the safe"""
        if self.room_state['safe_opened'] and 'key' not in self.inventory:
            self.print_slow("\nYou take the KEY from the safe.")
            self.inventory.append('key')
            self.room_state['key_found'] = True
        elif 'key' in self.inventory:
            print("\nYou already have the key.")
        else:
            print("\nThere's no key to take. You need to find it first!")

    def examine_vent(self):
        """Examine the air vent"""
        print("\nThe vent is too high to reach and seems securely fastened.")
        print("It doesn't look like a viable escape route.")

    def examine_window(self):
        """Examine the window"""
        print("\nThe window has thick iron bars. You can see outside, but there's no way through.")

    def try_door(self):
        """Try to open the door"""
        if 'key' in self.inventory:
            self.print_slow("\nYou insert the key into the lock...")
            self.print_slow("*Click* The door unlocks!")
            self.print_slow("\nYou push the door open and step out into freedom!")
            self.print_slow("\n" + "="*60)
            self.print_slow("CONGRATULATIONS! YOU ESCAPED!")
            self.print_slow("="*60)
            self.room_state['door_locked'] = False
            return True
        else:
            print("\nThe door is locked. You need a key to open it.")
            return False

    def show_help(self):
        """Show available commands"""
        print("\n" + "="*60)
        print("Available Commands:")
        print("- LOOK: Look around the room")
        print("- DESK: Examine the desk")
        print("- PAINTING: Examine the painting")
        print("- SAFE: Try to open the safe")
        print("- VENT: Examine the vent")
        print("- WINDOW: Examine the window")
        print("- DOOR: Try to open the door")
        print("- TAKE KEY: Take the key from the safe")
        print("- INVENTORY: Check your inventory")
        print("- HELP: Show this help message")
        print("- QUIT: Exit the game")
        print("="*60)

    def play(self):
        """Main game loop"""
        self.display_intro()
        self.show_help()

        while True:
            self.display_room()
            self.display_inventory()
            
            command = input("\nWhat do you want to do? ").strip().lower()

            if command in ['look', 'l']:
                self.display_room()
            elif command in ['desk', 'examine desk', 'd']:
                self.examine_desk()
            elif command in ['painting', 'examine painting', 'p']:
                self.examine_painting()
            elif command in ['safe', 'open safe', 's']:
                self.open_safe()
            elif command in ['vent', 'examine vent', 'v']:
                self.examine_vent()
            elif command in ['window', 'examine window', 'w']:
                self.examine_window()
            elif command in ['door', 'try door', 'open door']:
                if self.try_door():
                    break
            elif command in ['take key', 'get key', 'take', 'key']:
                self.take_key()
            elif command in ['inventory', 'i', 'inv']:
                self.display_inventory()
            elif command in ['help', 'h', '?']:
                self.show_help()
            elif command in ['quit', 'exit', 'q']:
                print("\nThanks for playing! Goodbye!")
                break
            else:
                print("\nI don't understand that command. Type HELP for available commands.")

def main():
    """Main function to start the game"""
    game = EscapeRoom()
    game.play()

if __name__ == "__main__":
    main()
