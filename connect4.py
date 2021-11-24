import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def createBoard():
    board = np.zeros((ROW_COUNT,COL_COUNT)) # Buat tabel 6 x 7
    return board

def dropPiece(board, row, col, piece):
    board[row][col] = piece # piece = nomor player, ini udah jelas lah ya

def isValidLocation(board, col):
    return board[ROW_COUNT-1][col] == 0 # Cek kolom udah penuh ato belum.

def getNextOpenRow(board, col):
    for row in range(ROW_COUNT): # Memeriksa setiap baris pada suatu kolom jika ada spot kosong untuk di drop piece.
        if board[row][col] == 0:
            return row

def printBoard(board):
    print(np.flip(board, 0)) # Kalo gk ada fungsi ini connect 4 bakal kebalik

def winningMove(board, piece):
    # Check horizontal locations for win
    for col in range(COL_COUNT-3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    
    # Check vertical locations for win
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    
    # Check positive sloped diagonals for win
    for col in range(COL_COUNT-3):
        for row in range(ROW_COUNT-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True
    # Check negatively sloped diagonals for win
    for col in range(COL_COUNT-3):
        for row in range(3, ROW_COUNT-3):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
    

board = createBoard() # Buat papan connect 4
printBoard(board) # Initial Game State
gameOver = False
turn = 0

while not gameOver:
    # Prompt player 1 for input
    if turn == 0:
        col = int(input("Player 1 move: ")) # Yang diinput kolom berapa
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            print(row)
            dropPiece(board, row, col, 1)

            if winningMove(board, 1):
                print("Player 1 menang.")
                gameOver = True
    # Prompt player 2 for input
    else:
        col = int(input("Player 2 move: ")) # Yang diinput kolom berapa
        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            print(row)
            dropPiece(board, row, col, 2)

            if winningMove(board, 2):
                print("Player 2 menang.")
                gameOver = True
    printBoard(board)
    turn += 1
    turn %= 2