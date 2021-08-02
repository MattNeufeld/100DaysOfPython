from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

end = False

while not end:
    screen.update()
    snake.move()
    time.sleep(0.1)
    if(snake.s_body[0].distance(food.xcor(), food.ycor()) <= 10):
        snake.newS()
        food.newL()
        score.update_score()
    if snake.s_body[0].xcor() >= 290 or snake.s_body[0].xcor() <= -290 or snake.s_body[0].ycor() >= 290 or snake.s_body[0].ycor() <= -290:
        score.game_over()
        end = True

    for seg in snake.s_body[1:]:
        if snake.s_body[0].distance(seg.xcor(), seg.ycor()) < 10:
            score.game_over()
            end = True

screen.exitonclick()