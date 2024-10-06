# Day22 for 100Days4Python
# Project for Day22 : The Pong Game

from turtle import Turtle


class Layout(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
    
    def draw_out_line(self):
        self.goto(-400, 300)
        self.pendown()
        self.goto(400, 300)
        self.goto(400, -300)
        self.goto(-400, -300)
        self.goto(-400, 300)
        self.penup()
    
    def draw_half_line(self):
        y = 300
        self.goto(0, y)
        while y > -300:
            y -= 10
            self.penup()
            if (y / 10) % 2 != 0:
                self.pendown()
            self.goto(0, y)