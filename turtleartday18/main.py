from turtle import Turtle, Screen, colormode
import random

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
#            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
degrees = [90, 180, 0, 270]
colormode(255)
def random_color():
    r= random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)
timmy_the_turtle=Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
 
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
def draw_spirograph(size_of_gap):


    for _ in range(int(360/size_of_gap)):
        # directions = [timmy_the_turtle.right, timmy_the_turtle.left]
        # set_direction = random.choice(directions)
        # set_direction(random.choice(degrees))
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.pensize(5)
        timmy_the_turtle.speed('fastest')
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading()+size_of_gap)
draw_spirograph(5)
screen = Screen()
screen.exitonclick()

