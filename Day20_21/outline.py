# Day20_21 for 100Days4Python
# Project for Day20_21 : Snake Game

from turtle import Turtle

LIMIT = 290


class Outline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(LIMIT, LIMIT)
        self.pendown()
        self.goto(LIMIT, -LIMIT)
        self.goto(-LIMIT, -LIMIT)
        self.goto(-LIMIT, LIMIT)
        self.goto(LIMIT, LIMIT)