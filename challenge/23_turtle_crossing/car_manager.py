import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars=[]
        for i in range(1,6):
            self.cars.append(self.add_car(0))

    def add_car(self,level):
        random_position = -170 + (random.randint(0,40)* MOVE_INCREMENT)
        return Car((300,random_position),STARTING_MOVE_DISTANCE + level)

    def move_cars(self):
        for car in self.cars:
            car.move()

    def might_add(self,level):
        if random.randint(1,20) >=(19-level//3):
            self.cars.append(self.add_car(level))


class Car(Turtle):
    def __init__(self,coordinates,move_speed):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.move_speed = move_speed
        self.goto(coordinates)

    def move(self):
        self.forward(self.move_speed)

