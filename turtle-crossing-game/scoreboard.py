from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")

    def show_level(self):
        self.goto(230, 260)
        self.write(f"Level:{self.level}", move=True, align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
