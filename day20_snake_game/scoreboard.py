from turtle import Turtle
ALIGNMENT='center'
FONT=('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_Scoreboard()



