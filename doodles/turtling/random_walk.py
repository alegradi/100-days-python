import random
import turtle
from turtle import Turtle, Screen

walk = Turtle()

# Turtle variables
# walk.shape("arrow")
walk.pendown()
turtle.colormode(255)
walk.speed(8)
turtle.pensize(15)


def random_movement():
    directions = [0, 90, 180, 270]
    angle = random.choice(directions)
    turtle.forward(50)
    turtle.setheading(angle)


def change_pen_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    turtle.pencolor(r, g, b)


n = 0

for _ in range(200):
    change_pen_color()
    random_movement()



screen = Screen()
screen.exitonclick()
