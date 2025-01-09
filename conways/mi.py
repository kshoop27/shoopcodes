import random

def create_board(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]

def print_board(board):
    for row in board:
        print(''.join('*' if cell else '.' for cell in row))

def random_board(width, height):
    board = create_board(width, height)
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            board[i][j] = random.choice([0, 1])
    return board

def count_neighbors(board, x, y):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) != (x, y) and 0 <= i < len(board) and 0 <= j < len(board[0]):
                count += board[i][j]
    return count

def next_generation(board):
    new_board = create_board(len(board[0]), len(board))
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[0]) - 1):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == 1 and neighbors in [2, 3]:
                new_board[i][j] = 1
            elif board[i][j] == 0 and neighbors == 3:
                new_board[i][j] = 1
    return new_board

def run_game(width, height, generations):
    board = random_board(width, height)
    for _ in range(generations):
        print_board(board)
        board = next_generation(board)
        print("\n")

# Example usage
run_game(20, 20, 5)