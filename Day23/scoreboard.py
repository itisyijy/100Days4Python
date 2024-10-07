# Day23 for 100Days4Python
# Project for Day23 : Turtle Crossing
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.show_level(self.level)
    
    def show_level(self, level):
        self.goto(-150, 300)
        self.write(f"Level: {level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.show_level(self.level)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        