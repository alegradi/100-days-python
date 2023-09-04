import turtle
from turtle import Turtle, Screen
import random

spiro = Turtle()
turtle.colormode(255)
spiro.speed(15)

def change_pen_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    spiro.pencolor(r, g, b)


# for _ in range(180):
#     change_pen_color()
#     spiro.circle(100)
#     spiro.setheading(_)

angle = 0

while angle < 360:
    angle += 5
    change_pen_color()
    spiro.circle(100)
    spiro.setheading(angle)












screen = Screen()
screen.exitonclick()

