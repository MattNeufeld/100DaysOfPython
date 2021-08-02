from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.sety(270)
        self.color("white")
        self.write("Score: " + str(self.score), align="center", font=("Arial", 14, "normal"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write("Score: " + str(self.score), align="center", font=("Arial", 14, "normal"))

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER!", align="center", font=("Arial", 14, "normal"))