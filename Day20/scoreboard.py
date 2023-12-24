from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
ARG = "GAME OVER."



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(x=0, y=270)
        self.update_scoreboard()
        


    def update_scoreboard(self):

        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(arg=ARG, move=False, align=ALIGNMENT, font=FONT)



    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()
