def inarow_Neast(ch, r_start, c_start, A, N):
        """this should start from r_start and c_start and check for N-in-a-row eastward
     of element ch, returning True or False, as appropriate."""
    
        num_rows = len(A)     
        num_cols = len(A[0])

        if r_start < 0 or r_start >= num_rows:
            return False
    
        if c_start < 0 or c_start > num_cols - N:
            return False     
    
        for i in range(N):                  
            if A[r_start][c_start+i] != ch: 
                return False                

        return True      

def inarow_Nsouth(ch, r_start, c_start, A, N):
        """this should start from r_start and c_start and check for N-in-a-row
        southward of element ch, returning True or False, as appropriate."""
        num_rows = len(A)
        num_cols = len(A[0])

        if r_start < 0 or r_start >= num_rows - N:
            return False
        
        if c_start < 0 or c_start > num_cols - N:
            return False     
        
        for i in range(N):                  
            if A[r_start+i][c_start] != ch or r_start+i >= len(A): 
                return False                

        return True 
    

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
        """this should start from r_start and c_start and check for N-in-a-row
        southeastward of element ch, returning True or False, as appropriate."""
        num_rows = len(A)
        num_cols = len(A[0])

        if r_start < 0 or r_start >= num_rows - N:
            return False
        
        if c_start < 0 or c_start > num_cols - N:
            return False     
        
        for i in range(N):                  
            if A[r_start+i][c_start+i] != ch: 
                return False                

        return True 

def inarow_Nnortheast(ch, r_start, c_start, A, N):
        """This should start from r_start and c_start and check for N-in-a-row 
        northeastward of element ch, returning True or False, as appropriate."""
        num_rows = len(A)
        num_cols = len(A[0])

        if r_start < 0 or r_start >= num_rows:
            return False
        
        if c_start < 0 or c_start > num_cols - N:
            return False     
        
        for i in range(N):                  
            if A[r_start-i][c_start+i] != ch: 
                return False                

        return True 

class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]


    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # The string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-' + "\n"   # Bottom of the board

        s += '\n'
        for c in range(self.width):
            s += ' '
            if c > 9:
                s += str(c % 10)
            else:
                s += str(c)

        return s       # The board is complete; return it
    
    def addMove(self, col, ox):
        """This method takes two arguments: the first, col, represents the 
        index of the column to which the checker will be added. The second 
        argument, ox, will be a 1-character string representing the checker 
        to add to the board"""
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
            
        self.data[self.height-1][col] = ox

    
    def clear(self):
        """clears the board"""
        self.__init__(self.width, self.height)

    
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, c):
        """hus, this method should check to be sure that c is within the 
        range from 0 to the last column and make sure that there is still
          room left in the column!"""
        H = self.height
        W = self.width
        D = self.data

        if c < 0 or c >= W:
            return False
        elif D[0][c] != ' ':
            return False
        else:
            return True



    def isFull(self):
        """This method should return True if the calling object (of type Board) 
        is completely full of checkers. It should return False otherwise."""

        x = 0
        for c in range(self.width):
            if self.allowsMove(c):
                x += 1
    
        return x == 0
            
    
    def delMove(self, c):
        x = self.height - 1
        y = 0

        while y <= x:
            if self.data[y][c] != ' ':
                self.data[y][c] = ' '
                break
            y += 1


    

    def winsFor(self, ox):
        """checks if specific move ox, wins the game"""
        H = self.height
        W = self.width
        D = self.data

        # Check to see if ox wins, starting from any checker:
        for row in range(0, H):
            for col in range(0, W):
                if inarow_Neast(ox, row, col, D, 4) == True:
                    return True
        for row in range(0, H-3):
            for col in range(0, W):
                if D[row][col] == ox and D[row+1][col] == ox and D[row+2][col] == ox and D[row+3][col] == ox:
                    return True
        for row in range(0, H):
            for col in range (0, W):
                if inarow_Nnortheast(ox, row, col, D, 4) == True:
                    return True
        for row in range(0, H-3):
            for col in range(0, W-3):
                if D[row][col] == ox and D[row+1][col+1] == ox and D[row+2][col+2] == ox and D[row+3][col+3] == ox:
                    return True
        return False



    def colsToWin(self, ox):
        """the colsToWin method should return the list of columns where ox can
          move in the next turn in order to win and finish the game"""
        x = []
        for col in range(self.width):
            if self.allowsMove(col) == True:
                self.addMove(col, ox)
                if self.winsFor(ox):
                    x += [col] 
                self.delMove(col)

        return x
    

    def aiMove(self, ox):
        
        if ox == 'X':
            player = 'O'
        else:
            player = 'X'

        if self.colsToWin(ox) != []:
            return self.colsToWin(ox)[0]
        elif self.colsToWin(player) != []:
            return self.colsToWin(player)[0]
        else:
            for col in range(self.width):
                if self.allowsMove(col):
                    return col
                
    def hostGame(self):
        """ hosts a full game of Connect Four with an AI """
        print('Are you ready to play Connect Four!')
        print('')
        print(self)
        player = 'X'
        while True:
            users_col = -1
            while self.allowsMove(users_col) == False:
                print('')
                users_col = self.aiMove('X')
                users_col = int(users_col)
            print('')
            print(player, "'s choice: ", users_col)
            self.addMove(users_col, player)
            print('')
            print(self)
            if self.winsFor(player):
                print('')
                print(player, 'you have won - Congratulations!')
                print('')
                print(self)
                self.clear()
                break
            if player == 'X':
                player = 'O'
            else:
                player = 'X'



            


# This is the end of the Board class
# Below are some boards that will be re-created each time the file is run:

bigb = Board(15,5)
b = Board(7,6)
game = Board(7, 6)