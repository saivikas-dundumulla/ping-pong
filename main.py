import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(0.1)
    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect the collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.increase_level()
        ball.bounce_x()
    # Detect the collision with the right wall
    if ball.xcor() > 380:
        score_board.increment_l_score()
        ball.reset_position()
    # Detect the collision with the left wall
    if ball.xcor() < -380:
        score_board.increment_r_score()
        ball.reset_position()

screen.exitonclick()