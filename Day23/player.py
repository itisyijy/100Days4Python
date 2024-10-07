# Day23 for 100Days4Python
# Project for Day23 : Turtle Crossing

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.start_position()
    
    def start_position(self):
        self.goto(0, -280)
        
    def up(self):
        self.goto(0, self.ycor() + 10)
    