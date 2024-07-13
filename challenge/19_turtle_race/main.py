from turtle import Turtle, Screen
import random


def create_turtle(color):
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    return turtle


def move_to_start(turtle,position):
    y = -160 + i * 65
    turtle.goto(-240,y)


def random_move(turtle):
    random_steps = random.randint(0,4)*2
    turtle.forward(random_steps)


def check_goal(turtle):
    if turtle.xcor() > 230:
        return True
    return False


screen = Screen()
screen.setup(500,400)

colors = ['red','orange','yellow','green','blue','purple']

turtles = []

for i in range(len(colors)):
    turtles.append(create_turtle(colors[i]))
    move_to_start(turtles[i],i)

winner_bet = screen.textinput(title="Make a bet",prompt="Which turtle is going to win the race?")

race_over = False
while race_over == False:
    for turtle in turtles:
        random_move(turtle)
        if check_goal(turtle):
            winning_color=turtle.color()
            race_over = True

if winning_color[0] == winner_bet:
    print("Congratulations, you've bet on the right turtle")
else:
    print(f"You lost, the {winning_color[0]} turtle won the race.")