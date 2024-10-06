# Day22 for 100Days4Python
# Project for Day22 : The Pong Game

import time
from scoreboard import Scoreboard
from ball import Ball
from turtle import Screen
from paddle import Paddle
from layout import Layout

LEFT = (-350, 0)
RIGHT = (350, 0)

# Create the screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=900, height=700)
screen.tracer(0)

layout = Layout()
layout.draw_out_line()
layout.draw_half_line()

ball = Ball()
r_paddle = Paddle(RIGHT)
l_paddle = Paddle(LEFT)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up")
screen.onkeypress(fun=l_paddle.go_up, key="w")
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_down, key="s")

is_bounce = False
is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if -10 <= ball.xcor() <= 10:
        is_bounce = False
    
    # Detect collision with wall and bounce
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce(wall=True)
    
    # Detect collision with paddle
    if ((ball.xcor() > 320 and ball.distance(r_paddle) < 50) or
            (ball.xcor() < -320 and ball.distance(l_paddle) < 50)):
        if not is_bounce:
            ball.bounce(paddle=True)
            is_bounce = True

    # Detect when paddle misses
    if ball.xcor() >= 390 or ball.xcor() <= -390:
        if ball.xcor() >= 390:
            scoreboard.update_score(left=True)
        if ball.xcor() <= -390:
            scoreboard.update_score(right=True)
        ball.goto(0, 0)
        ball.bounce(paddle=True)
        time.sleep(1)

screen.exitonclick()
