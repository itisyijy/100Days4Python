# Day23 for 100Days4Python
# Project for Day23 : Turtle Crossing
import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randrange(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)
    
    def level_up(self):
        self.move_speed += MOVE_INCREMENT