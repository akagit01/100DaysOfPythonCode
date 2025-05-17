import random
from turtle import Turtle
from turtle import Screen
from random import choice
"""
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 30)

rgb_colors=[]
for color in colors:
    r=color.rgb.r
    b=color.rgb.b
    g=color.rgb.g
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

tim=Turtle()
color_list=[(235, 216, 83), (230, 154, 67), (48, 102, 145), (113, 177, 208), (215, 130, 145), (161, 23, 52), (174, 79, 31), (225, 53, 82), (194, 156, 19), (171, 51, 76), (42, 182, 137), (120, 196, 161), (241, 162, 186), (72, 28, 52), (234, 71, 39), (105, 106, 184), (143, 226, 190), (27, 31, 65), (132, 213, 231), (166, 28, 19), (41, 47, 131), (43, 141, 90), (46, 169, 186), (244, 165, 155), (212, 219, 14), (33, 81, 79)]

tim.pensize(10)
tim.screen.colormode(255)
tim.color("white")
tim.setposition(-240,-240)
tim.speed("fastest")
#tim.color("black")
#for rgb in (random.choice(color_list)):
#    print(rgb)

#def select_color():
#    rgb_color = random.choice(color_list)
#    tim.color(rgb_color)
#    return rgb_color

def draw_dots():
    for steps in range(9):

        tim.color(random.choice(color_list))
        tim.dot()
        tim.pu()
        tim.forward(50)
        tim.pd()
        tim.dot()

def turn_left():
    tim.left(90)
    tim.color("white")
    tim.forward(50)
    tim.left(90)

def position_tim():
    tim.pu()
    x=tim.xcor()
    y=tim.ycor()
    tim.setposition(-240,y+50)


for i in range(10):
    draw_dots()
    position_tim()
tim.hideturtle()
print(tim.pos())


#for i in range(10):
#    draw_dots()
    #turn_left()
    #tim.right(90)
screen=Screen()
screen.exitonclick()