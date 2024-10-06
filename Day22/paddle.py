# Day22 for 100Days4Python
# Project for Day22 : The Pong Game

from turtle import Turtle

PADDLE_MOVE = 20


# Create and move a paddle
class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(cor)
        
    def go_up(self):
        new_y = self.ycor() + PADDLE_MOVE
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - PADDLE_MOVE
        self.goto(self.xcor(), new_y)
