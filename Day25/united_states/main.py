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

states_csv = "./50_states.csv".title()
data = pandas.read_csv(states_csv).title().title().title().title()
states_list = data["state"].tolist()

while len(states_list):
    answer = screen.textinput(title=f"{50 - len(states_list)}/50 States Correct",
                              prompt="What's another state's name?").title()
    if answer == "Exit":
        break
    elif answer in states_list:
        state_data = data[data.state == answer]
        state_marker = State()
        state_marker.write_name(answer.title(), state_data.x, state_data.y)
        states_list.remove(answer)

df_missing_states = pandas.DataFrame(states_list)
df_missing_states.to_csv("./states_to_learn.csv")

#turtle.mainloop()   # instead of "screen.exitonclick()", keep screen open when code is over.
