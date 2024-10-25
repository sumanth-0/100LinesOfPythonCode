import random
import os

class Game:
    def __init__(self):
        self.matrix = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()
        
    def add_new_tile(self): # Add a new tile in an empty spot
        if any(0 in row for row in self.matrix):
            row, col = random.choice([(r, c) for r in range(4) for c in range(4) if self.matrix[r][c] == 0])
            self.matrix[row][col] = random.choice([2, 4])

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Score: {self.score}\n" + "\n".join("".join(f"{num:>4}" for num in row) for row in self.matrix))

    def stack(self): # Shift non-zero tiles left
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    self.matrix[i][fill_position] = self.matrix[i][j]
                    fill_position += 1
            self.matrix[i][fill_position:] = [0] * (4 - fill_position) # Fill remaining spaces with 0

    def combine(self): # Merge tiles and update score
        combined = False
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2 # Combine tiles
                    self.score += self.matrix[i][j]
                    self.matrix[i][j + 1] = 0 # Set the combined tile position to 0
                    combined = True
        return combined

    def move_left(self):
        # Move tiles to the left and check if the matrix has changed
        old_matrix = [row[:] for row in self.matrix]
        self.stack()
        self.combine()
        self.stack()
        return old_matrix != self.matrix

    def move_right(self):
        # Move tiles to the right by reversing the rows
        self.matrix = [row[::-1] for row in self.matrix]
        moved = self.move_left()
        self.matrix = [row[::-1] for row in self.matrix]
        return moved

    def move_up(self):
        self.transpose() 
        moved = self.move_left()
        self.transpose()
        return moved

    def move_down(self):
        self.transpose() 
        moved = self.move_right()
        self.transpose()
        return moved

    def transpose(self): # Switch rows and columns
        self.matrix = [list(row) for row in zip(*self.matrix)]

    def game_over(self): # Check if reached 2048 or no moves left
        if any(2048 in row for row in self.matrix):
            print("You Win!")
            return True
        if not any(0 in row for row in self.matrix):
            return all(self.matrix[i][j] != self.matrix[i][j + 1] and (i == 3 or self.matrix[i][j] != self.matrix[i + 1][j]) for i in range(4) for j in range(3))
        return False

    def play(self):
        while True:
            self.display() # Display the current state
            move = input("Enter move (w: up, a: left, s: down, d: right) or 'exit' to quit: ").strip().lower()
            if move == 'exit':
                print("Goodbye!")
                break
            moved = (move == 'a' and self.move_left()) or (move == 'd' and self.move_right()) or (move == 'w' and self.move_up()) or (move == 's' and self.move_down())
            if moved: # Add a new tile after a move
                self.add_new_tile()
            if self.game_over(): # Check for game over condition
                self.display()
                print("Game Over!")
                break

if __name__ == "__main__":
    Game().play()
