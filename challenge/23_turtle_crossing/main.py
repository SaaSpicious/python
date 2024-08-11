import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def check_win(player,level):
    if player.ycor() > 200:
        player.reset()
        return level + 1
    return level


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
board = Scoreboard()

car_manager = CarManager()

screen.onkey(key="Up",fun=player.move_up)
screen.onkey(key="Left",fun=player.move_left)
screen.onkey(key="Right",fun=player.move_right)
screen.onkey(key="Down",fun=player.move_down)

level = 0

game_is_on = True
while not player.checkhit(car_manager.cars):
    time.sleep(0.1)
    screen.update()
    level = check_win(player,level)
    car_manager.move_cars()
    car_manager.might_add(level)
    board.refresh(level)

board.game_over()
screen.exitonclick()


