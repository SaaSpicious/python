from ball import Ball
from paddle import Paddle
from board import Board
import time
from turtle import Screen

screen = Screen()

player = Paddle(-560)
opponent = Paddle(560)
ball = Ball((0,0))

screen.screensize(800,600)
screen.bgcolor("#000000")
screen.title("Poor man's Pong")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up",fun=player.go_up)
screen.onkey(key="Down",fun=player.go_down)
screen.onkey(key="w",fun=opponent.go_up)
screen.onkey(key="s",fun=opponent.go_down)

player_points = 0
opponent_points = 0

board = Board()

while player_points + opponent_points < 11:
    time.sleep(ball.move_speed)
    ball.move(player,opponent)
    opponent.automove(ball)
    screen.update()
    if ball.xcor() > 600:
        player_points += 1
        ball.reset(-10)
    elif ball.xcor() < -600:
        opponent_points += 1
        ball.reset(10)
    board.refresh((player_points,opponent_points))


screen.exitonclick()
