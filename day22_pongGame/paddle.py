from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        #self.xcor=xcor
        #self.ycor=ycor
        self.shape("square")
        self.color("white")
        #self.width(20)
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.pu()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


