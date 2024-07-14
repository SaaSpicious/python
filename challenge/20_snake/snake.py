from turtle import Turtle


class Snake:

    def __init__(self,length):
        self.snake = []
        for i in range(length):
            segment = self.create_segment()
            segment.goto(0 - (i * 20), 0)
            self.snake.append(segment)
        self.head = self.snake[0]

    def create_segment(self):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        return segment


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


    def check_death(self):
        for seg_number in range(1,len(self.snake)-1):
            if self.snake[seg_number].pos() == self.head.pos():
                return False
        return True
