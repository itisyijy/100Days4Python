# Day23 for 100Days4Python
# Project for Day23 : Turtle Crossing

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=700)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.up, key="Up")

level = 1
cars = []
car_gap = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if car_gap % 6 == 0:
        car_gap = 0
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.move(level - 1)
    car_gap += 1
    
    for car in cars:
        if -25 <= car.xcor() <= 25 and player.ycor() -20 <= car.ycor() <= player.ycor() + 20:
            scoreboard.game_over()
            game_is_on = False
            break
    if player.ycor() >= 290:
        level += 1
        player.start_position()
        scoreboard.update_level(level)
        time.sleep(1)
        car = []
screen.exitonclick()
