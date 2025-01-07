from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.mov_up, "Up")
screen.onkey(r_paddle.mov_down, "Down")
screen.onkey(l_paddle.mov_up, "w")
screen.onkey(l_paddle.mov_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.mov_speed)
    screen.update()
    ball.mov_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        ball.speed()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_opp()

    if ball.xcor() > 380:
        ball.home()
        time.sleep(0.1)
        ball.bounce_opp()
        score.l_point()
    elif ball.xcor() < -380:
        ball.home()
        time.sleep(0.1)
        ball.bounce_opp()
        score.r_point()

screen.exitonclick()
