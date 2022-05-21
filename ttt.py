import pygame, sys
import numpy as np
pygame.init()

WIDTH = 600
HEIGHT = 600
BOX_SIZE = 200
RADIUS = 60
OFF_SET = 50

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
SILVER = (192,192,192)
GOLD = (218,165,32)

P1_COLOR = GOLD
P2_COLOR = SILVER

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BLACK)

# 2D array game board
board = np.zeros((3,3))

def create_grid():
    # horizontal lines
    pygame.draw.line(screen, WHITE, (0,200), (600,200), 10)
    pygame.draw.line(screen, WHITE, (0,400), (600,400), 10)

    # vertical lines
    pygame.draw.line(screen, WHITE, (200,0), (200,600), 10)
    pygame.draw.line(screen, WHITE, (400,0), (400,600), 10)


def fill_box(row, col, player):
    board[row][col] = player

def box_empty(row,col):
    return board[row][col] == 0

def board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def show_x_o():
    for row in range(3):
        for col in range(3):
            # put an O on the board
            if board[row][col] == -1:
                pygame.draw.circle(screen, P2_COLOR, (int(col * 200 + 100),int(row * 200 + 100)), RADIUS, 10)
            # put an X on the board
            elif board[row][col] == 1:
                pygame.draw.line(screen, P1_COLOR, (col * BOX_SIZE + OFF_SET, row * BOX_SIZE + BOX_SIZE - OFF_SET), (col * BOX_SIZE + BOX_SIZE - OFF_SET, row * BOX_SIZE + OFF_SET), 10)
                pygame.draw.line(screen, P1_COLOR, (col * BOX_SIZE + OFF_SET, row * BOX_SIZE + OFF_SET), (col * BOX_SIZE + BOX_SIZE - OFF_SET, row * BOX_SIZE + BOX_SIZE - OFF_SET), 10)


def game_result(player):
    # check for win in columns
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            show_col_win(col,player)
            return True

    # check for win in rows
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            show_row_win(row,player)
            return True

    # check for win in diagonal from SW to NE
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        diag_win_SW_NE(player)
        return True

    # check for win in diagonal from NW to SE
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        diag_win_NW_SE(player)
        return True

# check columns for win
def show_col_win(col, player):
    x_coord = col * 200 + 100
    if player == 1:
        color = P1_COLOR
    else:
        color = P2_COLOR
    pygame.draw.line(screen, color, (x_coord, 0), (x_coord, HEIGHT), 20)

# check rows for win
def show_row_win(row, player):
    y_coord = row * 200 + 100
    if player == 1:
        color = P1_COLOR
    else:
        color = P2_COLOR
    pygame.draw.line(screen, color, (0, y_coord), (WIDTH, y_coord), 20)

# check diagonal from South-West corner to North-East corner
def diag_win_SW_NE(player):
    if player == 1:
        color = P1_COLOR
    else:
        color = P2_COLOR
    pygame.draw.line(screen, color, (0, HEIGHT), (WIDTH, 0), 20)

# check diagonal from North-West corner to South-East corner
def diag_win_NW_SE(player):
    if player == 1:
        color = P1_COLOR
    else:
        color = P2_COLOR
    pygame.draw.line(screen, color, (0, 0), (WIDTH, HEIGHT), 20)

def new_game():
    screen.fill(BLACK)
    create_grid()
    for row in range(3):
        for col in range(3):
            board[row][col] = 0



create_grid()
player = 1  # 1 = X, -1 = O, X's start first
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_coord = event.pos[0]
            y_coord = event.pos[1]

            cur_row = int(y_coord // BOX_SIZE) # 200 is the HEIGHT and WIDTH of each box
            cur_col = int(x_coord // BOX_SIZE)

            if box_empty(cur_row, cur_col):
                if player == 1:
                    fill_box(cur_row, cur_col, 1)
                elif player == -1:
                    fill_box(cur_row, cur_col, -1)

                if game_result(player):
                    game_over = True
                show_x_o()
                player *= -1 # switch player

        # if the user hits the 'n' key on keyboard, a new game will start
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                new_game()
                game_over = False
                player = 1

    pygame.display.update()
