import os

"""
Contains functions to display game board and messages in the console.
"""

def clearScreen():

    os.system('cls' if os.name == 'nt' else 'clear')

def printGameIntro():
    """
    Print the welcome message and game rules
    """
    print("Tic Tac Toe")
    print("2 Players")
    print("Rules:")
    print("\t - First player is X's")
    print("\t - Second player is O's")
    print("\t - USe the numbers displayed in the board to select move position.")
    print("\n\n")

def printReadyToPlay():
    """
    Print message seeking to acknowledge players are ready.
    """
    print("Players, are you ready to play? (Yes/No)")

def printTurnIntro(board):
    """
    Prints message indicating which player is up.
    """
    player = board.nextMove

    print("Current turn: " + player)
    print("Please enter cell number to place your character: ")

def renderBoard(board):
        """
        Print a traditional tic tac toe board in a text based format.

        Like so:
             0 | 1 | 2 
            ---+---+---
             3 | 4 | 5
            ---+---+---
             6 | 7 | 8

        """
        #clear the screen first

        rowDivider = ['---+---+---'] * (board.size - 1) #characters that divide board rows
        index = 0 #printed to describe location of cells to user

        #create and print rows from board
        #TODO, not great with boards other than 3 x 3
        for row in board.board:
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


