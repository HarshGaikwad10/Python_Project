import time
import pygame
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
pygame.mixer.init()
screen = Screen()
want_restart=True
while want_restart:
    music= pygame.mixer.music.load("startingrintone.mp3")
    pygame.mixer.music.play(-1)

    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)
    play_1=Player()
    s_b=Scoreboard()
    play_1.line()
    screen.onkey(play_1.move_f,"Up")
    cm=CarManager()
    screen.listen()




    game_is_on = True  
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        cm.make_car()
        cm.move_car()
    
        for car in cm.all_cars:
            if car.distance(play_1)<20:
                s_b.gameover()
                g_o=pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play(-1)
                game_is_on = False
        if play_1.ycor()>255 :
            s_b.level+=1
            play_1.goto(0,-280)
            s_b.updateScore()
            cm.move_time*=0.6
    again=screen.textinput(title="Would want to continue?(yes or no)",prompt="Enter your answer : ").lower()
    if again=="yes":
        screen.clear()
        play_1.clear()
        s_b.clear()
        cm.clear()
        continue
    elif again=="no":
       pygame.mixer.quit()
       want_restart=False

    else:
        Turtle.write("Try again",align="center",font=("arial",24,"normal"))



screen.exitonclick()


