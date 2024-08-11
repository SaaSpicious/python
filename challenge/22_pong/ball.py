from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("circle")
        self.color("#FFFFFF")
        self.penup()
        self.shapesize(stretch_wid=2,stretch_len=2)
        self.goto(position)
        self.x_move = 11
        self.y_move = 11
        self.move_speed = 0.05

    def move(self,player,opponent):
        if self.ycor() < -450:
            self.y_move = random.randint(8,12)
        elif self.ycor() > 450:
            self.y_move = random.randint(8,12) * -1

        if (self.distance(player)) < 55:
            self.x_move = random.randint(8,12)
            self.move_speed -= 0.002
        elif self.distance(opponent) < 55:
            self.x_move = random.randint(8,12) * -1
            self.move_speed -= 0.002
        self.goto(self.xcor() + self.x_move,self.ycor() + self.y_move)

    def reset(self,x_move):
        self.x_move = x_move
        self.y_move = random.randint(8,11)
        self.goto(0,0)
        self.move_speed = 0.05
