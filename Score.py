from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-290, 270)
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align="left", font=("Arial", 15, "bold"))

    def GameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 20, "bold"))

    def score_increament(self):
        self.score += 1
        self.clear()
        self.update()
