# save in git

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

def game_over():
    # TODO CREATE GIT REPOSITORY check if player has won

    # DRAW all boxes filled, no winner
    num_empty_slots = 9
    for i in range(3):
        for j in range(3):
            if clicked[i][j] != -1: # still empty box
                num_empty_slots -= 1
    if num_empty_slots == 0:
        return True
    return False

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
        if game_over():
            # game is over, stop updating board
            if event.type == pygame.QUIT:
                run = False


        else:
            # EVENT HANDLER BOXES
            if event.type == pygame.MOUSEBUTTONUP:
                for i in range(len(boxes)):
                    # check if box was clicked
                    if boxes[i][0].collidepoint(event.pos) and x:
                        # get the coordinates of the box that was clicked
                        coords = boxes[i][1]
                        # update the value of the box to reflect the click
                        clicked[coords[1]][coords[0]] = 1
                        x = False   # X made move, change player to O
                    elif boxes[i][0].collidepoint(event.pos) and not x:
                        coords = boxes[i][1]
                        clicked[coords[1]][coords[0]] = 0
                        x = True    # O made move, change player to X

    pygame.display.flip()


pygame.quit()
