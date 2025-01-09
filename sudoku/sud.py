import random
import time

def make_sudoku():
    grid = [[0 for column in range(9)] for row in range(9)]
    
    if fill_grid(grid):
        remove_numbers(grid)
        return grid
    else:
        return None

def fill_grid(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    
    row, col = empty
    
    for num in random.sample(range(1, 10), 9):
        if is_valid(grid, num, row, col):
            grid[row][col] = num
            
            if fill_grid(grid):
                return True
            
            grid[row][col] = 0
    
    return False

def remove_numbers(grid):
    for i in range(40):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while grid[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        grid[row][col] = 0

def is_valid(grid, num, row, col):
    if num in grid[row]:
        return False
    
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def print_grid(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else ".", end=" ")
        print()

puzzle = make_sudoku()

print("Sudoku Puzzle:")
print_grid(puzzle)

print("\nSolving...\n")

time.sleep(2) # make it look like its loading

fill_grid(puzzle)

print("Solution:")
print_grid(puzzle)