from turtle import Turtle, Screen
import random

screen=Screen()
game_on=False
screen.setup(width=500, height=400)
color=['red','orange','yellow','green','blue','purple']
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
y_position=[-70,-40,-10,20,50,70]
all_turtle=[]
for i in range (6):
    tim=Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(-230,y_position[i])
    all_turtle.append(tim)

if user_bet:
    game_on=True

while game_on:
    
    for turtle in all_turtle:
        if turtle.xcor()>230:
            game_on=False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print(f"You've lost the winning color is {winning_color}")
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
    

screen.exitonclick()