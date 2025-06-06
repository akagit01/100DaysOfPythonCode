from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_Segment(position)


    def add_Segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        #add a new segment to snake
        self.add_Segment(self.segments[-1].position())


    def move(self):

        for seg_num in range(len(self.segments) - 1, 0, -1):  # (start=(3-1),stop=0,step=-1):
            new_xcor = self.segments[seg_num - 1].xcor()  # 3rd seg takes 2nd seg x-cor, y cor, 2nd seg takes 1st seg x,y cor.śkips 1st seg as range is 2,1
            new_ycor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
