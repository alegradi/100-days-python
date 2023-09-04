import random
import turtle
from turtle import Turtle, Screen
from random import Random

tim = Turtle()
tim.shape("turtle")
# tim.color("")
tim.pendown()
turtle.colormode(255)


def draw_shape(number_of_sides, side_length):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(side_length)
        tim.right(angle)


def change_turtle_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.color(r, g, b)


for _ in range(4, 11):
    change_turtle_color()
    draw_shape(_, 100)



















screen = Screen()
screen.exitonclick()

