from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cList = []
        self.create_s(5)
        self.level = 1

    def create_s(self, size):
        for i in range(size):
            turt = Turtle()
            turt.shape("square")
            turt.color(random.choice(COLORS))
            turt.penup()
            turt.setheading(180)
            turt.shapesize(stretch_len=2, stretch_wid=1)
            turt.setpos(290, random.randint(-260, 260))
            self.cList.append(turt)

    def move(self):
        for car in self.cList:
            car.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (self.level - 1)))

    def newC(self):
        rand = random.randint(1,10)
        if(rand > 8):
            turt = Turtle()
            turt.shape("square")
            turt.color(random.choice(COLORS))
            turt.penup()
            turt.setheading(180)
            turt.shapesize(stretch_len=2, stretch_wid=1)
            turt.setpos(290, random.randint(-260, 260))
            self.cList.append(turt)

    def clean(self):
        for car in self.cList:
            if car.xcor() < -310:
                self.cList.remove(car)

    def next(self):
        self.level += 1
