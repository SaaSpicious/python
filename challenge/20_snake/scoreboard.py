from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.font = "Arial"
        self.font_size = 12
        self.highscore = self.read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,240)

    def refresh(self, score):
         self.clear()
         self.write(f"Score: {str(score)} High Score: {str(self.read_highscore())}", move=False, align='center', font=(self.font, self.font_size, 'normal'))

    def failmessage(self,score):
        self.goto(0,0)
        self.color("red")
        self.font_size = 20
        self.write("GAME OVER", move=False, align='center', font=(self.font, self.font_size, 'normal'))
        if self.highscore < score:
            self.new_highscore(score)

    def new_highscore(self,score):
        self.goto(0, -40)
        self.color("#00CC88")
        self.write("NEW HIGHSCORE!", move=False, align='center', font=(self.font, self.font_size, 'normal'))
        self.write_highscore(score)

    def read_highscore(self):
        with open("highscore") as file:
            highscore = file.read()

        if highscore.isnumeric():
            return int(highscore)
        else:
            return 0

    def write_highscore(self,highscore):
        with open("highscore", "a") as file:
            file.truncate(0)
            file.write(str(highscore))