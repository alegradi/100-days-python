from turtle import Turtle

SCORE_X = 0
SCORE_Y = 270
ALIGNMENT = "center"
FONT = ("Rubik", 12, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as file:
            stored_highescore = file.read()
            self.highscore = int(stored_highescore)
        # self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCORE_X, SCORE_Y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

            # Save highscore in file
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     text = f"GAME OVER!"
    #     self.write(text, move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
