# Day18 for 100Days4Python
# Project for Day18 : Damien Hirst's Spot Painting
import random
import turtle

import colorgram
from turtle import Turtle, Screen

ROW = 10
COL = 10
DOT_SIZE = 20
DOT_GAP = 50
INITIAL_X = -(DOT_GAP * ROW) / 2
INITIAL_Y = -(DOT_GAP * COL) / 2

palette = []
colors = colorgram.extract('image.jpg', 100)
for color in colors:
    rgb_code = (color.rgb.r, color.rgb.g, color.rgb.b)
    if not (rgb_code[0] > 230 and rgb_code[1] > 230 and rgb_code[2] > 230):
        palette.append(rgb_code)

trtl = Turtle()
trtl.speed(0)
trtl.shape("classic")
turtle.colormode(255)

trtl.penup()
trtl.hideturtle()
trtl.setx(INITIAL_X)
trtl.sety(INITIAL_Y)
for col in range(COL):
    trtl.setx(INITIAL_X)
    trtl.sety(INITIAL_Y + col * DOT_GAP)
    for row in range(ROW):
        trtl.dot(DOT_SIZE, random.choice(palette))
        trtl.forward(DOT_GAP)
        
screen = Screen()
screen.exitonclick()