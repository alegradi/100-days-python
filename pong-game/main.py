from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Standard paddle coordinates
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

r_score = 0
l_score = 0

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()

    # Detect collision with top & bottom
    if ball.ycor() < -280 or ball.ycor() > 280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball moving past l_paddle
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    # Detect ball moving past r_paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()
