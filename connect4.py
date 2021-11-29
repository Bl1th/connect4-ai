import numpy as np
import pygame
import sys
import math

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COL_COUNT = 7
SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE / 2 - 5)

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
        for row in range(3, ROW_COUNT):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True

def drawBoard(board):
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (col*SQUARE_SIZE, row*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            pygame.draw.circle(screen, BLACK, (int(col*SQUARE_SIZE+SQUARE_SIZE/2), int(row*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
    
    for col in range(COL_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (int(col*SQUARE_SIZE+SQUARE_SIZE/2), height-int(row*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (int(col*SQUARE_SIZE+SQUARE_SIZE/2), height-int(row*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
        pygame.display.update()    

board = createBoard() # Buat papan connect 4
printBoard(board) # Initial Game State
gameOver = False
turn = 0

pygame.init()
width = COL_COUNT * SQUARE_SIZE
height = (ROW_COUNT+1) * SQUARE_SIZE
size = (width, height)

screen = pygame.display.set_mode(size)
drawBoard(board)
pygame.display.update()

myfont = pygame.font.SysFont("Consolas", 60)

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Prompt player 1 for input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARE_SIZE))
                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    print(row)
                    dropPiece(board, row, col, 1)
                    if winningMove(board, 1):
                        label = myfont.render("Player 1 menang.", 1, RED)
                        screen.blit(label, (80,10))
                        gameOver = True
            # Prompt player 2 for input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARE_SIZE))
                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    print(row)
                    dropPiece(board, row, col, 2)
                    if winningMove(board, 2):
                        label = myfont.render("Player 2 menang.", 1, YELLOW)
                        screen.blit(label, (80,10))
                        gameOver = True
            printBoard(board)
            drawBoard(board)
            turn += 1
            turn %= 2

            if gameOver:
                pygame.time.wait(3000)