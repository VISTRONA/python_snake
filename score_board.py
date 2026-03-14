from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))
        self.hideturtle()
        self.penup()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))

    def game_over(self):
        self.clear()
        self.write("Game Over", align="center", font=("Times-New-Roman", 30, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


