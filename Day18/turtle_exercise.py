# Day18 for 100Days4Python
# Day18 : Turtle Graphics | Tuples | Importing Modules

import random
import turtle
from turtle import Turtle, Screen

# Turtle
mbappe = Turtle()
mbappe.speed(0)
mbappe.shape("classic")
turtle.colormode(255)

# Draw a Square
turtle.title("Draw a Square")
def draw_square():
    for _ in range(4):
        mbappe.forward(100)
        mbappe.left(90)

# Draw a Dashed Line
turtle.title("Draw a Dashed Line")
def draw_dashed_line():
    for _ in range(15):
        mbappe.pendown()
        mbappe.forward(10)
        mbappe.penup()
        mbappe.forward(10)

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
turtle.title("Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon")
def shape_draw(num_sides):
    for _ in range(num_sides):
        mbappe.forward(100)
        mbappe.right(360 / num_sides)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)   # tuple
    return color

def draw_polygons():
    for n_sides in range(3, 11):
        mbappe.color(random_color())
        shape_draw(n_sides)

# Draw a Random Walk
turtle.title("Draw a Random Walk")
direction = [0, 90, 180, 270]

def random_walk(a_turtle, now, end):
    mbappe.width(5)
    if now == end:
        return
    mbappe.color(random_color())
    a_turtle.setheading(random.choice(direction))
    a_turtle.forward(30)
    random_walk(a_turtle, now + 1, end)

# Make a Spirograph
def draw_spirograph(num_circles):
    for _ in range(num_circles):
        mbappe.color(random_color())
        mbappe.setheading(mbappe.heading() + 360 / num_circles)
        mbappe.circle(100)

# TEST ALL FUNCTIONS
# draw_square()
# mbappe.reset()

# draw_dashed_line()
# mbappe.reset()

# draw_polygons()
# mbappe.reset()

# draw_spirograph(100)
# mbappe.reset()

# Screen
my_screen = Screen()
my_screen.exitonclick()