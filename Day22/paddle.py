# Day22 for 100Days4Python
# Project for Day22 : The Pong Game

from turtle import Turtle

# Create and move a paddle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cor)
        
    def go_up(self):
        print("up")
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        print("down")
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
