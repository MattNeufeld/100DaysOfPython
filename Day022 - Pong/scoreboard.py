from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.aiScore = 0
        self.sety(270)
        self.color("white")
        self.write(str(self.score) + " : " + (str(self.aiScore)), align="center", font=("Arial", 14, "normal"))
        self.penup()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(str(self.score) + " : " + (str(self.aiScore)), align="center", font=("Arial", 14, "normal"))

    def game_overP(self):
        self.setpos(0,0)
        self.write("GAME OVER!", align="center", font=("Arial", 14, "normal"))
        self.setpos(0, -30)
        self.write("Player Wins", align="center", font=("Arial", 14, "normal"))

    def game_overAI(self):
        self.setpos(0,0)
        self.write("GAME OVER!", align="center", font=("Arial", 14, "normal"))
        self.setpos(0, -30)
        self.write("Computer Wins", align="center", font=("Arial", 14, "normal"))