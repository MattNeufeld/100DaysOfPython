from turtle import Screen, Turtle

class Snake:

    def __init__(self):
        self.s_body = []
        self.create_s(3)

    def create_s(self, size):
        for i in range(size):
            turt = Turtle()
            turt.shape("square")
            turt.color("white")
            turt.penup()
            turt.setpos(0 - (i * 20), 0)
            self.s_body.append(turt)

    def move(self):
        for seg in range(len(self.s_body) - 1, 0, -1):
            x = self.s_body[seg - 1].xcor()
            y = self.s_body[seg - 1].ycor()
            self.s_body[seg].goto(x, y)
        self.s_body[0].forward(20)

    def newS(self):
        turt = Turtle()
        turt.shape("square")
        turt.color("white")
        turt.penup()
        last = len(self.s_body)
        turt.setpos(self.s_body[last - 1].xcor(), self.s_body[last - 1].ycor())
        self.s_body.append(turt)

    def up(self):
        if self.s_body[0].heading() != 270:
            self.s_body[0].setheading(90)

    def down(self):
        if self.s_body[0].heading() != 90:
            self.s_body[0].setheading(270)

    def right(self):
        if self.s_body[0].heading() != 180:
            self.s_body[0].setheading(0)

    def left(self):
        if self.s_body[0].heading() != 0:
            self.s_body[0].setheading(180)