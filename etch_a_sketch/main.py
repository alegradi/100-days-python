from turtle import Turtle, Screen

sketch = Turtle()
screen = Screen()


def move_forward():
    sketch.forward(10)


def move_backwards():
    sketch.backward(10)


def turn_right():
    sketch.right(2)


def turn_left():
    sketch.left(2)


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=sketch.clear, key="c")








screen.exitonclick()
