import random
import turtle
from turtle import Turtle, Screen

color_list = [(238, 250, 244), (188, 19, 46), (244, 233, 62), (218, 239, 245), (251, 227, 233),
              (195, 76, 34), (218, 66, 106), (14, 142, 88), (195, 175, 19), (21, 125, 173), (109, 182, 209),
              (18, 167, 213), (208, 154, 91), (25, 40, 74), (183, 43, 64), (36, 43, 111), (78, 175, 96), (234, 231, 5),
              (216, 67, 48), (216, 130, 153), (124, 184, 120), (237, 161, 180), (8, 61, 38), (148, 209, 220),
              (10, 92, 54), (6, 87, 109), (159, 30, 27), (160, 211, 182), (233, 171, 165), (86, 27, 63),
              (115, 120, 151), (180, 186, 212), (93, 29, 23), (245, 11, 38)]

painting = Turtle()
turtle.colormode(255)
painting.speed(5)
painting.ht()


def draw_spot():
    painting.dot(20, random.choice(color_list))


rows = 10
columns = 10
distance = 50

starting_x = 0 - ((columns * distance) / 2)
starting_y = 0 - ((rows * distance) / 2)

painting.penup()

for j in range(rows):
    y_position = starting_y + (j * distance)
    painting.setpos(float(starting_x), float(y_position))

    for i in range(columns):
        painting.pendown()
        draw_spot()
        painting.penup()
        painting.forward(distance)







screen = Screen()
screen.exitonclick()
