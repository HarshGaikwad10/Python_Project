from turtle import Turtle,Screen

scr=Screen()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def  __init__(self):
        super().__init__()
        self.color("pink")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move_f(self):

        self.fd(MOVE_DISTANCE)
    def line(self):
        new_t=Turtle()
        new_t.penup()
        new_t.color("red")
        new_t.goto(-300,-250)
        new_t.pendown()
        new_t.fd(600)
        new_t.penup()
        new_t.goto(300,250)
        new_t.setheading(180)
        new_t.pendown()
        new_t.fd(630)


