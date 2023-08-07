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
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    scoreboard.show_level()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect if the player reached the finish line
    # if player.ycor() > 270:
    #     player.reset_position()
    #     car_manager.increase_car_speed()
    #     scoreboard.update_level()
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_car_speed()
        scoreboard.update_level()

screen_overlay.game_over()

screen.exitonclick()
