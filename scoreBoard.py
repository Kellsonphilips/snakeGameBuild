
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.highest_score)
        self.goto(x=0, y=270)
        self.color("white")
        self.update_scores()
        self.hideturtle()

    with open("data.txt") as high_score_value:
        highest_score = high_score_value.read()

    def update_scores(self):
        self.clear()

        self.write(f"Score: {self.score}  |  Highest Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score_value:
                high_score_value.write(f"{self.high_score}")
        self.score = 0
        self.update_scores()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        self.update_scores()
