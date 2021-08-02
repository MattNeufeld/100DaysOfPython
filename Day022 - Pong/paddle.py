from turtle import Turtle

class Paddle:

    def __init__(self):
        turt = Turtle()
        turt.shape("square")
        turt.color("white")
        turt.shapesize(stretch_len=5, stretch_wid=1)
        turt.setheading(90)
        turt.penup()
        turt.setpos(-290, 0)
        self.body = turt

    def up(self):
        self.body.setheading(90)
        self.body.forward(10)

    def down(self):
        self.body.setheading(270)
        self.body.forward(10)
