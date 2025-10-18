#!/usr/bin/env python3
"""
Number Puzzle Solver - A 3x3 Sliding Puzzle Game
Solves the classic 8-puzzle problem using A* algorithm
"""

import heapq
from typing import List, Tuple, Optional


class PuzzleState:
    """Represents a state in the puzzle"""
    
    def __init__(self, board: List[List[int]], moves: int = 0, previous=None):
        self.board = [row[:] for row in board]
        self.moves = moves
        self.previous = previous
        self.blank_pos = self.find_blank()
        
    def find_blank(self) -> Tuple[int, int]:
        """Find the position of the blank (0) tile"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return (0, 0)
    
    def manhattan_distance(self) -> int:
        """Calculate Manhattan distance heuristic"""
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    target_row = (self.board[i][j] - 1) // 3
                    target_col = (self.board[i][j] - 1) % 3
                    distance += abs(i - target_row) + abs(j - target_col)
        return distance
    
    def __lt__(self, other):
        return (self.moves + self.manhattan_distance()) < (other.moves + other.manhattan_distance())
    
    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))
    
    def __eq__(self, other):
        return self.board == other.board
    
    def is_goal(self) -> bool:
        """Check if current state is the goal state"""
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal
    
    def get_neighbors(self) -> List['PuzzleState']:
        """Generate all possible next states"""
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col = self.blank_pos
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = [r[:] for r in self.board]
                new_board[row][col], new_board[new_row][new_col] = \
                    new_board[new_row][new_col], new_board[row][col]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        
        return neighbors


def solve_puzzle(initial_board: List[List[int]]) -> Optional[List[List[List[int]]]]:
    """Solve the puzzle using A* algorithm"""
    start_state = PuzzleState(initial_board)
    
    if start_state.is_goal():
        return [start_state.board]
    
    open_set = [start_state]
    closed_set = set()
    
    while open_set:
        current = heapq.heappop(open_set)
        
        if current.is_goal():
            path = []
            while current:
                path.append(current.board)
                current = current.previous
            return path[::-1]
        
        closed_set.add(current)
        
        for neighbor in current.get_neighbors():
            if neighbor not in closed_set:
                heapq.heappush(open_set, neighbor)
    
    return None


if __name__ == "__main__":
    # Example puzzle
    puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    
    print("Initial State:")
    for row in puzzle:
        print(row)
    
    solution = solve_puzzle(puzzle)
    
    if solution:
        print(f"\nSolved in {len(solution) - 1} moves!\n")
        for i, state in enumerate(solution):
            print(f"Step {i}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found!")
