from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from enemy import Enemy
from ball import Ball
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()
enemy = Enemy()
score = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(paddle.up, "w")
screen.onkeypress(paddle.down, "s")

end = False

while not end:
    time.sleep(0.05)
    enemy.move()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounceY()

    if ball.distance(paddle.body) < 65 and ball.xcor() < -270:
        ball.bounceX()
    if ball.distance(enemy.body) < 65 and ball.xcor() > 270:
        ball.bounceX()

    if ball.xcor() > 300:
        score.score += 1
        ball.resetPlayer()
        score.update_score()
    if ball.xcor() < -300:
        score.aiScore += 1
        ball.resetAI()
        score.update_score()

    if score.score == 5:
        end = True
        score.game_overP()
        ball.hideturtle()
    elif score.aiScore == 5:
        end = True
        score.game_overAI()
        ball.hideturtle()

    screen.update()

screen.exitonclick()