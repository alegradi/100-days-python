import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.seth(180)
        self.color(random.choice(COLORS))
        self.goto(200, 0)  # Just a starting position for now


    def move_car(self):
        self.forward(MOVE_INCREMENT)

