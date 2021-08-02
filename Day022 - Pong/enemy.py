from turtle import Turtle

class Enemy:

    def __init__(self):
        turt = Turtle()
        turt.shape("square")
        turt.color("white")
        turt.shapesize(stretch_len=5, stretch_wid=1)
        turt.setheading(90)
        turt.penup()
        turt.setpos(280, 0)
        self.body = turt

    def move(self):
        if(self.body.ycor() > 270):
            self.body.setheading(270)
        elif (self.body.ycor() < -270):
            self.body.setheading(90)
        self.body.forward(10)
