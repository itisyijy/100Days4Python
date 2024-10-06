# Day22 for 100Days4Python
# Project for Day22 : The Pong Game

from turtle import Screen
from paddle import Paddle

LEFT = (-350, 0)
RIGHT = (350, 0)

# Create the screen
screen = Screen()
r_paddle = Paddle(RIGHT)
l_paddle = Paddle(LEFT)

screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_down, key="s")

is_game_on = True
while is_game_on:
    screen.update()



# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

screen.exitonclick()
