from turtle import Turtle
import random

STEP = 40
class Paddle(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.shape("square")
        self.color("#FFFFFF")
        self.shapesize(stretch_wid=9,stretch_len=2)
        self.penup()
        self.goto(xcor,0)

    def go_up(self):
        if self.ycor() < 400:
            self.goto(self.xcor(),self.ycor() + STEP)

    def go_down(self):
        if self.ycor() > -400:
            self.goto(self.xcor(),self.ycor() - STEP)

    def automove(self,ball):
        dice = random.randint(1,20)
        if abs(self.ycor() - ball.ycor()) > 40:
            if ball.ycor() > self.ycor():
                if dice > 18: #Fehlschlag!
                    self.go_down()
                elif dice < 10:
                    self.go_up()
            else:
                if dice > 18:  # Fehlschlag!
                    self.go_up()
                elif dice < 10:
                    self.go_down()

