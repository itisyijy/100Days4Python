# Day25 for 100Days4Python
# Project for Day25 : United States

from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def write_name(self, name, x, y):
        self.goto(int(x.iloc[0]), int(y.iloc[0]))
        self.write(name)
