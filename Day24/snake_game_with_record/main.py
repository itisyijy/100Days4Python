# Day24 for 100Days4Python
# Day24 : Access Local Files and Directories
# Project for Day20_21 : Snake Game
# Project for Day24 : Snake Game with High Score

import time
from food import Food
from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
from outline import Outline, LIMIT

FOOD_DISTANCE = 15

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
outline = Outline()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # 4. detect collision with food
    if snake.head.distance(food) <= FOOD_DISTANCE:
        snake.extend()
        food.refresh()
        scoreboard.update_score()
    
    # 6. detect collision with wall
    if (snake.head.xcor() <= -LIMIT or snake.head.xcor() >= LIMIT
            or snake.head.ycor() <= -LIMIT or snake.head.ycor() >= LIMIT):
        # Day 24
        snake.reset()
        scoreboard.update_record()
        
    # 7. detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # Day 24
            snake.reset()
            scoreboard.update_record()
screen.exitonclick()
