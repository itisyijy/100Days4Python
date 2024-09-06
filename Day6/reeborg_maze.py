# Day6 for 100Days4Python
# Project for Day4

# Try Reeborg : https://reeborg.ca/index_en.html

# built-in functions
def move():             # basic function
    return
def turn_left():        # basic function
    return
def at_goal():          # basic function
    return
def front_is_clear():   # basic function
    return
def right_is_clear():
    return
def wall_in_front():    # basic function
    return
def wall_on_right():
    return

# customized functions
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# TASK : maze
while front_is_clear():     # force to meet wall on right
    move()
turn_left()

while not at_goal():        # move following the right side of wall
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()