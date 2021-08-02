import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.newC()
    car_manager.move()
    car_manager.clean()
    if(player.ycor() > 280):
        player.next()
        car_manager.next()
        scoreboard.score += 1
        scoreboard.update_score()
    for car in car_manager.cList:
        if car.distance(player) < 20 and abs(abs(car.ycor()) - abs(player.ycor())) < 15:
            game_is_on = False
            scoreboard.game_over()
    screen.update()
screen.exitonclick()
