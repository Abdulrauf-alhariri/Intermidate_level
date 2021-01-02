import pygame as pg
from pygame.locals import *
import sys
import random
import time

# We are going to create the global variabls
# that we might gonna need to use
pg.init()

lost = False
foodx = False
score = 0

width = 500
hight = 500

x_speed = 0
y_speed = 0

x_position = 55
y_position = 55

Clock = pg.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (220, 20, 60)

# Global variabls for the snake
snake_blcok = 15
snake_list = []
snake_lenght = 1

# Global variabls for the food
apple_Xposition = random.randint(0, width/2)
apple_Yposition = random.randint(50, hight/2)
snake_position = []

screen = pg.display.set_mode(size=(width, hight), depth=32)

apple_image = pg.image.load(
    "C:\\Users\\abdullrauf.alhariri\\Desktop\\HelloWorld\\snake_package\\pngwing.com.png")

apple_image = pg.transform.scale(apple_image, (15, 15))


def draw_window():

    # Here we are creating the vertical lines which gonna be 20 lines
    for i in range(20):
        draw_line1 = pg.draw.line(
            screen, white, (widht/20*i, 50), (width/20*i, hight))

    # Here we are creating the horizontal lines which also gonna be 20
    for i in range(20):
        draw_line = pg.draw.line(
            screen, white, (0, hight/20*i), (width, hight/20*i))

    # Here we are creating the snake and calling the status method
    pg.draw.rect(screen, (0, 255, 0), (x_position, y_position, 20, 20))

    game_status()
    checkScore()


def draw_snakeHead(snake_blcok, snake_list):
    for x, y in snake_list:
        pg.draw.rect(screen, (0, 255, 0), (x, y, snake_blcok, snake_blcok))


def draw_food():
    screen.blit(apple_image, (apple_Xposition, apple_Yposition))


def game_status():

    # Here we are locking if the player has lost or no
    if lost:
        message = "You've lost"
    else:
        message = "Score: " + str(score)

    # We are creating a font object and defining the message
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, white)

    # We are creating a new block and displaying the message
    screen.fill(black, (0, 0, width+100, 50))
    text_place = text.get_rect(topleft=(0, 50/2))

    screen.blit(text, text_place)


def checkScore():
    global score, lost, apple_Yposition, apple_Xposition, snake_lenght, snake_position

    # We are checking if the snake and the apple are very close to each others
    # So we increase the score
    if abs(apple_Xposition - x_position) < 10 and abs(apple_Yposition - y_position) < 10:
        score += 1
        apple_Xposition = random.randint(0, width/2)
        apple_Yposition = random.randint(50, hight/2)
        snake_lenght += 5

    # For each hundrede changes in the position we are going to move
    # The apple
    if len(snake_position) == 100:
        snake_position = []
        apple_Xposition = random.randint(0, width/2)
        apple_Yposition = random.randint(50, hight/2)

    # If the player hit the ground, walls or the roof so he lost
    if x_position == width or x_position == 0 or y_position == hight or y_position == 50:
        lost = True

    game_status()


def reset_game():
    global lost, snake_lenght, snake_list, score, x_position, y_position, x_speed, y_speed
    time.sleep(1)
    lost = False
    snake_lenght = 1
    snake_list = []
    score = 0
    x_position = 55
    y_position = 55

    x_speed = 0
    y_speed = 0

    draw_window()


while True:

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x_speed += 5
                y_speed = 0

            if event.key == K_LEFT:
                x_speed -= 5
                y_speed = 0

            if event.key == K_UP:
                y_speed -= 5
                x_speed = 0

            if event.key == K_DOWN:
                y_speed += 5
                x_speed = 0

    # Move the snake
    x_position += x_speed
    y_position += y_speed

    # Here we are creating the snake head
    snake_head = []
    snake_head.append(x_position)
    snake_head.append(y_position)

    # We are adding the current position to the snake list
    snake_list.append(snake_head)
    snake_position.append(snake_head)

    # If the length is bigger than the snake_lenght
    # So that means that we have a new position
    if len(snake_list) > snake_lenght:
        del snake_list[0]

    screen.fill(black)
    draw_window()
    draw_snakeHead(snake_blcok, snake_list)
    draw_food()

    if lost:
        reset_game()

    pg.display.update()
    Clock.tick(32)
    print(snake_list)
