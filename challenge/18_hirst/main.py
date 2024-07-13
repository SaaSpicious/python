import colorgram
import turtle as t
import random


def get_colors(filename):
    colors = colorgram.extract(filename,60)
    return colors


def get_random_color(colors):
    checksum = 711
    while checksum > 710:
        color = random.choice(colors)
        rgb = color.rgb
        rgb_color = (rgb.r,rgb.g,rgb.b)
        checksum = sum(rgb_color)
    return rgb_color


def reset_turtle(timmy,distance,width):
    timmy.setheading(270)
    timmy.forward(distance)
    timmy.setheading(180)
    timmy.forward(width * distance)


def draw_dot(timmy,colors,distance,size):
    timmy.setheading(0)
    timmy.dot(size,get_random_color(colors))
    timmy.forward(distance)

def draw_painting(timmy,height,width,distance,colors,size):
    for _ in range(height):
        for _ in range(width):
            draw_dot(timmy, colors, distance, size)
        reset_turtle(timmy, distance, width)


def initialize_turtle():
    timmy = t.Turtle()
    timmy.speed("fastest")
    timmy.penup()
    timmy.hideturtle()
    return timmy


screen = t.Screen()
screen.colormode(255)

distance = 50
width = 12
height = 12
size = 20

draw_painting(initialize_turtle(),height,width,distance,get_colors('hirst.jpg'),size)

screen.exitonclick()