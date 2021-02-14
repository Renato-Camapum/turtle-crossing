import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light grey")
screen.title("Why did the turtle cross the street?")
screen.tracer(0)

game_is_on = True
turtle = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkeypress(turtle.move, "Up")


while game_is_on:
    time.sleep(turtle.move_speed)
    screen.update()
    car.create_car()
    car.move_car()

    if turtle.ycor() > 280:
        score.level_sum()
        turtle.start_position()

    for car_ in car.all_cars:
        if turtle.distance(car_) < 25:
            game_is_on = False
            score.game_over()

screen.exitonclick()
