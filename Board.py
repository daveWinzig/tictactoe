class Board:
    """
    Contains the game board and position data and the logic to update positions, display board, and reset board."
    """

    def __init__(self, size=3):
        self.size = size #number of rows and columns in board
        self.rows = size # number of rows in board
        self.columns = size # number of columns in board
        self.scores = [0,0]
        self.board = self.initBoard() # empty board of rows x columns size

    def initBoard(self):
        """
        create a board of rows x columns - starts with empty values
        """
        return [[None for column in range(self.columns)] for row in range(self.rows)]

    def renderBoard(self):
        """
        renderBoard prints a traditional tic tac toe board
        with the current kayout of X's and O's
        """

        rowDivider = ['---+---+---'] * (self.size - 1) #characters that divide board rows
        index = 0 #printed to describe location of cells to user

        #create and print rows from board
        #TODO, not great with boards other than 3 x 3
        for row in self.board:
            rowVals = []
            for col in row:
                if col:
                    rowVals.append(" " + col + " ")
                else:
                    rowVals.append(" " + str(index) + " ") # f"{index:03}" maybe format that at some point
                index += 1
            formattedRow = "|".join(rowVals)
            print(formattedRow)
            if rowDivider:
                print(rowDivider.pop())

    def locationToCoords(self, location):
        """
        Convert linear number to row, column coordinates on board.
        """

        row = location // self.size
        col = location % self.size

        return row,col
        
    def updateBoard(self, location, value):
        """
        Place a move on the board in a designated position
        value goes to board[row][col] 

        Numbering (for size 3 board):
        0 | 1 | 2
        3 | 4 | 5
        6 | 7 | 8 
        """
        
        row, col = locationToCoords(location)
        self.board[row][col] = value


    def resetBoard(self, reset=False):
        """
        Clear current game board
        Option to reset score
        """
        self.board = self.initBoard()

        if reset:
            self.scores = [0,0]

    