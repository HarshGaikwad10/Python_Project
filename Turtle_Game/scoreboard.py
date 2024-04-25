from turtle import Turtle,Screen
FONT = ("Courier", 21, "normal")
scr=Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.level=1
        self.updateScore()

    def gameover(self):
        self.penup()
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("times new roman", 70, "normal"))

    def updateScore(self):
        self.clear()
        self.penup()
        self.goto(-210, 250)
        self.write(f"LEVEL :{self.level}", align="center", font=FONT)




