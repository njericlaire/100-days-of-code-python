from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_foward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_right():
    tim.right(10)
def move_left():
    tim.left(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_foward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()