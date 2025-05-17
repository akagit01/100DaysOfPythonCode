import turtle
from turtle import Turtle, Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race: ")
print(user_bet)
colors=["pink","orange","blue","yellow","green","red"]
all_turtles=[]


""" this creates 6 turtle and assigns different colors and position to each"""
y_position=-100
for turtle_index in range(0,6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)
    y_position=y_position+30

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You won. The {winning_color} colored turtle is the winner")
            else:
                print(f"You lose. The {winning_color} colored turtle is the winner")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()