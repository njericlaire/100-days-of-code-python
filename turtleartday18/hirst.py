# import colorgram
# rgb_colors=[] 
# color=colorgram.extract('turtleartday18/image.jpg',10)
# for color in color:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as t
import random
t.colormode(255)
color=[(210, 165, 122), (246, 232, 234), (140, 49, 106), (164, 169, 38), (245, 79, 56), (218, 234, 231), (232, 112, 163), (3, 141, 50), (64, 200, 221)]
tim=t.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100


for dot_count in range(1,number_of_dots+1):
   
    tim.dot(20, random.choice(color))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=t.Screen()
screen.exitonclick()