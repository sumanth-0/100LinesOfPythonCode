#!/usr/bin/env python3
"""Escape Room Text Adventure - A simple text-based escape room game."""

import random
import sys

class EscapeRoom:
    def __init__(self):
        self.inventory = []
        self.room_state = {
            'door_locked': True,
            'light_on': False,
            'safe_opened': False,
            'painting_examined': False,
            'code_found': False
        }
        self.safe_code = "2468"
        
    def show_intro(self):
        print("\n" + "="*60)
        print("     ESCAPE ROOM TEXT ADVENTURE")
        print("="*60)
        print("\nYou wake up in a dimly lit room. The door is locked.")
        print("You need to find a way to escape!\n")
        print("Commands: look, examine [item], take [item], use [item],")
        print("          inventory, help, quit\n")
        
    def show_room(self):
        if not self.room_state['light_on']:
            print("\nThe room is dimly lit. You can barely see anything.")
        else:
            print("\nThe room is now brightly lit. You can see clearly.")
        print("You see: a door, a light switch, a desk, a painting, and a safe.")
        
    def examine(self, item):
        item = item.lower()
        if item in ['door', 'exit']:
            if self.room_state['door_locked']:
                print("The door is locked. It needs a key.")
            else:
                print("The door is unlocked. You can now escape!")
        elif item in ['light', 'switch', 'light switch']:
            if self.room_state['light_on']:
                print("The light switch is ON. The room is bright.")
            else:
                print("The light switch is OFF. Try using it.")
        elif item == 'desk':
            if not self.room_state['light_on']:
                print("It's too dark to see the desk clearly.")
            else:
                print("A wooden desk with a drawer. There's a flashlight on it.")
        elif item == 'painting':
            self.room_state['painting_examined'] = True
            print("A beautiful landscape painting. Behind it, you find a note!")
            print("The note says: 'The code is my favorite even numbers.'")
            self.room_state['code_found'] = True
        elif item == 'safe':
            if self.room_state['safe_opened']:
                print("The safe is open and empty now.")
            else:
                print("A digital safe with a 4-digit code panel.")
        else:
            print(f"You can't examine '{item}'.")
            
    def take(self, item):
        item = item.lower()
        if item == 'flashlight' and 'flashlight' not in self.inventory:
            if self.room_state['light_on']:
                self.inventory.append('flashlight')
                print("You took the flashlight.")
            else:
                print("It's too dark to find the flashlight.")
        elif item == 'key' and 'key' not in self.inventory:
            if self.room_state['safe_opened']:
                self.inventory.append('key')
                print("You took the key from the safe!")
            else:
                print("You don't see a key.")
        else:
            print(f"You can't take '{item}'.")
            
    def use(self, item):
        item = item.lower()
        if item in ['light', 'switch', 'light switch']:
            self.room_state['light_on'] = not self.room_state['light_on']
            if self.room_state['light_on']:
                print("You turned ON the light. The room brightens!")
            else:
                print("You turned OFF the light.")
        elif item == 'key' and 'key' in self.inventory:
            self.room_state['door_locked'] = False
            print("You used the key to unlock the door!")
            print("\n" + "="*60)
            print("     CONGRATULATIONS! YOU ESCAPED!")
            print("="*60)
            return True
        else:
            print(f"You can't use '{item}'.")
        return False
        
    def open_safe(self, code):
        if code == self.safe_code:
            self.room_state['safe_opened'] = True
            print("The safe opens! Inside, you find a KEY!")
            return True
        else:
            print("Wrong code. The safe remains locked.")
            return False
            
    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Inventory:", ", ".join(self.inventory))
            
    def show_help(self):
        print("\nCommands:")
        print("  look - Look around the room")
        print("  examine [item] - Examine an item")
        print("  take [item] - Take an item")
        print("  use [item] - Use an item")
        print("  open safe [code] - Try to open the safe with a code")
        print("  inventory - Show your inventory")
        print("  help - Show this help")
        print("  quit - Exit the game\n")

def main():
    game = EscapeRoom()
    game.show_intro()
    game.show_room()
    
    while True:
        try:
            command = input("\n> ").strip().lower()
            
            if not command:
                continue
            elif command == 'quit':
                print("Thanks for playing!")
                break
            elif command == 'look':
                game.show_room()
            elif command.startswith('examine '):
                item = command[8:].strip()
                game.examine(item)
            elif command.startswith('take '):
                item = command[5:].strip()
                game.take(item)
            elif command.startswith('use '):
                item = command[4:].strip()
                if game.use(item):
                    break
            elif command.startswith('open safe '):
                code = command[10:].strip()
                game.open_safe(code)
            elif command == 'inventory':
                game.show_inventory()
            elif command == 'help':
                game.show_help()
            else:
                print("Unknown command. Type 'help' for commands.")
        except KeyboardInterrupt:
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
