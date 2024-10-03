# Day19 for 100Days4Python
# Day19 : Turtle Graphics | State and Multiple Instances

# State of attributes can be different between objects from same class
# Each object functions independently -> each separate Instance

import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win?")
rainbow = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]
all_turtles = []

for color in rainbow:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=-150 + 50 * rainbow.index(color))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() >= 230:
            is_race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            break
        random_distance = random.randint(0, 10)
        t.forward(random_distance)
    
screen.exitonclick()