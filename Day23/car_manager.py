# Day23 for 100Days4Python
# Project for Day23 : Turtle Crossing
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.now_x = 300
        self.now_y = random.randrange(-240, 241)
        self.goto(self.now_x, self.now_y)
        self.move_speed = STARTING_MOVE_DISTANCE
        
    def move(self, level):
        if self.xcor() > -320 :
            self.goto(self.xcor() - (self.move_speed + MOVE_INCREMENT * level), self.now_y)
            