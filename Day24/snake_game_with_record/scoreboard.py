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
        super().__init__()
        self.score = 0
        
        # Day 24
        self.record = 0
        self.read_record()
        
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 300)
        self.show_scoreboard()
    
    def read_record(self):
        with open("data.txt", mode="r") as data:
            self.record = int(data.read())
    
    def show_scoreboard(self):
        self.read_record()
        self.write(f"Score: {self.score} | Best Record: {self.record}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.show_scoreboard()

    # Day 24
    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", align=ALIGN, font=FONT)

    # Day 24
    def update_record(self):
        if self.record < self.score:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.clear()
        self.show_scoreboard()
        