import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
cList = ["red", "green", "blue", "cyan", "purple", "pink"]

bet = turtle.textinput("Place Your Bet!", "Type the colour of the turtle you think will win: ")
print(bet)

turtList = []
for i in range(len(cList)):
    print(i)
    newTurt = turtle.Turtle()
    newTurt.hideturtle()
    newTurt.color(cList[i])
    newTurt.penup()
    newTurt.setx(-200)
    newTurt.sety(80 - (20 * i))
    newTurt.pendown()
    newTurt.showturtle()
    turtList.append(newTurt)

def game(tList):
    end = False
    turt = tList
    while not end:
        for t in turt:
            dist = random.randint(0, 15)
            if (t.xcor() + dist >= 200):
                end = True
                return t.pencolor()
            t.forward(dist)

winner = game(turtList)

if(winner == bet.lower()):
    print(f"Congrats! You bet correctly, {bet} was the winner")
else:
    print(f"You Lose. The winner was {winner}")



screen.exitonclick()

