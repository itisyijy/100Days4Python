# Day19 for 100Days4Python
# Day19 : Turtle Graphics | Event Listeners

import turtle
from turtle import Turtle, Screen

turtle.title("Etch A Sketch")
toto = Turtle()
screen = Screen()

def move_forwards():
    toto.forward(10)

def move_backwards():
    toto.backward(10)
    
def turn_right():
    toto.right(10)

def turn_left():
    toto.left(10)

def clear_drawing():
    toto.clear()
    toto.penup()
    toto.home()
    toto.pendown()
    # toto.reset()

screen.listen()

# function as input(argument) -> function name without parenthesis
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=clear_drawing, key="c")

screen.exitonclick()