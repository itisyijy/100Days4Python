# Day22 for 100Days4Python
# Project for Day22 : The Pong Game

from turtle import Turtle


# Create the ball and make it move
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(0, 0)
        self.x_dir = 10
        self.y_dir = 10
    
    def bounce(self, wall=False, paddle=False):
        if wall:
            self.y_dir *= -1
        if paddle:
            self.x_dir *= -1
    
    def move(self):
        now_x = self.xcor()
        now_y = self.ycor()
        new_y = now_y + self.y_dir
        new_x = now_x + self.x_dir
        self.goto(new_x, new_y)
