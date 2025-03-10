import time
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



    #Detect collision with food
    if snake.segment[0].distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() > 290 or snake.segment[0].ycor() < -290:

        scoreboard.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment)<10:
            scoreboard.reset()
            snake.reset()



















screen.exitonclick()