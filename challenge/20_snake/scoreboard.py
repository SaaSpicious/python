from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.font = "Arial"
        self.font_size = 12
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,240)

    def refresh(self, score):
         self.clear()
         self.write("Score: "+str(score), move=False, align='center', font=(self.font, self.font_size, 'normal'))

    def failmessage(self):
        self.goto(0,0)
        self.color("red")
        self.font_size = 20
        self.write("GAME OVER", move=False, align='center', font=(self.font, self.font_size, 'normal'))
