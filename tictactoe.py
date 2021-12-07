def XInARow(board):
    """
    Scan to see if there are X in a row
    Value - the game token to be checked.
    """
    
    #results of scan
    result = dict() 
    result['won'] = False
    result['winner'] = None

    #used for reference
    XOMap = ['X','O']

    #size of (square) board
    size = len(board)

    # row scan
    comp = [['X' for x in range(size)],['O' for x in range(size)]]
    rowResult = [x in board for x in comp]
        
    if True in rowResult:
        result['won'] = True
        result['winner'] = XOMap[rowResult.index(True)]

    # column scan
    for i in range(size):
        inARow = 0
        compValue = board[0][i]
        for j in range(size):
            if board[j][i] == compValue and compValue in XOMap:
                inARow += 1
        if inARow == 3:
            result['won'] = True
            result['winner'] = compValue
            break

    #diagonal scan

    #TODO
    
    return result