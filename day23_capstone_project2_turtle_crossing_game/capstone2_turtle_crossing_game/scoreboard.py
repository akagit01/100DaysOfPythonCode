from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        #self.status="Game Over"
        self.hideturtle()
        self.pu()
        self.score=0
        self.level=0
        self.goto(-280,250)
        self.display_level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over",align="center", font=FONT)




    def display_level(self):
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", align="left", font=FONT)






