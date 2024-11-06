from turtle import Screen, Turtle
from paddle import  Paddle
from ball import Ball
from scoreboard import  Scoreboard
import time
screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle=Paddle(360,0)
l_paddle=Paddle(-360,0)
my_ball=Ball()
score=Scoreboard()




screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(my_ball.move_speed)
    screen.update()
    my_ball.move()

    if my_ball.ycor() > 280 or my_ball.ycor() <-300:

        my_ball.y_bounce()

    if my_ball.distance(r_paddle)<50 and my_ball.xcor()>340 or my_ball.distance(l_paddle)<50 and my_ball.xcor()<-340:

        my_ball.x_bounce()


    if my_ball.xcor() > 380:
        my_ball.reset_position()
        score.l_point()

    if my_ball.xcor() < -380:
        my_ball.reset_position()
        score.r_point()


screen.exitonclick()