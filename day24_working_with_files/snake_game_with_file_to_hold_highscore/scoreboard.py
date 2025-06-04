from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def read_high_score(self):
        with open("../../../../snake_game_highscore.txt",mode='r') as file:
            high_score_from_file=file.read()
            return  high_score_from_file

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.read_high_score()}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        highscore=self.read_high_score()
        if self.score > int(highscore):
            #self.highscore=self.score
            with open("D:\\python_16Days\\snake_game_highscore.txt",mode='w') as file:
                file.write(str(self.score))
        self.score=0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        #self.clear()
        self.update_scoreboard()
