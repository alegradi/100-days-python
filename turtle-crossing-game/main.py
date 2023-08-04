import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from screen_overlay import ScreenOverlay

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

screen_overlay = ScreenOverlay()
player = Player()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.move_car()



screen.exitonclick()