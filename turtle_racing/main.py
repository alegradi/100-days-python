from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_position = -100

for available_color in colors:
    turtle_instance = Turtle(shape="turtle")
    turtle_instance.penup()
    turtle_instance.color(available_color)
    turtle_instance.goto(x=-235, y=y_position)
    turtles.append(turtle_instance)
    y_position += 40

continue_race = True
winner = None

while continue_race:

    for turtle in turtles:
        if turtle.xcor() > 225:
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You won! The winner is: {winner_color}")
            else:
                print(f"you lose! The winner is: {winner_color}")
            continue_race = False
        else:
            turtle.forward(random.randint(1, 6))

screen.exitonclick()
