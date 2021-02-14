import random
import turtle
from turtle import Turtle
from scoreboard import Scoreboard


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            random_color = random.randint(0, 5)
            new_car.color(COLORS[random_color])
            new_car.pencolor("black")
            random_y = random.randint(-230, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.penup()
            car.bk(5)





