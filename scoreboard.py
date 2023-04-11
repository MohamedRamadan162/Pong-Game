from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        if side == "right":
            self.goto(100, 180)
        elif side == "left":
            self.goto(-100, 180)
        self.write(self.score, False, "center", font=("courier", 88, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, False, "center", font=("courier", 88, "normal"))

    def player_win(self, player_color):
        self.goto(0, 0)
        self.write(f"{player_color} player wins!", False, "center", ("Arial", 46, "normal"))