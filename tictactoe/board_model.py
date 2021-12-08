class Board:
    """
    Contains the game board and position data and the logic to update positions and reset board."
    """

    def __init__(self, size=3):
        self.size = size #number of rows and columns in board
        self.scores = {'X' : 0, 'O' : 0} #player scores
        self.nextMove = 'X' #track current player
        self.XOMap = {'X' : 'O','O' : 'X'} #used for swapping player turns
        self.XO = ['X', 'O'] 
        self.board = self.initBoard() # empty board of rows x columns size


    def initBoard(self):
        """
        create a board of rows x columns - starts with empty values
        """
        return [[None for column in range(self.size)] for row in range(self.size)]


    def locationToCoords(self, location):
        """
        Convert linear number to row, column coordinates on board.
        """

        row = location // self.size
        col = location % self.size

        return row,col
        
    def updateBoard(self, location):
        """
        Place a move on the board in a designated position
        value goes to board[row][col] 

        Numbering (for size 3 board):
        0 | 1 | 2
        3 | 4 | 5
        6 | 7 | 8 

        Returns True if successful.
        """

        value = self.nextMove #get current player from 
        row, col = self.locationToCoords(location) #use player input to get board position

        #is the space open?
        if self.board[row][col] not in  self.XO:
        
            self.board[row][col] = value #update board

            self.nextMove = self.XOMap[value] #update next move
        
            return True

        #if space is occupado
        else:
            print("That space is occupied, try again...")
            return False


    def resetBoard(self, score=False):
        """
        Clear current game board
        Option to reset score
        """
        self.board = self.initBoard()

        if score:
            self.scores = {'X' : 0, 'O' : 0}

    def isDraw(self):
        """
        Determine if current game board represents a draw.
        Returns True if a draw.
        """
        for row in self.board:
            for col in row:
                if col == None:
                    return False
        
        return True


    def isWon(self):
        """
        Scan to see if there are X in a row
        Value - the game token to be checked.
        """
        
        #results of scan - includes whether game is won and if so, who the winner was
        result = dict() 
        result['won'] = False
        result['winner'] = None

        #size of (square) board
        size = len(self.board)

        # row scan
        comp = [['X' for x in range(size)],['O' for x in range(size)]]
        rowResult = [x in self.board for x in comp]
            
        if True in rowResult:
            result['won'] = True
            result['winner'] = self.XO[rowResult.index(True)]
            return result

        # column scan
        for i in range(size):
            inARow = 0
            compValue = self.board[0][i]
            for j in range(size):
                if self.board[j][i] == compValue and compValue in self.XO:
                    inARow += 1
            if inARow == 3:
                result['won'] = True
                result['winner'] = compValue
                return result

        #diagonal scan

        compValue = self.board[0][0]
        diag = False
        for i in range(3):
            diag = self.board[i][i] == compValue and compValue in self.XO

        if diag:
                    result['won'] = True
                    result['winner'] = compValue
                    return result

        refSize = self.size - 1
        compValue = self.board[0][refSize]
        diag = False
        for i in range(3):
            diag = self.board[i][refSize - i] == compValue and compValue in self.XO

        if diag:
            result['won'] = True
            result['winner'] = compValue
            return result
        
        return result

