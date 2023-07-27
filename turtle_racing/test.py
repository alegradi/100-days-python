from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_position = -100

teddy = Turtle(shape="turtle")
teddy.color("red")
teddy.penup()
teddy.goto(x=-235, y=0)

turtles.append(teddy)

tobby = Turtle(shape="turtle")
tobby.color("green")
tobby.penup()
tobby.goto(x=-235, y=40)

turtles.append(tobby)

winner = None

def game_loop(target):
    global game_over, winner
    if target.xcor() >= 200:
        game_over = True
        print(f"X coordinate of {target.color()}: {target.xcor()}")
        winner = target
        return game_over
    else:
        print(f"X coordinate of {target.color()}: {target.xcor()}")


game_over = False

while not game_over:
    for racer in turtles:
        racer.forward(random.randint(1, 15))
        game_over = game_loop(racer)

print(f"The winner is: {winner.color()}")

screen.exitonclick()