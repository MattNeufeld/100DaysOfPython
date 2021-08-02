from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.sety(260)
        self.setx(-220)
        self.color("black")
        self.write("Level: " + str(self.score), align="center", font=FONT)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write("Level: " + str(self.score), align="center", font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME OVER!", align="center", font=("Arial", 14, "normal"))
