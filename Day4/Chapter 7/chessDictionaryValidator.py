import sys
"""
Check for:
v One white King
v One black King
v each player max 16 pieces
v Only 8 pawns per player
v All pieces must be on squares 1a to 8h
v Pieces should begin with w or b
- After should be P, K, Q, N, B, R
"""
boardState = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}
piecesMaxFreq = {'wK':1,'wQ':1,'wP':8,'bK':1,'bQ':1,'bP':8}
allPieces = ['wK', 'wQ', 'wB', 'wN', 'wR', 'wP', 'bK', 'bQ', 'bB', 'bN', 'bR', 'bP']

def checkFreq2(board):
    boardFreq = {}          
    wFreq = 0
    bFreq = 0
    for square, piece in board.items():                                                            # Loop over board
        if square[1] not in '12345678' or square[0] not in 'abcdefgh':                        # Check if piece is on a valid square and valid piece
            print('This board is not valid, a piece is on an invalid square.')
            exit()
        elif piece not in allPieces:                  
            print('This board is not valid, there is a wrong piece on it')

        if piece[0] == 'w':                                                             # Check how many white and black pieces there are
            wFreq += 1
        elif piece[0] == 'b':
            bFreq += 1
        else:
            print('This board is not valid, there is a piece on it that is niether black nor white')
            exit()

        boardFreq.setdefault(piece, 0)
        boardFreq[piece] += 1

    if wFreq > 16 or bFreq > 16:                                                    # After loop check if there are not too many w/b piecees
        print('This board is not valid, one side has too many pieces.')
        print(wFreq, bFreq)
        exit()

    for piece, maxAmount in piecesMaxFreq.items():                                                 # After loop check if there are not too many individual pieces
        if boardFreq.get(piece, 0) > maxAmount:
            print('This board is not valid, ther is an invalid amount of pieces on it')
            exit()


checkFreq2(boardState)
print('This board is valid')


