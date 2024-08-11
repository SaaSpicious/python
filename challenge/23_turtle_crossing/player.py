from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("#009944")
        self.shapesize(stretch_wid=1.3,stretch_len=1.3)
        self.reset()


    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.setheading(90)
        self.goto(0, -200)

    def checkhit(self,cars):
        for car in cars:
            if self.distance(car) < 18:
                return True
        return False

