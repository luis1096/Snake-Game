# Author -> Luis Oliveros
# Version -> 6/15/2022

import pygame as p
import time as t
import random as r

p.init()
display = p.display.set_mode((800,600))
p.display.update()
p.display.set_caption("Snake Game By Luis O :p")
font_style = p.font.SysFont("bahnschrift", 30)
score_font = p.font.SysFont("comicsansms", 30)
game_over = False

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
clock = p.time.Clock()

def user_score(score):
    value = score_font.render("Score: " + str(score), True, green)
    display.blit(value, [0, 0])

def snake_obj(snake_block, snake_list):
    for x in snake_list:
        p.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [64, 280])
    
def gameLoop(): 
    game_over = False
    game_close = False
    x = 400
    y = 300
    x_change = 0
    y_change = 0
    food_x = round(r.randrange(0, 600 - 10) / 10.0) * 10.0
    food_y = round(r.randrange(0, 600 - 10) / 10.0) * 10.0
    snake_list = []
    snake_length = 1

    while not game_over:

        while game_close == True:
            display.fill(black)
            message("Game Over ): Press [Q] to Quit or [C] to Play Again", red)
            user_score(snake_length - 1)
            p.display.update()
            for event in p.event.get():
                if event.type == p.KEYDOWN:
                    if event.key == p.K_q:
                        game_over = True
                        game_close = False
                    if event.key == p.K_c:
                        gameLoop()

        for event in p.event.get():
            if event.type == p.QUIT:
                game_over = True
            if event.type == p.KEYDOWN:
                if event.key == p.K_LEFT:
                    x_change = -10
                    y_change = 0
                elif event.key == p.K_RIGHT:
                    x_change = 10
                    y_change = 0
                elif event.key == p.K_UP:
                    y_change = -10
                    x_change = 0
                elif event.key == p.K_DOWN:
                    y_change = 10
                    x_change = 0 
        if x >= 800 or x < 0 or y >= 600 or y < 0:
            game_close = True

        x += x_change
        y += y_change
        display.fill(black)
        #print(event)
        p.draw.rect(display, red, [food_x, food_y, 10,10])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        for z in snake_list:
            if z == snake_head[:-1]:
                game_close = True
        
        snake_obj(10, snake_list)
        user_score(snake_length - 1)
        p.display.update()
        clock.tick(30)

        if x == food_x and y == food_y:
            food_x = round(r.randrange(0, 600 - 10) / 10.0) * 10.0
            food_y = round(r.randrange(0, 600 - 10) / 10.0) * 10.0
            snake_length += 1
    
    p.quit()
    quit()

gameLoop()





