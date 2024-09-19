# Day06 for 100Days4Python
# Function & While  Loop

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

def jump_1():               # # jump 1-height huddle
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def jump_n():               # jump n-height huddle
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

# TASK : huddle 1
for step in range(0, 6):
    jump_1()

# TASK : huddle 2
while not at_goal():
    move()
    jump_1()

# TASK : huddle 3
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_1()

# TASK : huddle 4
while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_n()