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
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.create_car()
    cars.move()
    
    # Detect collision with car
    for car in cars.all_cars:
        if player.distance(car) <= 20:
            scoreboard.game_over()
            game_is_on = False
            break
    
    # Detect collision with finish line
    if player.ycor() >= 280:
        player.start_position()
        scoreboard.update_level()
        cars.level_up()
        time.sleep(1)

screen.exitonclick()
