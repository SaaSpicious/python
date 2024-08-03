from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SPEED = 20
INITIAL_LENGTH = 5

def move_snake(snakes, speed):
    for i in range(len(snakes)-1,0,-1):
        snakes[i].goto(snakes[i-1].pos())
    snakes[0].forward(speed)

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("#000000")
screen.title("SNAKE GAME")
screen.tracer(0)

food = Food()

screen.update()

snake = Snake(INITIAL_LENGTH)

screen.listen()
screen.onkey(key="Up",fun=snake.turn_up)
screen.onkey(key="Down",fun=snake.turn_down)
screen.onkey(key="Left",fun=snake.turn_left)
screen.onkey(key="Right",fun=snake.turn_right)

score = 0

scoreboard = Scoreboard()
scoreboard.refresh(score)

while snake.detect_wall_collision() & snake.detect_snake_collision():
    screen.update()
    time.sleep(0.08)
    snake.move(speed=SPEED)

    # Collision detection
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score += 1
        scoreboard.refresh(score)

scoreboard.failmessage()
screen.exitonclick()