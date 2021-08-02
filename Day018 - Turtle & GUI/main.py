import random
import turtle
import colorgram

turtle.colormode(255)
cList = ["red", "blue", "green", "purple", "pink", "black", "brown", "yellow", "cyan", "wheat"]
turt = turtle.Turtle()
turt.shape("turtle")
turt.color("green")
length = 100

def r_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(90):
    turt.color(r_color())
    turt.circle(100)
    turt.right(4)


screen = turtle.Screen()
screen.exitonclick()