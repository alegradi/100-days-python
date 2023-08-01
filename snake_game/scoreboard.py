from turtle import Turtle

SCORE_X = 0
SCORE_Y = 270
ALIGNMENT = "center"
FONT = ("Rubik", 12, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCORE_X, SCORE_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        text = f"Score: {self.score}"
        self.write(text, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        text = f"GAME OVER!"
        self.write(text, move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
