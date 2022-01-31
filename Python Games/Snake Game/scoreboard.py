from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.score_update()

    # Initial Scoreboard
    def score_update(self):
        self.goto(-10, 270)
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier New", 15, "normal"))

    # Increasing Score and updating in scoreboard
    def score_increase(self):
        self.score += 1
        self.clear()
        self.score_update()

    # Printing Game over
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Courier New", 15, "normal"))
