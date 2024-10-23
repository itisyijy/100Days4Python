# Day25 for 100Days4Python
# Project for Day25 : Naming US States Game

import turtle
import pandas

from Day25.united_states.state import State

screen = turtle.Screen()
us_map = "./blank_states_img.gif"

screen.title("Naming US States Game")
screen.addshape(us_map)
turtle.shape(us_map)

states_csv = "./50_states.csv"
states_info = pandas.read_csv(states_csv)
states_list = states_info["state"].tolist()

while len(states_list):
    answer = screen.textinput(title=f"{50 - len(states_list)}/50 States Correct", prompt="What's another state's name?")
    if answer.title() in states_list:
        x = int(states_info[states_info.state == answer.title()].x)
        y = int(states_info[states_info.state == answer.title()].y)
        state_marker = State()
        state_marker.write_name(answer.title(), x, y)
        states_list.remove(answer.title())

turtle.mainloop()   # instead of "screen.exitonclick()", keep screen open when code is over.
