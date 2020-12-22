import pygame as pg
from pygame.locals import *
import sys
import time

# We are initilazing pygame
pg.init()

# We are creating the gloobal variabls
winner = None
drawn = None
xo = "x"
CLOCK = pg.time.Clock()

# The width and high of our window
width = 400
high = 400

# How many frames gonna be per sec
# How many columns and rows we gonna have
fps = 35
play_board = [[None]*3, [None]*3, [None]*3]

# Creating the window and seating a caption
screen = pg.display.set_mode(size=(width, high + 100), depth=32)
pg.display.set_caption("Tic Tac Toe game")


# Downloding the png files
o_image = pg.image.load(
    "C:\\Users\\abdullrauf.alhariri\\Desktop\\HelloWorld\\First_pygame_game\\o_image.png")
x_image = pg.image.load(
    "C:\\Users\\abdullrauf.alhariri\\Desktop\HelloWorld\\First_pygame_game\\x_image.png")
game_cover = pg.image.load(
    "C:\\Users\\abdullrauf.alhariri\\Desktop\HelloWorld\\First_pygame_game\\xo_image.png")

# Initialize the size of the png files
x_image = pg.transform.scale(x_image, (80, 80))
o_image = pg.transform.scale(o_image, (80, 80))
game_cover = pg.transform.scale(game_cover, (width, high + 100))

# The colors of the window and lines
white = (255, 255, 255)

line_color = (0, 0, 0)


def design_window():
    global screen

    # We're displaying the game and
    # Then we are filling back the
    # Window with white
    screen.blit(game_cover, (0, 0))
    pg.display.update()
    time.sleep(3)

    screen.fill(white)

    # Here we are creaating the vertical lines
    first_line = pg.draw.line(
        screen, line_color, (width / 3, 0), (width/3, high), 5)
    second_line = pg.draw.line(
        screen, line_color, (width/3 * 2, 0), (width/3 * 2, high), 5)

    # Here we are creating the horizontal lines
    line_one = pg.draw.line(
        screen, line_color, (0, high / 3), (width, high/3), 5)
    line_two = pg.draw.line(
        screen, line_color, (0, high/3 * 2), (width, high/3 * 2), 5)

    game_status()


def game_status():
    global drawn

    # We are locking if someone has won yet or not
    if winner == None:
        message = xo.upper() + "'s Turn"
    else:
        message = winner.upper() + " Won!"

    if drawn:
        message = "Game is Over!"

    # We are creating a font object
    font = pg.font.Font(None, 30)

    # We are entering the text, size and color
    text = font.render(message, 1, white)

    # We are creating a new surface for
    # Displaying the text

    # The first argument is the color
    # The second argument is the given area
    # First number is left(the start line from x cor)
    # Second number is where on the y cor we gonna start drawing
    # The third is the width and the fourth is the highst
    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_place = text.get_rect(center=(width/2, 500 - 50))
    screen.blit(text, text_place)

    pg.display.update()


def checkwin():
    global drawn, winner, play_board

    # We are checking for the wining rows
    for row in range(0, 3):
        if (play_board[row][0] == play_board[row][1] == play_board[row][2]) and (play_board[row][0] != None):
            winner = play_board[row][0]
            draw_line = pg.draw.line(
                screen, (255, 0, 0), (0, (row + 1) * high/3 - high/6), (width, (row+1)*high/3 - high/6), 4)
            break

    # We are checking for the wining columns
    for col in range(0, 3):
        if(play_board[0][col] == play_board[1][col] == play_board[2][col]) and (play_board[0][col] != None):
            winner = play_board[0][col]
            draw_line = pg.draw.line(screen, (255, 0, 0), ((
                col + 1)*width/3 - width/6, 0), ((col + 1) * width/3 - width/6, high), 4)
            break

    # We are checking for the winners from left to the right
    if (play_board[0][0] == play_board[1][1] == play_board[2][2]) and (play_board[0][0] != None):
        winner = play_board[0][0]
        draw_line = pg.draw.line(
            screen, (255, 0, 0), (50, high - 350), (350, 350), 4)

    # We are checking if the winner is from the right to the left
    if (play_board[0][2] == play_board[1][1] == play_board[2][0]) and (play_board[0][2] != None):
        winner = play_board[0][2]
        drawn_line = pg.draw.line(screen, (255, 0, 0), (350, 50), (50, 350), 4)

    if all([all(row) for row in play_board]) and (winner == None):
        drawn = True

    game_status()


def draw_xo(row, col):
    global play_board, xo

    # Here we are chekcing for the position of x and o
    if row == 1:
        posy = 30

    if row == 2:
        posy = high / 3 + 30

    if row == 3:
        posy = high/3 * 2 + 30

    if col == 1:
        posx = 30

    if col == 2:
        posx = width / 3 + 30

    if col == 3:
        posx = width/3 * 2 + 30

    # We are setting the value for xo
    play_board[row-1][col-1] = xo

    if (xo == "x"):
        screen.blit(x_image, (posx, posy))
        xo = "o"

    else:
        screen.blit(o_image, (posx, posy))
        xo = "x"
    pg.display.update()


def user_click():

    x, y = pg.mouse.get_pos()

    if(x < width/3):
        col = 1

    elif(x < width/3*2):
        col = 2

    elif(x < width):
        col = 3

    else:
        col = None

    if(y < high/3):
        row = 1

    elif(y < high/3*2):
        row = 2

    elif(y < high):
        row = 3

    else:
        row = None

    if(row and col and play_board[row-1][col-1] == None):
        draw_xo(row, col)
        checkwin()


def reset_game():
    global xo, play_board, winner, draw_xo, drawn
    time.sleep(3)
    winner = None
    drawn = False
    xo = "x"
    screen.fill(white)
    design_window()
    play_board = [[None]*3, [None]*3, [None]*3]


design_window()

while True:
    for even in pg.event.get():
        if even.type == QUIT:
            pg.quit()
            sys.exit()
        elif even.type == MOUSEBUTTONDOWN:
            user_click()

        if(winner or drawn):
            reset_game()

    pg.display.update()
    CLOCK.tick(fps)
