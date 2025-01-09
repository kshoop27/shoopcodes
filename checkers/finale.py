import random
import math
import time
import webbrowser

class Board:
    """A data type representing a Checkers board with a dynamic grid."""

    def __init__(self):
        """Construct a Checkers board with a dynamic grid."""
        self.width = random.choice([4, 5, 6])
        self.height = random.choice([4, 5, 6])
        self.data = [[' ']*self.width for _ in range(self.height)]
        self.obstacles = set()
        self.move_counter = 0
        self.max_depth = 4
        self.transposition_table = {}

    def __repr__(self):
        """Return a string representation of the board with row numbers."""
        s = ' '
        for col in range(self.width):
            s += ' ' + str(col % 10)
        s += '\n'
        for row in range(self.height):
            s += str(row % 10) + '|'
            for col in range(self.width):
                if (row, col) in self.obstacles:
                    s += 'X|'  # Represent obstacles as 'X'
                else:
                    s += self.data[row][col] + '|'
            s += '\n'
        s += (2*self.width + 2) * '-' + "\n"
        return s

    def addPiece(self, row, col, piece):
        """Add a piece (X or O) to the board at the specified row and column."""
        self.data[row][col] = piece

    def addObstacles(self):
        """Add obstacles to the board randomly."""
        for _ in range(2):  # Add 2 obstacles
            while True:
                row = random.randint(0, self.height - 1)
                col = random.randint(0, self.width - 1)
                if (row, col) not in self.obstacles and self.data[row][col] == ' ':
                    self.obstacles.add((row, col))
                    break

    def clear(self):
        """Clear the board by resetting all slots to empty."""
        self.data = [[' ']*self.width for _ in range(self.height)]
        self.obstacles = set()

    def isValidMove(self, row, col):
        """Check if the given row and column represent a valid move."""
        return 0 <= row < self.height and 0 <= col < self.width and self.data[row][col] == ' ' and (row, col) not in self.obstacles

    def getValidMoves(self):
        """Return a list of valid moves (row, col) on the board."""
        return [(row, col) for row in range(self.height) for col in range(self.width) if self.data[row][col] == ' ' and (row, col) not in self.obstacles]

    def clone(self):
        """Return a copy of the board."""
        clone_board = Board()
        clone_board.data = [row[:] for row in self.data]
        clone_board.obstacles = self.obstacles.copy()
        clone_board.move_counter = self.move_counter
        return clone_board

    def hasWinner(self, piece):
        """Check if the specified piece has won the game."""
        # Check rows
        for row in range(self.height):
            if all(cell == piece for cell in self.data[row]):
                return True

        # Check columns
        for col in range(self.width):
            if all(self.data[row][col] == piece for row in range(self.height)):
                return True

        # Check diagonals
        if all(self.data[i][i] == piece for i in range(min(self.width, self.height))) or \
           all(self.data[i][self.width - 1 - i] == piece for i in range(min(self.width, self.height))):
            return True

        return False

    def isFull(self):
        """Check if the board is completely full of pieces."""
        # print([[cell != ' ' for cell in row] for row in self.data])
        return all(cell != ' ' for row in self.data for cell in row if (self.data.index(row), row.index(cell)) not in self.obstacles)
        # for row in range(self.height):
        #     for col in range(self.width):
        #         if self.data[row][col] == " ":
        #             return False

        # return True
    

    def undoMove(self, row, col):
        """Undo the move at the specified row and column."""
        self.data[row][col] = ' '

    def minimax(self, depth, alpha, beta, maximizingPlayer):
        """Implement the minimax algorithm with alpha-beta pruning."""
        if depth == 0 or self.hasWinner('X') or self.hasWinner('O') or self.isFull():
            return self.evaluate(), None

        if maximizingPlayer:
            max_eval = -math.inf
            best_move = None
            for move in self.getValidMoves():
                row, col = move
                self.addPiece(row, col, 'O')
                eval, _ = self.minimax(depth - 1, alpha, beta, False)
                self.undoMove(row, col)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            best_move = None
            for move in self.getValidMoves():
                row, col = move
                self.addPiece(row, col, 'X')
                eval, _ = self.minimax(depth - 1, alpha, beta, True)
                self.undoMove(row, col)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate(self):
        """Evaluate the current state of the board."""
        if self.hasWinner('X'):
            return -1
        elif self.hasWinner('O'):
            return 1
        else:
            return 0

    def playGame(self):
        """Host a game of Checkers against the computer with a live scoreboard."""
        player_score = 0
        ai_score = 0
        print("Welcome to Checkers!\n")
        print(self)

        while True:
            # Add obstacles every 4 moves
            if self.move_counter % 4 == 0:
                self.addObstacles()
                print("\nObstacles added:")
                print(self)

            # Player's turn
            while True:
                player_move = input("Your move (row col): ")
                try:
                    row, col = map(int, player_move.split())
                    if self.isValidMove(row, col):
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter two integers separated by a space.")

            self.addPiece(row, col, 'X')
            print("\n" + str(self))

            if self.hasWinner('X'):
                print("\nYou win--Congratulations!\n")
                player_score += 1
                print(f"Player Score: {player_score} | AI Score: {ai_score}\n")
                return 'X'  # Player wins

            if self.isFull():
                print("\nThe game is a tie!\n")
                print(f"Player Score: {player_score} | AI Score: {ai_score}\n")
                return 'TIE'  # Tie

            self.move_counter += 1

            # Allow undo or change opponent's move after 6 moves
            if self.move_counter >= 6:
                while True:
                    undo_option = input("Do you want to undo (U) or change (C) opponent's move? (U/C): ")
                    if undo_option.upper() == 'U':
                        while True:
                            undo_move = input("Enter opponent's move to undo (row col): ")
                            try:
                                undo_row, undo_col = map(int, undo_move.split())
                                if 0 <= undo_row < self.height and 0 <= undo_col < self.width:  # Check if within bounds
                                    if self.data[undo_row][undo_col] == 'O':
                                        self.undoMove(undo_row, undo_col)
                                        break
                                    else:
                                        print("Invalid move. Try again.")
                                else:
                                    print("Row and column must be within the board's dimensions. Try again.")
                            except ValueError:
                                print("Invalid input. Please enter two integers separated by a space.")
                        break
                    elif undo_option.upper() == 'C':
                        while True:
                            change_move = input("Enter new position for opponent's move (row col): ")
                            try:
                                change_row, change_col = map(int, change_move.split())
                                if self.isValidMove(change_row, change_col):
                                    self.addPiece(change_row, change_col, 'O')
                                    break
                                else:
                                    print("Invalid move. Try again.")
                            except ValueError:
                                print("Invalid input. Please enter two integers separated by a space.")
                        break
                    else:
                        print("Invalid option. Please enter 'U' for undo or 'C' for change.")

            # Computer's turn
            start_time = time.time()
            best_eval, best_move = -math.inf, None
            for d in range(1, self.max_depth + 1):
                eval, move = self.minimax(d, -math.inf, math.inf, True)
                if time.time() - start_time > 3:  # Time limit for move calculation
                    break
                best_eval, best_move = eval, move

            if best_move:
                row, col = best_move
                self.addPiece(row, col, 'O')
                print(f"\nComputer's move: {row} {col}")
                print("\n" + str(self))

            if self.hasWinner('O'):
                print("\nComputer wins. Better luck next time!\n")
                ai_score += 1
                print(f"Player Score: {player_score} | AI Score: {ai_score}\n")
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                return 'O'  # Computer wins

if __name__ == "__main__":
    board = Board()
    winner = board.playGame()
