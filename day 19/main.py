from turtle import Turtle, Screen

tim=Turtle()
tim.shape("turtle")

screen=Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    #tim.left(180)
    tim.backward(10)

def counter_clockwise():
    tim.left(45)

def clockwise():
    tim.right(45)

def clear():
    tim.clear()
    tim.pu()
    tim.home()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='a',fun=counter_clockwise)
screen.onkey(key='d',fun=clockwise)
screen.onkey(key='c',fun=clear)

screen.exitonclick()