from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.pencolor("black")
        self.penup()
        self.left(90)
        self.move_speed = 0.1
        self.start_position()

    def start_position(self):
        self.goto(STARTING_POSITION)
        self.move_speed *= 0.9

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)