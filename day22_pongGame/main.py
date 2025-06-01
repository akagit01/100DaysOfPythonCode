from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.tracer(0)
ball=Ball()
scoreboard=Scoreboard()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))


screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")

ball.move_ball()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
l_paddle_score=0
r_paddle_score=0
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_ball_y()

    #detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -320):
        ball.bounce_ball_x()

    #detect r_paddle missed the ball
    if ball.xcor()>380:
        ball.reset_ball_position()
        scoreboard.l_point()

    # detect l_paddle missed the ball
    if ball.xcor()<-380:
        ball.reset_ball_position()
        scoreboard.r_point()

    #print(f"r_paddle_score is {r_paddle_score} and l_paddle_Score is {l_paddle_score}")

screen.exitonclick()

