from turtle import Screen, Turtle
from snake import Snake
import time

SPEED = 20

def move_snake(snakes, speed):
    for i in range(len(snakes)-1,0,-1):
        snakes[i].goto(snakes[i-1].pos())
    snakes[0].forward(speed)

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("#000000")
screen.title("SNAKE GAME")
screen.tracer(0)

screen.update()

snake = Snake(15)

screen.listen()
screen.onkey(key="Up",fun=snake.turn_up)
screen.onkey(key="Down",fun=snake.turn_down)
screen.onkey(key="Left",fun=snake.turn_left)
screen.onkey(key="Right",fun=snake.turn_right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move(speed=SPEED)
    game_is_on = snake.check_death()

screen.exitonclick()