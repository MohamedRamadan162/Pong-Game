from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
mid = Turtle()
mid.hideturtle()
mid.penup()
mid.goto(0, -400)
mid.setheading(90)
mid.color("white")
mid.pensize(5)


while mid.ycor() <= 300:
    mid.forward(15)
    mid.pendown()
    mid.forward(15)
    mid.penup()

fora = int(screen.textinput("El fora", "3ayez el fora mn kam?"))
r_paddle = Paddle("right")
l_paddle = Paddle("left")
ball = Ball()
l_scoreboard = ScoreBoard("left")
r_scoreboard = ScoreBoard("right")
ball.first_play("right")
screen.update()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


def return_everything_to_position():
    ball.return_to_mid()
    r_paddle.return_to_mid()
    l_paddle.return_to_mid()
    screen.update()
    time.sleep(1)


c = 0
run = True
while run:
    speed = 10 + c * 2
    ball.forward(speed)
    time.sleep(0.05)
    if (ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50) and abs(ball.xcor()) >= 330:
        ball.setheading(180-ball.heading())
        c += 1

    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.setheading(-ball.heading())

    if ball.xcor() >= 380:
        c = 0
        l_scoreboard.increase_score()
        if r_scoreboard.score == fora:
            r_scoreboard.player_win("Red")
            break
        elif l_scoreboard.score == fora:
            l_scoreboard.player_win("Blue")
            break
        return_everything_to_position()
        ball.first_play("left")

    if ball.xcor() <= -380:
        c = 0
        r_scoreboard.increase_score()
        if r_scoreboard.score == fora:
            r_scoreboard.player_win("Red")
            break
        elif l_scoreboard.score == fora:
            l_scoreboard.player_win("Blue")
            break
        return_everything_to_position()
        ball.first_play("right")

    screen.update()


screen.exitonclick()
