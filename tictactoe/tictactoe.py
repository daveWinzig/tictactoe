import board_model, board_view, validate


if __name__ == "__main__":

    #game board
    board = board_model.Board()

    #welcome message
    board_view.printGameIntro()

    #player input to continue 
    board_view.printReadyToPlay()
    user = input()

    #quick check on input - exception if fails check
    validate.doesInputMatch(user, "Yes", "No", "Y", "N", "yes", "no", "y", "n")

    #end program if user selects not to continue
    if user[0].lower() == 'n':
        quit()
    
    #main game loop
    won = False #loop while game in progress
    while(not won):
        #display the initial board (contains number positions)
        board_view.renderBoard(board)
        print("\n")


        #ask for move
        success = False
        while(not success):
            board_view.printTurnIntro(board)
            move = int(input())

            #quick check on input - exception if fails check
            validate.isInputIntInRange(move, board.size ** 2)

            #try to update board
            success = board.updateBoard(move)

        result = board.XInARow()
        won = result['won']
        

    print(result['winner'] + " is the Winner!")

