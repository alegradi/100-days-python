from turtle import Turtle

# PADDLE_WIDTH = 20
# PADDLE_HEIGHT = 100
PADDLE_X = 350
PADDLE_Y = 0


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        paddle_x = coordinates[0]
        paddle_y = coordinates[1]
        self.goto(paddle_x, paddle_y)
        # Set the correct size
        self.seth(90)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.seth(90)
        if self.ycor() < 240:
            self.forward(20)

    def down(self):
        self.seth(270)
        if self.ycor() > -240:
            self.forward(20)
