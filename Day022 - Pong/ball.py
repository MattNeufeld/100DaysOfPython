from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.setheading(0)
        self.xDir = 10
        self.yDir = 10
        self.mvSpeed = 1

    def move(self):
        x = self.xcor() + self.xDir
        y = self.ycor() + self.yDir
        self.goto(x,y)

    def bounceY(self):
        self.yDir = -1 * self.yDir * self.mvSpeed

    def bounceX(self):
        self.mvSpeed += 0.05
        self.xDir = -1 * self.xDir * self.mvSpeed

    def resetAI(self):
        self.setpos(0, 0)
        self.xDir = 10
        self.yDir = 10
        self.mvSpeed = 1

    def resetPlayer(self):
        self.setpos(0, 0)
        self.xDir = -10
        self.yDir = -10
        self.mvSpeed = 1