from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        if side == "right":
            self.color("red")
            self.o_xcor = 350
            self.goto(self.o_xcor, 0)
        if side == "left":
            self.color("blue")
            self.o_xcor = -350
            self.goto(self.o_xcor, 0)
        self.setheading(90)

    def up(self):
        if self.ycor() <= 280:
            self.setheading(90)
            self.forward(20)

    def down(self):
        if self.ycor() >= -280:
            self.setheading(270)
            self.forward(20)

    def return_to_mid(self):
        self.goto(self.o_xcor, 0)
