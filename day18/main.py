import random
import turtle as t
from turtle import Screen


timmy=t.Turtle()
timmy.shape("turtle")
t.colormode(255)




#colors=['red','green','yellow','blue','purple','black','orange']
direction=[0,90,180,270]
timmy.pensize(15)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color= (r,g,b)
    return (random_color)

def draw_shape(no_of_sides):

    for i in range(3,no_of_sides):
        timmy.color(random_color())
        for j in range(1,i+1):
            timmy.forward(100)
            timmy.right(360/i)

def random_walk():
    timmy.speed("fastest")
    for i in range(300):
        timmy.color(random_color())
        timmy.forward(50)
        timmy.setheading(random.choice(direction))




timmy.pensize(1)
timmy.speed("fastest")

def draw_spirograph(size_of_graph):
    for i in range(int(360/size_of_graph)):
        timmy.color(random_color())
        current_heading=timmy.heading()
        timmy.circle(100)
        timmy.setheading(current_heading+size_of_graph)


draw_spirograph(10)
screen = Screen()
screen.exitonclick()