from turtle import Turtle
import random


class Snake:

    def __init__(self,length):
        self.snake = []
        for i in range(length):
            segment = self.create_segment((0 - (i * 20), 0))
            self.snake.append(segment)
        self.head = self.snake[0]

    def random_color(self):
        r = lambda: random.randint(0,255)
        return ('#%02X%02X%02X' % (r(),r(),r()))

    def create_segment(self, coordinates):
        segment = Turtle(shape="square")
        segment.color(self.random_color())
        segment.penup()
        segment.goto(coordinates)
        return segment
    
    def extend(self):
        segment = self.create_segment(self.snake[-1].pos())
        self.snake.append(segment)
    
    def detect_wall_collision(self):
        if abs(self.head.xcor()) > 300:
            return False
        if abs(self.head.ycor()) > 300:
            return False
        return True


    def move(self, speed):
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].goto(self.snake[i-1].pos())
        self.head.forward(speed)


    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)



    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)


    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    def detect_snake_collision(self):
        for segment in self.snake[1:]:
            if (self.head.distance(segment) < 3):
                return False
        return True
