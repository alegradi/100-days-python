from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y_position = -100


def has_won(target):
    global game_over, winner
    if target.xcor() > 200:
        game_over = True
        winner = target
        return game_over
    else:
        return game_over

game_over = False
winner = None

for available_color in colors:
    turtle_instance = Turtle(shape="turtle")
    turtle_instance.penup()
    turtle_instance.color(available_color)
    turtle_instance.goto(x=-235, y=y_position)
    turtles.append(turtle_instance)
    y_position += 40

we_have_winner = False

while not we_have_winner:
    for individual_turtle in turtles:
        individual_turtle.forward(random.randint(1, 15))
        print(individual_turtle.color())
        print(individual_turtle.xcor())
        print("-----------------------------")
        we_have_winner = has_won(individual_turtle)

winner_color = winner.color()[0]

if user_bet == winner_color:
    print(f"You won! The winner is: {winner.color()[0]}")
else:
    print(f"you lose! The winner is: {winner.color()[0]}")


screen.exitonclick()

