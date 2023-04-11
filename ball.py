from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("white")
        self.penup()

    def first_play(self, side):
        if side == "right":
            self.setheading(randint(-30, 30))
        elif side == "left":
            self.setheading(randint(140, 210))

    def return_to_mid(self):
        self.goto(0, 0)
