from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1

    def move_ball(self):
        self.pu()
        new_xcor=self.xcor() + self.x_move
        new_ycor=self.ycor() + self.y_move
        self.goto(new_xcor,new_ycor)

    def bounce_ball_y(self):
        self.y_move *= -1


    def bounce_ball_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball_position(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.bounce_ball_x()



