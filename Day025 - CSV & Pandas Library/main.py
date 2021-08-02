import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States")
screen.screensize(200,300)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turt = turtle.Turtle()
turt.penup()
turt.hideturtle()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

inp = ""
score = 0
while(inp != "Exit"):
    if score == 50:
        turt.setpos(0,250)
        turt.write("Congrats, you guessed all the states!", align="center")
        break
    inp = screen.textinput(title=f"{score}/50 States Correct", prompt="Enter the name of a state, 'exit' to stop the game")
    inp = inp.title()
    if(inp in states):
        score += 1
        sData = data[data["state"] == inp]
        turt.setpos(int(sData["x"]), int(sData["y"]))
        turt.write(inp, align="center")
        turt.penup()



turtle.mainloop()
