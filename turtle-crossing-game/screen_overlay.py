from turtle import Turtle

FONT = ("Courier", 12, "normal")


class ScreenOverlay(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("Black")
        self.pensize(3)
        self.draw_bottom()
        self.draw_top()

    def draw_bottom(self):
        self.goto(-220, -260)
        self.pendown()
        self.goto(290, -260)
        self.penup()
        self.goto(-285, -270)
        self.write("Start", align="left", font=FONT)

    def draw_top(self):
        self.goto(-220, 260)
        self.pendown()
        self.goto(290, 260)
        self.penup()
        self.goto(-285, 250)
        self.write("Finish", align="left", font=FONT)
