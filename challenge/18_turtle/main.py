import turtle as t
import random


def random_color(colormode):
    new_color = (random.randint(0, colormode), random.randint(0, colormode), random.randint(0, colormode))
    return new_color


timmy = t.Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
colormode=255

t.colormode(colormode)
screen = t.Screen()

timmy.pensize(2)

size=80
for _ in range(10):
    for _ in range(72):
        timmy.pencolor(random_color(colormode))
        timmy.circle(size)
        timmy.right(5)
    size+=30

screen.exitonclick()
