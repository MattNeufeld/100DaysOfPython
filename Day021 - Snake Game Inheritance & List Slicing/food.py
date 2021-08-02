from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.setpos(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))

    def newL(self):
        self.setpos(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))