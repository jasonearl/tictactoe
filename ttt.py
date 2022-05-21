import pygame
pygame.init()

WIDTH = 900
HEIGHT = 800

# colors
black = (0,0,0)
white = (255,255,255)
grey = (128,128,128)
dark_grey = (50,50,50)
green = (0,255,0)
gold = (212,175,55)
blue = (0,255,255)


screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Tik Tac Toe')
label_font = pygame.font.Font('freesansbold.ttf', 60)


fps = 60
timer = pygame.time.Clock()
# track which boxes have been cliked, -1 means NOT clicked, +1 means clicked
clicked = [[-1 for _ in range(3)] for _ in range(3)]
box_taken = [[False for _ in range(3)] for _ in range(3)]
board = [[None for _ in range(3)] for _ in range(3)]



def draw_grid(clicks):
    boxes = [] # store rectangle object and its coordinates
    # draw game board
    for i in range(3):
        for j in range(3):
            rect = pygame.draw.rect(screen,grey,[i * 300,j * 200,300,HEIGHT-600],5)
            boxes.append((rect, (i,j))) # store rectangle object and its coordinates
            # text box = X (1) or O (0) or Blank (-1)
            if (clicks[j][i] == -1):
                text = label_font.render('', True, blue)
            elif (clicks[j][i] == 1):
                text = label_font.render('X', True, blue)
            else:
                text = label_font.render('O', True, blue)
            screen.blit(text, ((i*300) +125,(j*200) +75))

    return boxes

def check_rows():
    for i in range(len(board)):
        if (board[i][0] != None):
            if (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
                winner = f"{board[i][0]} WINS!"
                return (True,winner)
    return (False,"")

def check_cols():
    for i in range(len(board)):
        if (board[0][i] != None):
            if (board[0][i] == board[1][i] and board[1][i] == board[2][i]):
                winner = f"{board[0][i]} WINS!"
                return (True,winner)
    return (False,"")

def check_diagonals():
    # top left to bottom right
    if (board[0][0] != None):
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            winner = f"{board[0][0]} WINS!"
            return (True,winner)

    # bottom left to top right
    if (board[2][0] != None):
        if (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
            winner = f"{board[2][0]} WINS!"
            return (True,winner)
    return (False,"")

def draw():
    # check if all blocks are filled and there is NO winner, game is a draw
    num_empty_slots = 9
    for i in range(3):
        for j in range(3):
            if clicked[i][j] != -1: # still empty box
                num_empty_slots -= 1
    if num_empty_slots == 0:
        winner = "The Game is a Draw"
        return (True, winner)
    return (False,"")

def game_over():
    # check if player has won
    row_result = check_rows()
    if row_result[0]:
        return row_result

    col_result = check_cols()
    if row_result[0]:
        return row_result

    diag_result = check_diagonals()
    if diag_result[0]:
        return diag_result

    draw_result = draw()
    if draw_result[0]:
        return draw_result

    return (False,"")


def start():
    # track player turn, X's move first
    x = True
    run = True
    while run:
        timer.tick(fps)
        screen.fill(black)
        boxes = draw_grid(clicked)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # CHECK IF GAME OVER
            result = game_over()
            if (result[0]):
                # game is over, stop updating board
                # TODO figure out how to end game 
                if event.type == pygame.QUIT:
                    run = False


            else:
                # EVENT HANDLER BOXES
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in range(len(boxes)):
                        # get coordinates of box clicked
                        coords = boxes[i][1]
                        # check if box was clicked, check player turn X or O, check the box isn't already taken
                        if boxes[i][0].collidepoint(event.pos) and x and not box_taken[coords[1]][coords[0]]:
                            # update the value of the box to reflect the click
                            clicked[coords[1]][coords[0]] = 1
                            # indicate the box has been taken
                            box_taken[coords[1]][coords[0]] = True
                            board[coords[1]][coords[0]] = 'X'
                            x = False   # X made move, change player to O
                        elif boxes[i][0].collidepoint(event.pos) and not x and not box_taken[coords[1]][coords[0]]:
                            clicked[coords[1]][coords[0]] = 0
                            box_taken[coords[1]][coords[0]] = True
                            board[coords[1]][coords[0]] = 'O'
                            x = True

        pygame.display.flip()


def main():
    start()
    pygame.quit()


if __name__ == '__main__':
    main()
