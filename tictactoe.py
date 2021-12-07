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
        
        for row in self.board:
            # switch in a box character fro empty values
            swappedInSpaces = ["-" if col == None else col for col in row]
            # join row characters together to form a single string to print
            formattedRow = "|".join(swappedInSpaces)

            print(formattedRow)

    def updateBoard(self, row, column, value):
        """
        Place a move on the board in a designated position
        value goes to board[row][col] 
        """

        #check value is an X or an O
        errors = []
        values = ['X', 'O']
        if value not in values:
            errors.append("Value needs to be an X or an O")
        if row < 0 or row >= self.rows:
            errors.append("Row index must be less than " + str(self.rows))
        if column < 0 or column >= self.columns:
            errors.append("Column index must be less than " + str(self.columns))

        if not errors :
            self.board[row][column] = value
        else:
            [print(error) for error in errors]

    def resetBoard(self, reset=False):
        """
        Clear current game board
        Option to reset score
        """
        self.board = self.initBoard()

        if reset:
            self.scores = [0,0]

    def XInARow(self):
        """
        Scan to see if there are X in a row
        Value - the game token to be checked.
        """

        result = dict()
        result['won'] = False
        result['winner'] = None
        XOMap = ['X','O']

        # row scan

        comp = [['X' for x in range(self.size)],['O' for x in range(self.size)]]
        rowResult = [x in self.board for x in comp]
            
        if True in rowResult:
            result['won'] = True
            result['winner'] = XOMap[rowResult.index(True)]

        # column scan
        for i in range(self.columns):
            inARow = 0
            compValue = self.board[0][i]
            for j in range(self.rows):
                if self.board[j][i] == compValue and compValue in XOMap:
                    inARow += 1
            if inARow == 3:
                result['won'] = True
                result['winner'] = compValue
                break

        return result