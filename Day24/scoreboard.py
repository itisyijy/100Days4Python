# Day24 for 100Days4Python
# Day24 : Access Local Files and Directories
# Project for Day20_21 : Snake Game
# Project for Day24 : Snake Game with High Score

from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "normal")


# 5. create a scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0

        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 300)
        self.show_scoreboard()
    
    def show_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_scoreboard()

    def game_over(self):
        self.home()
        self.write(f"Game Over", align=ALIGN, font=FONT)
