# Day22 for 100Days4Python
# Project for Day22 : The Pong Game

from turtle import Turtle


# Keep score
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.l_score = 0
        self.r_score = 0
        self.show_score()
    
    def show_score(self):
        self.write(f"{self.l_score}\t{self.r_score}", align="center", font=('Arial', 30, 'normal'))
    
    def update_score(self, left=False, right=False):
        if left:
            self.l_score += 1
        if right:
            self.r_score += 1
        self.clear()
        self.show_score()
        